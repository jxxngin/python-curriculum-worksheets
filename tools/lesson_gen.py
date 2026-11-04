"""주차 설계 파일(lesson_spec.py) 하나로 교안 파일들을 만든다.

사용법: python tools/lesson_gen.py worksheets/semester1/week01/lesson_spec.py [...]

만드는 파일: lesson.html, README.md, answer_key.md (+ mini_starter.py, mini_solution.py)
- 단계 코드는 spec 한 곳에서 정의되므로 교안과 solution이 자동으로 일치한다.
- "완성하면 이렇게 돼요" 화면은 solution을 실제로 실행해서 만든다(무작위 값은 demo_randoms로 고정).
- 프로젝트 주차처럼 mini 파일을 만들지 않으면 spec에 mini=False, complete=(실행할 파일, 입력, 무작위 값 또는 None)을 준다.
spec 필드 설명: docs/05-production-workflow.md "설계 파일". 예시: week01, week04의 lesson_spec.py
"""
import html, io, re, sys, random, builtins
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TPL = (ROOT / 'docs' / 'templates' / 'lesson-template.html').read_text(encoding='utf-8')
HEAD = TPL[:TPL.index('<body>')]
E = lambda s: html.escape(s, quote=False)


def code(lines, start=None, nonum=False, note=None):
    out = []
    if note:
        out.append(f'<span class="l"><span class="c">{E(note)}</span></span>')
    for l in lines:
        if l.lstrip().startswith('#'):
            out.append(f'<span class="l"><span class="c">{E(l)}</span></span>')
        else:
            out.append(f'<span class="l">{E(l)}</span>')
    cls = 'code nonum' if nonum else 'code'
    st = f' style="counter-reset: ln {start}"' if start is not None else ''
    return f'<pre class="{cls}"{st}>' + ''.join(out) + '</pre>'


def todo(items, title='📋 할 일'):
    return '<div class="todo"><h3>' + title + '</h3><ol>' + ''.join(f'<li>{i}</li>' for i in items) + '</ol></div>'


def check(items):
    return '<ul class="check">' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'


def tool(name, when, lines, result):
    return (f'<div class="tool"><div class="th">🧰 도구 카드 · {name}</div><p>{when}</p>'
            f'{code(lines, nonum=True)}<p class="muted">→ {result}</p></div>')


def table(headers, rows=0, first=None, widths=None):
    widths = widths or [None] * len(headers)
    h = ''.join(f'<th{f" style=width:{w}" if w else ""}>{x}</th>' for x, w in zip(headers, widths))
    body = ''
    for r in (first or []):
        body += '<tr>' + ''.join(f'<td class="w">{c}</td>' for c in r) + '</tr>'
    body += ('<tr>' + '<td class="w"></td>' * len(headers) + '</tr>') * rows
    return f'<table class="fill"><tr>{h}</tr>{body}</table>'


def run(src, inputs, randoms=None):
    it = iter(inputs)
    out = io.StringIO()

    def fin(p=''):
        v = next(it)
        out.write(p + v + '\n')
        return v
    g = {'input': fin, '__name__': '__main__'}
    if randoms is not None:
        r_it = iter(randoms)
        orig = random.randint
        random.randint = lambda a, b: next(r_it)
    old = sys.stdout
    sys.stdout = out
    try:
        exec(src, g)
    finally:
        sys.stdout = old
        if randoms is not None:
            random.randint = orig
    return out.getvalue().rstrip('\n')


def build(w):
    d = w['_dir']
    if w.get('mini', True) is False:
        f, inp, rnd = w['complete']
        complete = run((d / f).read_text(encoding='utf-8'), inp, rnd)
    else:
        complete = make_py(w, d)
    lesson(w, d, complete)
    return complete


def make_py(w, d):
    starter = [f"# {w['week']}주 미니 프로젝트: {w['title']}", '# 교안의 단계마다 그 아래에 코드를 이어 써요.', '']
    sol = [f"# {w['week']}주 미니 프로젝트: {w['title']} (정답)", '# 교안의 단계 순서대로 이어 쓴 완성본이에요.', '']
    for i, s in enumerate(w['steps'], 1):
        starter += [f"# 단계 {i}: {s['name']}", '', '']
        sol += [f"# 단계 {i}: {s['name']}"] + s.get('sol_lines', s['lines']) + ['']
    sol += ['# ----- 바꾸기 예시 (선생님용, 주석을 풀면 실행돼요) -----'] + ['# ' + l if l else '#' for l in w['change_example']]
    (d / 'mini_starter.py').write_text('\n'.join(starter) + '\n', encoding='utf-8')
    (d / 'mini_solution.py').write_text('\n'.join(sol) + '\n', encoding='utf-8')
    src = '\n'.join(sol)
    complete = run(src, w['demo_inputs'], w.get('demo_randoms'))
    # each step prefix must run
    acc = []
    for i, s in enumerate(w['steps'], 1):
        acc += s.get('sol_lines', s['lines'])
        run('\n'.join(acc), w['demo_inputs'] + ['1'] * 5, (w.get('demo_randoms') or []) + [1] * 5 if w.get('demo_randoms') else None)
    return complete


def lesson(w, d, complete):
    wl = (d / 'warmup.py').read_text(encoding='utf-8').splitlines()
    warm_code = code(wl[4:], start=4)
    B = []
    B.append(f'''  <header class="lesson-head">
    <span class="chip">{w.get('semester', 1)}학기 · {w['week_label']} · {w['badge']}</span>
    <h1>{w.get('h1', w['title'] + ' 만들기')}</h1>
    <div class="who">이름 <span></span> 날짜 <span></span></div>
  </header>''')
    B.append(f'''  <section class="block mission">
    <h2>🎯 오늘의 미션</h2>
    <p>{w['story']}</p>
    <div class="screen"><div class="bar">완성하면 이렇게 돼요</div><div class="body">{E(complete)}</div></div>
    {todo(w.get('mission_todo') or (['🔧 워밍업: 고장 난 코드를 고쳐요.'] + [f"🪜 단계 {i}: {s['name']}" for i, s in enumerate(w['steps'], 1)] + ['⭐ 내 것으로 바꿔요.']), '📋 오늘 할 일')}
  </section>''')
    B.append(f'''  <section class="block warmup">
    <h2>🔧 워밍업 <small>{w['warm_title']}</small></h2>
    {todo(['이상한 곳 <b>3개</b>에 동그라미 쳐요.', '<code>warmup.py</code>를 실행해서 오류 메시지를 봐요.', '고친 방법을 표에 적어요.'])}
    <p class="muted">1~4번 줄은 설명 주석이라 생략했어요. 5번 줄부터 실어요.</p>
    {warm_code}
    {table(['줄 번호', '오류 이름', '어떻게 고쳤나요?'], 3, widths=['20%', '30%', None])}
    <p class="muted">{w['warm_tip']}</p>
  </section>''')
    for i, s in enumerate(w['steps'], 1):
        steps_todo = []
        if s.get('tool'):
            steps_todo.append('🧰 도구 카드를 읽어요.')
        if s.get('lines'):
            steps_todo.append('⌨️ 코드를 <code>' + w.get('file', 'mini_starter.py') + '</code>의 <b>' + f'# 단계 {i}' + '</b> 아래에 따라 써요.')
            steps_todo.append('▶️ 실행하고, 화면에 나온 것을 적어요.')
        steps_todo += s.get('extra_todo', [])
        if s.get('todo'):
            steps_todo = s['todo']
        tools = ''.join(tool(*t) for t in s.get('tool', []))
        trace = ''
        if s.get('trace'):
            tq, th, trows = s['trace']
            trace = f'<div class="label">🔍 따라가기: {tq}</div>' + table(th, 0, first=trows)
        B.append(f'''  <section class="block step">
    <h2><span class="tag">단계 {i}</span> {s['name']}</h2>
    {todo(steps_todo)}
    {tools}
    {('<div class="label">⌨️ 따라 쓸 코드</div>' + code(s['lines'], nonum=True)) if s.get('lines') else ''}
    {s.get('body', '')}
    {('<div class="label">▶️ 실행하고 확인</div><div class="write' + (' small' if s.get('small') else '') + '"></div>') if s.get('write', bool(s.get('lines'))) else ''}
    {check(s['ok']) if s.get('ok') else ''}
    {trace}
  </section>''')
    c = w['change']
    B.append(f'''  <section class="block change">
    <h2>⭐ 내 것으로 바꾸기 <small>오늘의 완성 기준</small></h2>
    {todo(['표에 바꿀 내용을 먼저 적어요.', '코드를 고치고 실행해요.', '★ 꼭 하기 3개를 체크하면 완성!'])}
    {table(c['headers'], 2, first=[c['example']])}
    <div class="label">★ 꼭 하기 (이 3개를 하면 완성!)</div>
    {check(c['must'])}
    <div class="label">➕ 더 해 보기</div>
    {check(c['more'])}
    <div class="label">👀 친구에게 보여 주기: 친구의 한마디</div>
    <div class="write small"></div>
  </section>''')
    B.append(f'''  <section class="block new">
    <h2>💡 새로 만들기 <small>하고 싶은 사람</small></h2>
    {todo(['아이디어 하나를 골라요.', '무엇을 만들지 적고 만들어요.'])}
    {check(w['new_ideas'] + ['내 아이디어'])}
    <div class="write"></div>
    <h3>✅ 오늘의 마무리</h3>
    {check(['워밍업 오류 3개를 고쳤어요.', '단계를 하나씩 실행하며 만들었어요.', '★ 꼭 하기 3개를 완성했어요.', '친구에게 내 프로그램을 보여 줬어요.'])}
    <div class="label">{w['brag']}</div>
    <div class="write small"></div>
  </section>''')
    ch = w['challenge']
    B.append(f'''  <section class="block challenge">
    <h2>🚀 도전 프로젝트 <small>{ch['name']} · 일찍 끝낸 사람</small></h2>
    {todo(['<code>extension_starter.py</code>를 그대로 실행해 봐요.', ch['design'], '코드를 바꾸고 실행해서 체크해요.'])}
    <p>{ch['story']}</p>
    {''.join(tool(*t) for t in ch.get('tool', []))}
    {ch.get('body', '<div class="draw"></div>')}
    {check(ch['checks'])}
    <div class="label">➕ 더 해 보기</div>
    {check(ch['more'])}
  </section>''')
    hints = ''.join(f'<div class="hint"><div class="hh"><span>{h}</span><span>{dots}</span></div>{body}</div>' for h, dots, body in w['hints'])
    B.append(f'''  <section class="block hints">
    <h2>🃏 힌트 카드 <small>막히면 1번부터 차례로</small></h2>
    <div class="hints-grid">{hints}</div>
  </section>''')
    page = HEAD.replace('<title>{{N}}주차 교안</title>', f"<title>{w['week_label']} 교안</title>") + '<body>\n<main class="lesson">\n' + '\n\n'.join(B) + '\n</main>\n</body>\n</html>\n'
    (d / 'lesson.html').write_text(page, encoding='utf-8')
    return complete



strip = lambda s: re.sub(r'<[^>]+>', '', s)


def docs(w, complete):
    d = w['_dir']
    k = w['key']
    # README (교안 요약)
    r = [f"# {w['week_label']}: {w.get('h1', w['title'] + ' 만들기')}", '', '> 교안 요약이에요. 활동은 `lesson.html`을 열어서 해요(인쇄하면 학습지).', '',
         '## 🎯 오늘의 미션', '', strip(w['story']), '', '완성하면 이렇게 돼요:', '', '```', complete, '```', '',
         '## 🔧 워밍업', '', f"`warmup.py`를 실행하고 오류 3개를 고쳐요. ({w['warm_title']})", '']
    for i, s in enumerate(w['steps'], 1):
        r += [f"## 🪜 단계 {i}: {s['name']}", '']
        for t in s.get('tool', []):
            r += [f"> 🧰 **{strip(t[0])}**: {strip(t[1])}", '']
        if s.get('lines'):
            r += [f"`{w.get('file', 'mini_starter.py')}`의 `# 단계 {i}` 아래에 이어 써요.", '', '```python'] + s['lines'] + ['```', '']
        if s.get('readme'):
            r += [s['readme'], '']
        if s.get('ok'):
            r += ['✅ ' + ' / '.join(strip(x) for x in s['ok']), '']
    c = w['change']
    r += ['## ⭐ 내 것으로 바꾸기 (오늘의 완성 기준)', '', '**★ 꼭 하기**', ''] + [f'- [ ] {strip(x)}' for x in c['must']] + ['', '**➕ 더 해 보기**', ''] + [f'- [ ] {strip(x)}' for x in c['more']]
    r += ['', '## 💡 새로 만들기 (하고 싶은 사람)', ''] + [f'- {x}' for x in w['new_ideas']]
    ch = w['challenge']
    r += ['', f"## 🚀 도전 프로젝트: {ch['name']}", '', strip(ch['story']), '', '`extension_starter.py`를 실행해 보고 바꿔요.', ''] + [f'- [ ] {strip(x)}' for x in ch['checks']]
    r += ['', '## 🃏 힌트', '']
    for h, dots, body in w['hints']:
        r += ['<details>', f'<summary>{h} {dots}</summary>', '', strip(body).strip(), '', '</details>', '']
    (d / 'README.md').write_text('\n'.join(r), encoding='utf-8')
    # answer key
    a = [f"# {w['week_label']} 교안 정답지: {w['title']}", '', '교사용. `lesson.html`의 블록 순서대로 정리했다. 실행 결과는 `mini_solution.py`를 실제로 실행해 확인했다' + (' (무작위 값은 보물 문 2, 비밀번호 12로 고정).' if w.get('demo_randoms') else '.'), '',
         '## 🎯 미션', '', f"\"완성하면 이렇게 돼요\"는 {' / '.join(w['demo_inputs'])}를 넣고 실행한 화면이다.", '',
         f"## 🔧 워밍업 ({w['warm_title']})", '', '| 줄 | 오류 이름 | 고친 방법 |', '| --- | --- | --- |'] + [f'| {x} | {y} | {z} |' for x, y, z in k['warm']] + ['', '- ' + k['warm_note'], '']
    for i, (s, ans) in enumerate(zip(w['steps'], k['steps']), 1):
        a += [f"## 🪜 단계 {i} · {s['name']}", '', '- 실행하고 확인: ' + ans]
        if s.get('trace'):
            a += ['', f"**따라가기** ({strip(s['trace'][0])}, 실행해 확인함)", '', k['trace']]
        a += ['']
    a += ['## ⭐ 내 것으로 바꾸기', '', '- ' + k['change'], '- 완성 기준은 ★ 꼭 하기 3개다. 더 해 보기는 평가에 넣지 않는다.', '',
          f"## 🚀 도전 프로젝트 ({ch['name']})", '', '- ' + k['challenge'], '', '## 🃏 힌트', '', '정답이 아닌 안내다. "거의 코드" 힌트는 그대로 따라 쳐도 실행된다.', '']
    (d / 'answer_key.md').write_text('\n'.join(a), encoding='utf-8')


def main(spec_path):
    import runpy
    spec_path = Path(spec_path).resolve()
    w = runpy.run_path(str(spec_path))['SPEC']
    w['_dir'] = spec_path.parent
    w.setdefault('week_label', f"{w['week']}주차")
    complete = build(w)
    docs(w, complete)
    print(complete)


if __name__ == '__main__':
    for p in sys.argv[1:]:
        main(p)
