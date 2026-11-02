"""A4 워크시트(worksheet.html) 검사.

사용법: python tools/check_worksheet.py worksheets/semester1/week01/worksheet.html [...]

1) 구조 검사: .page 3~6쪽, 쪽마다 .foot, 이름/날짜 칸, 외부 리소스는 Google Fonts만
2) 레이아웃 검사(playwright가 있으면): 쪽마다 내용이 A4 밖으로 넘치거나 쪽 번호와 겹치지 않는지
   설치: pip install playwright && python -m playwright install chromium
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


class Scan(HTMLParser):
    def __init__(self):
        super().__init__()
        self.pages = 0
        self.foots = 0
        self.external = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        classes = (a.get("class") or "").split()
        if "page" in classes:
            self.pages += 1
        if "foot" in classes:
            self.foots += 1
        for key in ("src", "href"):
            url = a.get(key) or ""
            if url.startswith("http") and "fonts.googleapis.com" not in url and "fonts.gstatic.com" not in url:
                self.external.append(url)


LAYOUT_JS = """
async () => {
  await document.fonts.ready;
  return [...document.querySelectorAll('.page')].map((p, i) => {
    const r = p.getBoundingClientRect();
    let bottom = 0;
    p.querySelectorAll(':scope > *:not(.foot)').forEach(c => {
      bottom = Math.max(bottom, c.getBoundingClientRect().bottom);
    });
    const foot = p.querySelector('.foot');
    const footTop = foot ? foot.getBoundingClientRect().top : r.bottom;
    return {page: i + 1, gap: Math.round(footTop - bottom),
            overflow: p.scrollHeight > p.clientHeight + 1};
  });
}
"""


def check(path):
    errors = []
    html = Path(path).read_text(encoding="utf-8")
    s = Scan()
    s.feed(html)
    if not 3 <= s.pages <= 6:
        errors.append(f"쪽 수가 {s.pages}쪽이에요 (3~6쪽이어야 해요)")
    if s.foots != s.pages:
        errors.append(f".foot {s.foots}개 / .page {s.pages}개 (쪽마다 하나씩)")
    if "이름" not in html or "날짜" not in html:
        errors.append("머리글에 이름/날짜 칸이 없어요")
    if s.external:
        errors.append(f"허용되지 않은 외부 리소스: {s.external}")
    if not re.search(r"@page\s*\{\s*size:\s*A4", html):
        errors.append("@page { size: A4 } 가 없어요")

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print(f"  (playwright 없음: {path} 레이아웃 검사는 건너뜀)")
        return errors
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 900, "height": 1200})
        page.goto(Path(path).resolve().as_uri())
        page.wait_for_timeout(1500)
        for r in page.evaluate(LAYOUT_JS):
            if r["overflow"] or r["gap"] < 0:
                errors.append(f"{r['page']}쪽 내용이 넘쳐요 (여유 {r['gap']}px). 내용을 줄이거나 다음 쪽으로 옮겨요")
        browser.close()
    return errors


if __name__ == "__main__":
    failed = False
    for f in sys.argv[1:]:
        errs = check(f)
        print(("FAIL " if errs else "OK   ") + f)
        for e in errs:
            print("  - " + e)
        failed |= bool(errs)
    sys.exit(1 if failed else 0)
