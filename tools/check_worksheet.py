"""교안·워크시트 검사.

사용법: python tools/check_worksheet.py <파일.html> [...]

두 형식을 구분해 검사한다.
- 교안(새 형식, <main class="lesson">): docs/templates/lesson-template.html 기준
  1) 구조: 머리(이름/날짜), 활동 블록 순서(mission → warmup → step… → change → … → hints),
     블록마다 할 일 상자, 공통 스타일이 템플릿과 같은지, 외부 리소스, 편집기 표현
  2) playwright가 있으면: 휴대폰(375px)·노트북(1024px) 폭에서 가로로 넘치지 않는지,
     인쇄했을 때 끊기면 안 되는 칸(할 일, 코드, 쓰는 칸 등)이 한 쪽보다 크지 않은지, 인쇄 쪽 수
- A4 워크시트(예전 형식, <section class="page">): docs/templates/legacy/a4-worksheet-template.html 기준
  쪽 수, .foot, 공통 스타일, A4 안에서 넘치거나 잘리는 칸

playwright 설치: pip install playwright && python -m playwright install chromium
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LESSON_TEMPLATE = ROOT / "docs" / "templates" / "lesson-template.html"
LEGACY_TEMPLATE = ROOT / "docs" / "templates" / "legacy" / "a4-worksheet-template.html"
MARK = "/* ===== 주차별 추가"
BANNED = ("Thonny", "Ctrl+F5", "Ctrl+F2", "Step over", "변수 창", "디버거")
ORDER = ["mission", "warmup", "step", "change", "new", "challenge", "hints"]


def common_css(html):
    m = re.search(r"<style>\s*(.*?)</style>", html, re.S)
    css = m.group(1) if m else ""
    return css.split(MARK)[0]


class Scan(HTMLParser):
    def __init__(self):
        super().__init__()
        self.pages = 0
        self.foots = 0
        self.external = []
        self.blocks = []        # 활동 블록 종류 순서
        self.todo_in_block = []  # 블록마다 할 일 상자가 있는지
        self._block_depth = None
        self._depth = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        classes = (a.get("class") or "").split()
        if tag not in ("br", "img", "meta", "link", "input"):
            self._depth += 1
        if "page" in classes:
            self.pages += 1
        if "foot" in classes:
            self.foots += 1
        if tag == "section" and "block" in classes:
            kind = next((c for c in classes if c in ORDER), "?")
            self.blocks.append(kind)
            self.todo_in_block.append(False)
        if ("todo" in classes or "goal" in classes or "goals" in classes) and self.todo_in_block:
            self.todo_in_block[-1] = True
        for key in ("src", "href"):
            url = a.get(key) or ""
            if url.startswith("http") and "fonts.googleapis.com" not in url and "fonts.gstatic.com" not in url:
                self.external.append(url)

    def handle_endtag(self, tag):
        self._depth -= 1


def common_checks(path, html, template, errors):
    if template.exists() and Path(path).resolve() != template.resolve():
        if common_css(html) != common_css(template.read_text(encoding="utf-8")):
            errors.append(f"공통 스타일이 템플릿({template.relative_to(ROOT).as_posix()})과 달라요. 덧붙일 스타일은 '주차별 추가' 표시 아래에만 써요")
    banned = [w for w in BANNED if w in html]
    if banned:
        errors.append(f"특정 편집기 표현이 있어요: {banned} (docs/02-content-rules.md 편집기 중립)")
    if "이름" not in html or "날짜" not in html:
        errors.append("머리에 이름/날짜 칸이 없어요")


def playwright():
    try:
        from playwright.sync_api import sync_playwright
        return sync_playwright
    except ImportError:
        return None


# ------------------------------------------------------------------ 교안 (새 형식)
LESSON_PRINT_JS = """
async () => {
  await document.fonts.ready;
  const limit = 297 * 96 / 25.4 - 2 * 12 * 96 / 25.4;   // A4 높이 - 위아래 여백(12mm)
  const sel = '.todo, .tool, pre.code, .write, .screen, table.fill, .draw, .hint';
  return [...document.querySelectorAll(sel)]
    .filter(e => e.getBoundingClientRect().height > limit)
    .map(e => (e.innerText || e.className).trim().split(String.fromCharCode(10))[0].slice(0, 30));
}
"""


def check_lesson(path, html, s):
    errors = []
    common_checks(path, html, LESSON_TEMPLATE, errors)
    if s.external:
        errors.append(f"허용되지 않은 외부 리소스: {s.external}")
    kinds = s.blocks
    for need in ("mission", "warmup", "step", "change", "hints"):
        if need not in kinds:
            errors.append(f"활동 블록 '{need}'가 없어요")
    rank = [ORDER.index(k) for k in kinds if k in ORDER]
    if rank != sorted(rank):
        errors.append(f"활동 블록 순서가 고정 흐름과 달라요: {kinds} (docs/01-worksheet-format.md)")
    for k, has in zip(kinds, s.todo_in_block):
        if not has and k != "hints":
            errors.append(f"'{k}' 블록에 📌 목표 한 줄이 없어요")
    # 2차 피드백 규칙
    if 'class="todo"' in html:
        errors.append("할 일 목록(.todo)이 남아 있어요. 목표 한 줄 + 제자리 번호 지시로 바꿔요")
    if "따라 쓸 코드" in html:
        errors.append("'따라 쓸 코드'라는 말이 있어요. '기능 추가하기'로 써요")
    emoji = re.compile("[\U0001F300-\U0001FAFF\u2600-\u27BF]")
    for m in re.finditer(r'기능 추가하기.*?<pre[^>]*>(.*?)</pre>', html, re.S):
        if emoji.search(re.sub(r"<[^>]+>", "", m.group(1))):
            errors.append("기능 추가하기 코드에 이모지가 있어요. 따라 치기 어려우니 빼요")
            break
    # 3차 피드백: 번호 지시에 이모지 없음, 목표 줄은 📌, 힌트 카드마다 뱃지
    if re.search(r'<span class="n">[①②③④⑤]</span>\s*[🌀-🫿☀-➿▶]', html):
        errors.append("번호 지시(① ② ③) 옆에 이모지가 있어요. 빼요")
    if re.search(r'<div class="goal">(?!📌)', html):
        errors.append("목표 줄이 📌로 시작하지 않아요")
    if html.count('<div class="hint" ') != html.count('<span class="hb">'):
        errors.append("뱃지(단계 N / 새로 만들기 / 도전)가 없는 힌트 카드가 있어요")
    hints = re.findall(r'<div class="hint" data-group="(\w+)"><div class="hh"><span class="ht"><span class="hb">.*?</span><span>(.*?)</span></span><span class="hd">(.*?)</span>', html)
    for g, title, dots in hints:
        if re.fullmatch(r"\s*단계\s*\d+\s*", re.sub(r"<[^>]+>", "", title)):
            errors.append(f"힌트 제목이 '{title}'처럼 번호만 있어요. '하려는 일 · 막힌 상황'으로 써요")
    for g in ("new", "challenge"):
        if g not in kinds:
            continue
        levels = {d for gg, _, d in hints if gg == g}
        if levels != {"●○○", "●●○", "●●●"}:
            errors.append(f"'{g}' 힌트가 3단계(●○○ ●●○ ●●●)가 아니에요: {sorted(levels)}")
    readme = Path(path).with_name("README.md")
    if readme.exists() and re.search(r"&(lt|gt|amp);", readme.read_text(encoding="utf-8")):
        errors.append("README.md에 HTML 기호(&lt; 등)가 남아 있어요")

    sp = playwright()
    if not sp:
        print(f"  (playwright 없음: {path} 화면·인쇄 검사는 건너뜀)")
        return errors
    with sp() as p:
        browser = p.chromium.launch()
        for w in (375, 1024):
            page = browser.new_page(viewport={"width": w, "height": 900})
            page.goto(Path(path).resolve().as_uri())
            page.wait_for_timeout(1200)
            sw = page.evaluate("document.documentElement.scrollWidth")
            if sw > w + 1:
                errors.append(f"{w}px 화면에서 가로로 넘쳐요 (폭 {sw}px)")
            page.close()
        page = browser.new_page(viewport={"width": 1024, "height": 900})
        page.goto(Path(path).resolve().as_uri())
        page.wait_for_timeout(1200)
        page.emulate_media(media="print")
        for t in page.evaluate(LESSON_PRINT_JS):
            errors.append(f"인쇄할 때 한 쪽보다 큰 칸이 있어요: '{t}'. 나누거나 줄여요")
        page.close()
        page = browser.new_page()   # 새로 연 페이지로 PDF를 만들어야 쪽 수가 정확하다
        page.goto(Path(path).resolve().as_uri())
        page.wait_for_timeout(1200)
        pdf = page.pdf(prefer_css_page_size=True, print_background=True)
        n = len(re.findall(rb"/Type\s*/Page[^s]", pdf))
        if n > 16:
            errors.append(f"인쇄하면 {n}쪽이에요. 16쪽 이하로 줄여요")
        print(f"  (인쇄 {n}쪽)")
        browser.close()
    return errors


# ------------------------------------------------------------------ A4 워크시트 (예전 형식)
LEGACY_LAYOUT_JS = """
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
    const wide = [...p.querySelectorAll('pre, table, .row, .grid2, .hints')]
      .filter(e => e.scrollWidth > e.clientWidth + 1 || e.getBoundingClientRect().right > r.right - 40)
      .map(e => (e.innerText || '').trim().split(String.fromCharCode(10))[0].slice(0, 30));
    const cut = [...p.querySelectorAll('.quest, .qbody, .box, .concept, .hint, pre, .screen, .answer')]
      .filter(e => e.scrollHeight > e.clientHeight + 2)
      .map(e => (e.innerText || '').trim().split(String.fromCharCode(10))[0].slice(0, 30));
    return {page: i + 1, gap: Math.round(footTop - bottom),
            overflow: p.scrollHeight > p.clientHeight + 1, wide, cut};
  });
}
"""


def check_legacy(path, html, s):
    errors = []
    if not 3 <= s.pages <= 10:
        errors.append(f"쪽 수가 {s.pages}쪽이에요 (3~10쪽이어야 해요)")
    if s.foots != s.pages:
        errors.append(f".foot {s.foots}개 / .page {s.pages}개 (쪽마다 하나씩)")
    if s.external:
        errors.append(f"허용되지 않은 외부 리소스: {s.external}")
    common_checks(path, html, LEGACY_TEMPLATE, errors)
    if not re.search(r"@page\s*\{\s*size:\s*A4", html):
        errors.append("@page { size: A4 } 가 없어요")
    sp = playwright()
    if not sp:
        print(f"  (playwright 없음: {path} 레이아웃 검사는 건너뜀)")
        return errors
    with sp() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 900, "height": 1200})
        page.goto(Path(path).resolve().as_uri())
        page.wait_for_timeout(1500)
        for r in page.evaluate(LEGACY_LAYOUT_JS):
            if r["overflow"] or r["gap"] < 0:
                errors.append(f"{r['page']}쪽 내용이 넘쳐요 (여유 {r['gap']}px). 내용을 줄이거나 다음 쪽으로 옮겨요")
            for c in r["cut"]:
                errors.append(f"{r['page']}쪽 세로로 잘리는 칸: '{c}'. 내용을 줄이거나 다음 쪽으로 옮겨요")
            for w in r["wide"]:
                errors.append(f"{r['page']}쪽 가로로 잘리는 칸: '{w}'. 코드 줄을 짧게 나눠요(괄호 안에서만)")
        browser.close()
    return errors


def check(path):
    html = Path(path).read_text(encoding="utf-8")
    s = Scan()
    s.feed(html)
    if '<main class="lesson"' in html:
        return check_lesson(path, html, s)
    return check_legacy(path, html, s)


if __name__ == "__main__":
    failed = False
    for f in sys.argv[1:]:
        errs = check(f)
        print(("FAIL " if errs else "OK   ") + f)
        for e in errs:
            print("  - " + e)
        failed |= bool(errs)
    sys.exit(1 if failed else 0)
