"""웹에서 링크로 볼 수 있는 교안 사이트(GitHub Pages)를 만든다.

    python tools/build_site.py            # _site/ 에 만든다
    python tools/build_site.py --out DIR  # 다른 폴더에 만든다

- 목차(index.html)는 docs/curriculum.md 의 학기·주차 표로 만든다.
  교안이 있는 주차는 링크, 없는 주차는 "준비 중"으로 보인다.
- 교안(lesson.html, 없으면 worksheet.html)은 <학기>/<주차>/index.html 로 복사하고,
  화면 맨 위에 목차·이전·다음 막대를 끼워 넣는다(인쇄할 때는 숨는다).
  원본 파일은 고치지 않는다.
- GitHub Actions(.github/workflows/pages.yml)가 main에 푸시될 때마다 실행해 배포한다.
"""
import argparse
import html
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO_URL = "https://github.com/jxxngin/python-curriculum-worksheets"

# 학기마다 교안을 찾을 폴더. 앞에 있는 것이 우선이다.
# (폴더, 시안 여부) — 시안은 기준 확정 전 별도 제작본이라 목차에 '시안' 표시를 단다.
SOURCES = {
    1: [("worksheets/semester1", False)],
    2: [("worksheets/semester2", False),
        ("codex-created-semester2/worksheets/semester2", True)],
    3: [("worksheets/semester3", False)],
    4: [("worksheets/semester4", False)],
}

NAV_MARK = "<!-- site-nav -->"


# ---------- 커리큘럼 읽기 ----------

def clean_md(text):
    text = text.replace("\\~", "~").replace("\\_", "_")
    text = re.sub(r"`([^`]*)`", r"\1", text)
    return text.strip()


def parse_curriculum():
    """[{num, title, intro, tracks:[{name, note, headers, rows:[[...]]}]}]"""
    lines = (ROOT / "docs/curriculum.md").read_text(encoding="utf-8").splitlines()
    semesters = []
    sem = None
    track = None
    para_target = None  # 표 앞 설명 문단을 붙일 곳
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^## (\d)학기: (.+)$", line)
        if m:
            sem = {"num": int(m.group(1)), "title": clean_md(m.group(2)),
                   "intro": "", "tracks": []}
            semesters.append(sem)
            track = None
            para_target = sem
            i += 1
            continue
        if line.startswith("## "):
            sem = None
            track = None
            para_target = None
            i += 1
            continue
        if sem is None:
            i += 1
            continue
        m = re.match(r"^### (.+)$", line)
        if m:
            track = {"name": clean_md(m.group(1)), "note": "", "headers": [], "rows": []}
            para_target = track
            i += 1
            continue
        if line.startswith("|"):
            table = []
            while i < len(lines) and lines[i].startswith("|"):
                table.append(lines[i])
                i += 1
            cells = [[clean_md(c) for c in row.strip().strip("|").split("|")] for row in table]
            cells = [r for r in cells if not all(set(c) <= set("- :") for c in r)]
            if track is None:
                track = {"name": "", "note": "", "headers": [], "rows": []}
            track["headers"] = cells[0]
            track["rows"] = cells[1:]
            sem["tracks"].append(track)
            track = None
            para_target = None
            continue
        if line.strip() and para_target is not None:
            key = "intro" if para_target is sem else "note"
            if not para_target[key]:
                para_target[key] = clean_md(line)
        i += 1
    return semesters


# ---------- 교안 찾기 ----------

def week_dir_name(week):
    """'1' -> week01, '10~11' -> week10-11"""
    parts = [p.strip() for p in week.split("~")]
    if not all(p.isdigit() for p in parts):
        return None
    return "week" + "-".join("%02d" % int(p) for p in parts)


def find_lesson(sem_num, week):
    name = week_dir_name(week)
    if not name:
        return None
    for folder, draft in SOURCES.get(sem_num, []):
        d = ROOT / folder / name
        for fname in ("lesson.html", "worksheet.html"):
            if (d / fname).exists():
                return {"path": d / fname, "dir": d, "draft": draft,
                        "kind": "교안" if fname == "lesson.html" else "워크시트",
                        "slug": "semester%d/%s" % (sem_num, name)}
    return None


def lesson_heading(path):
    text = path.read_text(encoding="utf-8")
    m = re.search(r"<h1[^>]*>(.*?)</h1>", text, re.S)
    if not m:
        return ""
    return html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip()


# ---------- 교안에 끼우는 막대 ----------

NAV_STYLE = """<style>
.site-nav{position:sticky;top:0;z-index:1000;display:flex;align-items:center;gap:8px;flex-wrap:wrap;
  padding:8px 16px;background:rgba(255,255,255,.96);border-bottom:1px solid #d1d5db;
  font:500 14px/1.4 "Noto Sans KR","Malgun Gothic",sans-serif;color:#1f2937;backdrop-filter:blur(6px)}
.site-nav a{color:#2563eb;text-decoration:none;padding:4px 10px;border-radius:8px;border:1px solid #dbe4f3;background:#fff;white-space:nowrap}
.site-nav a:hover{background:#eff6ff}
.site-nav .sn-here{flex:1;min-width:0;text-align:center;font-weight:700;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.site-nav .sn-off{visibility:hidden}
@media (max-width:560px){.site-nav{justify-content:space-between}.site-nav .sn-here{display:none}}
@media print{.site-nav{display:none!important}}
</style>"""


def nav_html(label, prev, nxt, depth):
    up = "../" * depth
    def link(item, text_fmt, cls):
        if not item:
            return '<a class="sn-off" aria-hidden="true">%s</a>' % (text_fmt % "")
        return '<a class="%s" href="%s%s/">%s</a>' % (cls, up, item["slug"],
                                                      text_fmt % html.escape(item["short"]))
    return (NAV_MARK + NAV_STYLE +
            '<nav class="site-nav" aria-label="교안 이동">'
            '<a href="%s">☰ 목차</a>' % up +
            link(prev, "← %s", "sn-prev") +
            '<span class="sn-here">%s</span>' % html.escape(label) +
            link(nxt, "%s →", "sn-next") +
            "</nav>")


def inject_nav(text, nav):
    m = re.search(r"<body[^>]*>", text)
    if not m:
        return nav + text
    return text[:m.end()] + "\n" + nav + text[m.end():]


# ---------- 목차 ----------

INDEX_CSS = """
:root{--ink:#1f2937;--sub:#6b7280;--line:#e5e7eb;--bg:#f6f7fb;--paper:#fff;
  --main:#2563eb;--main-soft:#eff6ff;--more:#ea580c;--more-soft:#fff7ed;--muted:#9ca3af}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--ink:#e5e7eb;--sub:#9ca3af;--line:#374151;
  --bg:#111827;--paper:#1f2937;--main:#60a5fa;--main-soft:#1e3a5f;--more:#fb923c;--more-soft:#431407;--muted:#6b7280}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:"Noto Sans KR","Malgun Gothic","Apple SD Gothic Neo",sans-serif;line-height:1.6}
.wrap{max-width:1040px;margin:0 auto;padding:32px 16px 64px}
header h1{margin:0 0 6px;font-size:28px}
header p{margin:0;color:var(--sub)}
.jump{display:flex;gap:8px;flex-wrap:wrap;margin:20px 0 8px}
.jump a{padding:6px 14px;border-radius:999px;border:1px solid var(--line);background:var(--paper);color:var(--ink);text-decoration:none;font-size:14px}
.jump a:hover{border-color:var(--main);color:var(--main)}
section.sem{margin-top:36px}
section.sem h2{font-size:22px;margin:0 0 4px}
section.sem h2 small{font-size:14px;font-weight:500;color:var(--sub);margin-left:8px}
.intro{color:var(--sub);margin:0 0 14px;font-size:15px}
h3{font-size:16px;margin:20px 0 6px}
.note{color:var(--sub);font-size:14px;margin:0 0 8px}
.weeks{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px}
.week{background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:14px 16px;display:flex;flex-direction:column;gap:6px}
.week.ready{border-color:color-mix(in srgb,var(--main) 35%,var(--line))}
.week .top{display:flex;align-items:center;gap:8px}
.wk{font-weight:700;color:var(--main);font-size:14px;white-space:nowrap}
.week:not(.ready) .wk{color:var(--muted)}
.tag{font-size:12px;padding:1px 8px;border-radius:999px;background:var(--more-soft);color:var(--more);white-space:nowrap}
.tag.wait{background:var(--bg);color:var(--muted)}
.title{font-weight:700;font-size:16px}
.concept{color:var(--sub);font-size:13px}
.proj{font-size:14px}
.proj b{font-weight:500;color:var(--sub);margin-right:4px}
.links{display:flex;gap:8px;margin-top:auto;padding-top:6px;flex-wrap:wrap}
.links a{font-size:14px;text-decoration:none;border-radius:8px;padding:5px 12px}
.links a.open{background:var(--main);color:#fff}
.links a.open:hover{filter:brightness(1.1)}
.links a.files{border:1px solid var(--line);color:var(--sub)}
.links a.files:hover{color:var(--main);border-color:var(--main)}
footer{margin-top:48px;color:var(--sub);font-size:13px}
footer a{color:var(--sub)}
"""


def build_index(semesters, built):
    out = []
    jump = "".join('<a href="#s%d">%d학기 · %s</a>' % (s["num"], s["num"], html.escape(s["title"]))
                   for s in semesters)
    for s in semesters:
        ready = sum(1 for t in s["tracks"] for r in t["rows"] if (s["num"], r[0]) in built)
        total = sum(len(t["rows"]) for t in s["tracks"])
        out.append('<section class="sem" id="s%d">' % s["num"])
        out.append('<h2>%d학기 · %s<small>교안 %d / %d</small></h2>'
                   % (s["num"], html.escape(s["title"]), ready, total))
        if s["intro"]:
            out.append('<p class="intro">%s</p>' % html.escape(s["intro"]))
        for t in s["tracks"]:
            if t["name"]:
                out.append("<h3>%s</h3>" % html.escape(t["name"]))
            if t["note"]:
                out.append('<p class="note">%s</p>' % html.escape(t["note"]))
            out.append('<div class="weeks">')
            hdr = t["headers"]
            for row in t["rows"]:
                row = row + [""] * (len(hdr) - len(row))
                week, concept = row[0], row[1]
                b = built.get((s["num"], week))
                cls = "week ready" if b else "week"
                out.append('<div class="%s">' % cls)
                tag = ""
                if b and b["draft"]:
                    tag = '<span class="tag">시안</span>'
                elif not b:
                    tag = '<span class="tag wait">준비 중</span>'
                out.append('<div class="top"><span class="wk">%s주차</span>%s</div>'
                           % (html.escape(week), tag))
                if b and b["heading"]:
                    out.append('<div class="title">%s</div>' % html.escape(b["heading"]))
                out.append('<div class="concept">%s</div>' % html.escape(concept))
                for h, v in zip(hdr[2:], row[2:]):
                    if v:
                        out.append('<div class="proj"><b>%s</b>%s</div>'
                                   % (html.escape(h), html.escape(v)))
                if b:
                    rel = b["dir"].relative_to(ROOT).as_posix()
                    out.append('<div class="links"><a class="open" href="%s/">%s 열기</a>'
                               '<a class="files" href="%s/tree/main/%s">파이썬 파일·교사용</a></div>'
                               % (b["slug"], b["kind"], REPO_URL, rel))
                out.append("</div>")
            out.append("</div>")
        out.append("</section>")

    return """<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>파이썬 교안 목차</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
<style>%s</style>
</head>
<body>
<div class="wrap">
<header>
<h1>🐍 파이썬 1년 커리큘럼 교안</h1>
<p>초등 5~6학년 소그룹 파이썬 수업 · 학기당 11주, 주 1회 110분. 교안은 화면에서 보고, 인쇄하면 학습지가 됩니다.</p>
</header>
<nav class="jump">%s</nav>
%s
<footer>
인쇄할 때는 A4, 배경 그래픽 켜기, 머리글·바닥글 끄기를 권장합니다. ·
<a href="%s">GitHub 저장소</a>
</footer>
</div>
</body>
</html>
""" % (INDEX_CSS, jump, "\n".join(out), REPO_URL)


# ---------- 실행 ----------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "_site"))
    args = ap.parse_args()
    out = Path(args.out)
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    semesters = parse_curriculum()

    # 4학기는 게임별 표가 여러 개라 주차 번호만으로 교안을 고를 수 없다. 교안이 생기면 SOURCES/폴더 규칙을 정한다.
    order = []
    built = {}
    for s in semesters:
        if s["num"] == 4:
            continue
        for t in s["tracks"]:
            for row in t["rows"]:
                info = find_lesson(s["num"], row[0])
                if not info:
                    continue
                info["heading"] = lesson_heading(info["path"])
                info["short"] = "%d학기 %s주" % (s["num"], row[0])
                info["label"] = "%d학기 %s주차 · %s" % (s["num"], row[0], info["heading"] or info["kind"])
                built[(s["num"], row[0])] = info
                order.append(info)

    for idx, info in enumerate(order):
        prev = order[idx - 1] if idx > 0 else None
        nxt = order[idx + 1] if idx + 1 < len(order) else None
        text = info["path"].read_text(encoding="utf-8")
        text = inject_nav(text, nav_html(info["label"], prev, nxt, depth=2))
        dest = out / info["slug"] / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text, encoding="utf-8")

    (out / "index.html").write_text(build_index(semesters, built), encoding="utf-8")
    (out / ".nojekyll").write_text("", encoding="utf-8")
    print("교안 %d개, 목차 1개 -> %s" % (len(order), out))


if __name__ == "__main__":
    main()
