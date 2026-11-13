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
    return (f'<div class="tool"><div class="th">🧰 {name}</div><p>{when}</p>'
            f'{code(lines, nonum=True)}<p class="muted">→ {result}</p></div>')


def table(headers, rows=0, first=None, widths=None):
    widths = widths or [None] * len(headers)
    h = ''.join(f'<th{f" style=width:{w}" if w else ""}>{x}</th>' for x, w in zip(headers, widths))
    body = ''
    for r in (first or []):
        body += '<tr>' + ''.join(f'<td class="w">{c}</td>' for c in r) + '</tr>'
    body += ('<tr>' + '<td class="w"></td>' * len(headers) + '</tr>') * rows
    return f'<table class="fill"><tr>{h}</tr>{body}</table>'


def run(src, inputs, randoms=None, choices=None):
    """src를 실행한 화면을 돌려준다. randoms: randint가 차례로 낼 값, choices: random.choice가 차례로 고를 값.
    time.sleep()은 기다리지 않는다."""
    import time
    it = iter(inputs)
    out = io.StringIO()

    def fin(p=''):
        v = next(it)
        out.write(p + v + '\n')
        return v
    g = {'input': fin, '__name__': '__main__'}
    orig = random.randint, random.choice, time.sleep
    if randoms is not None:
        r_it = iter(randoms)
        random.randint = lambda a, b: next(r_it)
    if choices is not None:
        c_it = iter(choices)
        random.choice = lambda seq: next(c_it)
    time.sleep = lambda s: None
    old = sys.stdout
    sys.stdout = out
    try:
        exec(src, g)
    finally:
        sys.stdout = old
        random.randint, random.choice, time.sleep = orig
    return out.getvalue().rstrip('\n')


def build(w):
    d = w['_dir']
    if w.get('mini', True) is False:
        f, inp, rnd = w['complete'][:3]
        ch = w['complete'][3] if len(w['complete']) > 3 else None
        complete = run((d / f).read_text(encoding='utf-8'), inp, rnd, ch)
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
    where = w.get('change_where', '맨 아래에 이어서')
    sol += [f'# ----- 바꾸기 예시 (선생님용). 주석을 풀어 {where} 넣으면 실행돼요 -----'] + ['# ' + l if l else '#' for l in w['change_example']]
    (d / 'mini_starter.py').write_text('\n'.join(starter) + '\n', encoding='utf-8')
    (d / 'mini_solution.py').write_text('\n'.join(sol) + '\n', encoding='utf-8')
    src = '\n'.join(sol)
    complete = run(src, w['demo_inputs'], w.get('demo_randoms'), w.get('demo_choices'))
    # each step prefix must run
    acc = []
    for i, s in enumerate(w['steps'], 1):
        acc += s.get('sol_lines', s['lines'])
        ch = w.get('demo_choices')
        run('\n'.join(acc), w.get('prefix_inputs', w['demo_inputs'] + ['1'] * 5), (w.get('demo_randoms') or []) + [1] * 5 if w.get('demo_randoms') else None, ch * 2 if ch else None)
    return complete


def hint_badges(w):
    """힌트마다 뱃지를 붙인다. 단계 힌트는 나온 차례대로 단계 1, 2, …(단계마다 한 칸), 나머지는 활동 이름."""
    n, out = 0, []
    hints = list(w['hints'])
    for wm in reversed(warmups(w)):   # 워밍업 힌트 카드가 맨 앞(워밍업이 여럿이면 뱃지에 주차를 붙인다)
        if wm.get('hint'):
            hints.insert(0, (wm['hint'][0], '●○○', wm['hint'][1], 'warmup', wm.get('label', '워밍업')))
    names = {'warmup': '워밍업', 'change': '바꾸기', 'new': w.get('new_badge', '새로 만들기'), 'challenge': '도전'}
    for h, dots, body, g, *badge in hints:
        if g == 'step':
            n += 1
            b = f'단계 {n}'
        else:
            b = badge[0] if badge else names[g]
        out.append((b, h, dots, body, g))
    if n != len(w['steps']):
        raise SystemExit(f"단계 힌트 {n}개 / 단계 {len(w['steps'])}개: 단계마다 한 칸씩 둬요")
    return out


def warmups(w):
    """워밍업 목록. 보통은 하나(warm_title·warm_errors·warm_hint, warmup.py).
    여러 주에 걸친 교안은 spec의 warmups=[dict(file, title, errors, hint, label, before_step, key, note), …]로 여럿을 둔다.
    before_step: 그 워밍업을 둘 자리(단계 번호, 1부터). 첫 워밍업은 미션 바로 뒤."""
    if w.get('warmups'):
        return w['warmups']
    return [dict(file='warmup.py', title=w['warm_title'], errors=w['warm_errors'], hint=w.get('warm_hint'),
                 key=w['key']['warm'], note=w['key']['warm_note'], skip=w.get('warm_skip'))]


def warmup_block(d, wm, multi):
    wl = (d / wm['file']).read_text(encoding='utf-8').splitlines()
    skip = wm.get('skip')
    if skip is None:   # 맨 앞 주석과 그 뒤 빈 줄은 생략하고 코드가 있는 첫 줄부터(5차 피드백)
        skip = 0
        while skip < len(wl) and (not wl[skip].strip() or wl[skip].lstrip().startswith('#')):
            skip += 1
    skip_note = f'1~{skip}번 줄은 설명 주석이라 생략했어요. {skip + 1}번 줄부터 실었어요.'
    label = f"{wm['label']} " if multi else '워밍업 '
    return f'''  <section class="block warmup">
    <h2>🔧 {label}<small>{wm['title']}</small></h2>
    {goal('오류 메시지를 읽고 오류 3개를 고친다.')}
    {act('①', '코드 읽기', '이상한 곳 3개 표시 · ' + skip_note, code(wl[skip:], start=skip))}
    {act('②', '실행하고 고치기', f"<code>{wm['file']}</code>를 실행하고 오류 메시지를 보며 표에 적기", err_table(wm['errors']) + table(['줄 번호', '오류 이름', '어떻게 고쳤나요?'], 3, widths=['20%', '30%', None]))}
  </section>'''


def err_table(errors):
    """워밍업 오류 사전 표(5차 피드백): 오류 이름 | 뜻 | 확인할 곳."""
    rows = ''.join(f'<tr><td><b>{n}</b></td><td>{m}</td><td>{c}</td></tr>' for n, m, c in errors)
    return f'<table class="fill ref"><tr><th style=width:24%>오류 이름</th><th>뜻</th><th>확인할 곳</th></tr>{rows}</table>'


def goal(text):
    return f'<div class="goal">📌 목표: {text}</div>'


def act(n, name, how, inner):
    """제자리 지시: 번호 + 이름 + 짧은 설명, 바로 다음 부품과 .keep으로 묶는다."""
    num = f'<span class="n">{n}</span>' if n else ''
    h = f' <span class="how">{how}</span>' if how else ''
    return f'<div class="keep"><div class="label">{num}{name}{h}</div>{inner}</div>'


def wrap_list(w):
    """오늘의 마무리 체크리스트. 프로젝트 주차는 spec의 wrap으로 바꾼다."""
    return w.get('wrap', ['워밍업 오류 3개를 고쳤다.', '단계마다 실행하며 완성했다.', '★ 3개를 완성했다.', '친구에게 보여 줬다.'])


def record_box(s):
    if s.get('record_table'):
        hd, rows = s['record_table']
        return table(hd, 0, first=rows)
    return '<div class="write' + (' small' if s.get('small') else '') + '"></div>'


def lesson(w, d, complete):
    f = w.get('file', 'mini_starter.py')
    wms = warmups(w)
    multi = len(wms) > 1
    B = []
    B.append(f'''  <header class="lesson-head">
    <span class="chip">{w.get('semester', 1)}학기 · {w['week_label']} · {w['badge']}</span>
    <h1>{w.get('h1', w['title'] + ' 만들기')}</h1>
    <div class="who">이름 <span></span> 날짜 <span></span></div>
  </header>''')
    goals = ''.join(f'<li>{g}</li>' for g in w['goals'])
    B.append(f'''  <section class="block mission">
    <h2>🎯 오늘의 미션</h2>
    <p>{w['story']}</p>
    <div class="goals"><h3>📌 오늘의 목표</h3><ul>{goals}</ul></div>
    <div class="screen"><div class="bar">{w.get('complete_bar', '완성하면 이렇게 돼요')}</div><div class="body">{E(complete)}</div></div>
  </section>''')
    B.append(warmup_block(d, wms[0], multi))
    later = {wm['before_step']: wm for wm in wms[1:]}
    for i, s in enumerate(w['steps'], 1):
        if i in later:
            B.append(warmup_block(d, later[i], multi))
        tools = ''.join(tool(*t) for t in s.get('tool', []))
        parts = [goal(s['goal']), tools]
        if s.get('lines'):
            parts.append(act('①', '기능 추가하기', f'<code>{f}</code>의 <b># 단계 {i}</b> 아래에 입력', code(s['lines'], nonum=True)))
            parts.append(act('②', '실행하고 확인', s.get('record', '마지막 줄 적기'), record_box(s)))
        parts.append(s.get('body', ''))
        if s.get('ok'):
            parts.append(check(s['ok']))
        if s.get('trace'):
            tq, th, trows = s['trace']
            parts.append(act('③', '따라가기', tq, table(th, 0, first=trows)))
        B.append(f'''  <section class="block step">
    <h2><span class="tag">단계 {i}</span> {s['name']}</h2>
    {''.join(parts)}
  </section>''')
    c = w['change']
    a1 = c.get('act1', ('설계하기', '바꿀 내용을 표에 먼저 적기'))
    body1 = c['body'] if 'body' in c else table(c['headers'], 2, first=[c['example']])
    fr = c.get('friend', ('👀 친구에게 보여 주기', '친구의 한마디'))
    B.append(f'''  <section class="block change">
    <h2>{c.get('title', '⭐ 내 것으로 바꾸기')} <small>{c.get('small', '오늘의 완성 기준')}</small></h2>
    {goal(c['goal'])}
    {act('①', a1[0], a1[1], body1)}
    {act('②', c.get('act2', '고치고 실행하기'), '★ 3개를 하면 완성', check(['★ ' + x for x in c['must']]))}
    <div class="label">➕ 더 해 보기</div>
    {check(c['more'])}
    {act('', fr[0], fr[1], '<div class="write small"></div>')}
  </section>''')
    new_body = w.get('new_body') or (act('①', '아이디어 고르기', '하나에 표시', check(w['new_ideas'] + ['내 아이디어']))
                                     + '\n    ' + act('②', '계획 적고 만들기', '무엇을 묻고 무엇을 보여 줄지', '<div class="write"></div>'))
    B.append(f'''  <section class="block new">
    <h2>{w.get('new_title', '💡 새로 만들기')} <small>{w.get('new_small', '하고 싶은 사람')}</small></h2>
    {goal(w.get('new_goal', '오늘 만든 프로그램에 내 아이디어 기능을 하나 더한다.'))}
    {new_body}
    <h3>✅ 오늘의 마무리</h3>
    {check(wrap_list(w))}
    {act('', w['brag'], '', '<div class="write small"></div>')}
  </section>''')
    ch = w.get('challenge')
    if ch:
        B.append(f'''  <section class="block challenge">
    <h2>🚀 도전 프로젝트 <small>{ch['name']} · 일찍 끝낸 사람</small></h2>
    <p class="why"><b>왜 만들까?</b> {ch['why']}</p>
    {goal(ch['goal'])}
    {''.join(tool(*t) for t in ch.get('tool', []))}
    {act('①', '실행해 보기', ch.get('run', '<code>extension_starter.py</code>를 그대로 실행'), '')}
    {act('②', ch['design'][0], ch['design'][1], ch.get('body', '<div class="draw"></div>'))}
    {act('③', '바꾸고 체크하기', '', check(ch['checks']))}
    <div class="label">➕ 더 해 보기</div>
    {check(ch['more'])}
  </section>''')
    hints = ''.join(f'<div class="hint" data-group="{g}"><div class="hh"><span class="ht"><span class="hb">{b}</span><span>{h}</span></span><span class="hd">{dots}</span></div>{body}</div>' for b, h, dots, body, g in hint_badges(w))
    B.append(f'''  <section class="block hints">
    <h2>🃏 힌트 카드 <small>막힌 상황에 맞는 카드를 찾아 ●○○부터</small></h2>
    <div class="hints-list">{hints}</div>
  </section>''')
    page = HEAD.replace('<title>{{N}}주차 교안</title>', f"<title>{w['week_label']} 교안</title>") + '<body>\n<main class="lesson">\n' + '\n\n'.join(B) + '\n</main>\n</body>\n</html>\n'
    (d / 'lesson.html').write_text(page, encoding='utf-8')
    return complete


def md(s):
    """HTML 조각 → README용 마크다운(백틱 유지, 기호 풀기)."""
    s = re.sub(r'<code>(.*?)</code>', r'`\1`', s)
    s = re.sub(r'<br\s*/?>', ' ', s)
    s = re.sub(r'<[^>]+>', '', s)
    return html.unescape(s).strip()


def md_block(body):
    """교안 칸(HTML) → README 마크다운. 표는 마크다운 표로, 빈칸은 ____로."""
    body = re.sub(r'<span class="blank"></span>', '____', body)
    out = []
    for part in re.split(r'(<table.*?</table>)', body, flags=re.S):
        if part.startswith('<table'):
            rows = re.findall(r'<tr>(.*?)</tr>', part, re.S)
            cells = [[md(c) or ' ' for c in re.findall(r'<t[hd][^>]*>(.*?)</t[hd]>', r, re.S)] for r in rows]
            if cells:
                out += ['| ' + ' | '.join(cells[0]) + ' |', '|' + ' --- |' * len(cells[0])] + ['| ' + ' | '.join(c) + ' |' for c in cells[1:]] + ['']
        else:
            for t in re.findall(r'<p[^>]*>(.*?)</p>', part, re.S) or ([part] if md(part) else []):
                out += [md(t), '']
    return '\n'.join(out).strip()


def md_body(body):
    if '<pre' in body:
        lines = re.findall(r'<span class="l">(.*?)</span>(?=<span class="l">|</pre>)', body, re.S)
        lines = [html.unescape(re.sub(r'<[^>]+>', '', l)) for l in lines]
        pre_text = md(body[:body.index('<pre')])
        out = ([pre_text, ''] if pre_text else []) + ['```python'] + lines + ['```']
        return '\n'.join(out)
    return md(body)


def readme_warm(wm, multi):
    head = f"## 🔧 {wm['label']}" if multi else '## 🔧 워밍업'
    return [head, '', f"📌 목표: 오류 메시지를 읽고 오류 3개를 고친다. ({wm['title']})", '', f"`{wm['file']}`를 실행하고 고친다.", '',
            '| 오류 이름 | 뜻 | 확인할 곳 |', '| --- | --- | --- |'] + [f'| {md(n)} | {md(m)} | {md(c)} |' for n, m, c in wm['errors']] + ['']


def key_warm(wm, multi):
    head = f"## 🔧 {wm['label']} ({wm['title']})" if multi else f"## 🔧 워밍업 ({wm['title']})"
    return [head, '', '| 나타나는 순서 | 줄 | 오류 이름 (실제 메시지) | 고친 방법 |', '| --- | --- | --- | --- |'] +         [f'| {o} | {x} | {y} | {z} |' for o, x, y, z in wm['key']] + ['', '- ' + wm['note'], '']


def docs(w, complete):
    d = w['_dir']
    k = w['key']
    f = w.get('file', 'mini_starter.py')
    wms = warmups(w)
    multi = len(wms) > 1
    later = {wm['before_step']: wm for wm in wms[1:]}
    r = [f"# {w['week_label']}: {w.get('h1', w['title'] + ' 만들기')}", '', '> 교안 요약이다. 활동은 `lesson.html`에서 한다(인쇄하면 학습지).', '',
         '## 🎯 오늘의 미션', '', md(w['story']), '', '**오늘의 목표**', ''] + [f'- {md(g)}' for g in w['goals']] + ['', md(w.get('complete_bar', '완성하면 이렇게 돼요')) + ':', '', '```', complete, '```', '']
    r += readme_warm(wms[0], multi)
    for i, s in enumerate(w['steps'], 1):
        if i in later:
            r += readme_warm(later[i], multi)
        r += [f"## 🪜 단계 {i}: {s['name']}", '', f"📌 목표: {md(s['goal'])}", '']
        for t in s.get('tool', []):
            r += [f"> 🧰 **{md(t[0])}**: {md(t[1])}", '>', '> ```python'] + [f'> {l}' for l in t[2]] + ['> ```', f'> → {md(t[3])}', '']
        if s.get('lines'):
            r += [f"① 기능 추가하기: `{f}`의 `# 단계 {i}` 아래에 입력", '', '```python'] + s['lines'] + ['```', '', f"② 실행하고 확인: {md(s.get('record', '마지막 줄 적기'))}", '']
        if s.get('readme'):
            r += [s['readme'], '']
        if s.get('ok'):
            r += ['✅ ' + ' / '.join(md(x) for x in s['ok']), '']
        if s.get('trace'):
            r += [f"③ 따라가기: {md(s['trace'][0])}", '']
    c = w['change']
    r += [f"## {md(c.get('title', '⭐ 내 것으로 바꾸기'))} ({md(c.get('small', '오늘의 완성 기준'))})", '', f"📌 목표: {md(c['goal'])}", '']
    if c.get('readme'):
        r += [c['readme'], '']
    r += ['**★ 꼭 하기**', ''] + [f'- [ ] {md(x)}' for x in c['must']] + ['', '**➕ 더 해 보기**', ''] + [f'- [ ] {md(x)}' for x in c['more']]
    fr = f"{md(c['friend'][0])}: {md(c['friend'][1])}" if c.get('friend') else '👀 친구에게 보여 주고 한마디 받기'
    r += ['', fr, '', f"## {md(w.get('new_title', '💡 새로 만들기'))} ({md(w.get('new_small', '하고 싶은 사람'))})", '']
    r += [w['new_readme']] if w.get('new_readme') else [f'- {md(x)}' for x in w['new_ideas']]
    r += ['', '**✅ 오늘의 마무리**', ''] + [f'- [ ] {md(x)}' for x in wrap_list(w)]
    ch = w.get('challenge')
    if ch:
        r += ['', f"## 🚀 도전 프로젝트: {ch['name']}", '', f"**왜 만들까?** {md(ch['why'])}", '', f"📌 목표: {md(ch['goal'])}", '']
        for t in ch.get('tool', []):
            r += [f"> 🧰 **{md(t[0])}**: {md(t[1])}", '']
        r += ['① 실행해 보기: ' + md(ch.get('run', '<code>extension_starter.py</code>를 그대로 실행')), '', f"② {md(ch['design'][0])}: {md(ch['design'][1])}", '']
        if ch.get('body'):
            r += [md_block(ch['body']), '']
        r += ['③ 바꾸고 체크하기', ''] + [f'- [ ] {md(x)}' for x in ch['checks']] + ['', '**➕ 더 해 보기**', ''] + [f'- {md(x)}' for x in ch['more']]
    r += ['', '## 🃏 힌트', '']
    for b, h, dots, body, g in hint_badges(w):
        r += ['<details>', f'<summary>[{b}] {md(h)} {dots}</summary>', '', md_body(body), '', '</details>', '']
    (d / 'README.md').write_text('\n'.join(r), encoding='utf-8')
    note = f" ({w['demo_random_note']})" if w.get('demo_random_note') else ''
    intro = k.get('intro', '교사용. `lesson.html`의 블록 순서대로 정리했다. 실행 결과는 `mini_solution.py`를 Python 3.11로 실제로 실행해 확인했다' + note + '.')
    mission = k.get('mission', f"\"완성하면 이렇게 돼요\"는 {' / '.join(w.get('demo_inputs', []))}를 넣고 실행한 화면이다.")
    a = [f"# {w['week_label']} 교안 정답지: {w['title']}", '', intro, '', '## 🎯 미션', '', mission, '']
    a += key_warm(wms[0], multi)
    for i, (s, ans) in enumerate(zip(w['steps'], k['steps']), 1):
        if i in later:
            a += key_warm(later[i], multi)
        a += [f"## 🪜 단계 {i} · {s['name']}", '', f"- {k.get('step_label', '실행하고 확인')}: " + ans]
        if s.get('trace'):
            a += ['', f"**따라가기** ({md(s['trace'][0])}, 실행해 확인함)", '', k['trace']]
        a += ['']
    a += [f"## {md(c.get('title', '⭐ 내 것으로 바꾸기'))}", '', '- ' + k['change'], '- 완성 기준은 ★ 3개다. 더 해 보기는 평가에 넣지 않는다.', '']
    if k.get('new'):
        a += [f"## {md(w.get('new_title', '💡 새로 만들기'))}", '', '- ' + k['new'], '']
    if ch:
        a += [f"## 🚀 도전 프로젝트 ({ch['name']})", '', '- ' + k['challenge'], '']
    a += ['## 🃏 힌트', '', '정답이 아닌 안내다. "거의 코드" 힌트는 적힌 위치에 넣으면 실행된다.', '']
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
