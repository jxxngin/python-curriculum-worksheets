# -*- coding: utf-8 -*-
from pathlib import Path
import importlib.util, html, os, runpy

HERE = Path(__file__).resolve().parent
REPO = Path(os.environ.get('CURRICULUM_REPO', str(HERE.parent)))
OUT = HERE
spec = importlib.util.spec_from_file_location('lesson_gen', REPO/'tools/lesson_gen.py')
gen = importlib.util.module_from_spec(spec); spec.loader.exec_module(gen)
E = html.escape
def lines(s): return s.strip('\n').splitlines()
def write(p,s): p.write_text(s,encoding='utf-8')
def block(kind,title,body,actions):
    return f'<section class="block {kind}"><h2>{title}</h2>'+gen.todo(actions)+body+'</section>'
def c(src): return gen.code(lines(src) if isinstance(src,str) else src,nonum=True)

from preview import render
weeks = [runpy.run_path(str(p))['SPEC'] for p in sorted(OUT.glob('worksheets/semester2/week*/lesson_spec.py'))]

for w in weeks:
    for i,s in enumerate(w['steps']):
        if i and not s['lines'][0].startswith('#'):
            s['lines'].insert(0,f'# 단계 {i} 코드 아래에 이어서 써요.')
    n=w['week']; d=OUT/'worksheets'/'semester2'/f'week{n:02d}'; d.mkdir(parents=True,exist_ok=True)
    # A single spec supplies all displayed code and practice files.
    # lesson_spec.py is the source; never overwrite it during generation.
    warm='# 오류 3개를 찾아 고쳐 보세요.\n# 먼저 오류 메시지를 읽어요.\n# 고친 뒤 다시 실행해요.\n# 표시된 줄 번호는 이 파일과 같아요.\n'+w['warm']+'\n'
    write(d/'warmup.py',warm)
    starter=['# 2학기 '+str(n)+'주: '+w['title'],'# 단계 주석 아래에 코드를 이어 써요.']
    sol=[]
    for i,s in enumerate(w['steps'],1):
        starter += ['',f'# 단계 {i}: {s["name"]}','','']
        sol += [f'# 단계 {i}: {s["name"]}']+s['lines']+['']
    turtle=n<4
    if turtle:
        starter += ['# 모든 단계 아래 마지막 줄에 t.done()을 써요.']
        sol += ['# 그림 창을 열어 둬요.','t.done()','']
    sol+=['# 꼭 하기 세 가지를 모두 바꾼 예시는 mini_change_solution.py에 있다.']
    write(d/'mini_starter.py','\n'.join(starter).rstrip()+'\n');write(d/'mini_solution.py','\n'.join(sol)+'\n')
    for suffix,key in [('starter','extension'),('solution','extension_solution')]:write(d/f'extension_{suffix}.py','# '+w['challenge_name']+'\n'+w[key]+'\n')
    write(d/'mini_change_solution.py', '# 교사용: 꼭 하기 세 가지를 만족하는 바꾸기 예시\n'+w['change_solution']+'\n')
    B=[]
    B.append(f'<header class="lesson-head"><span class="chip">2학기 · {n}주차 · {w["badge"]}</span><h1>{w["title"]}</h1><div class="who">이름 <span></span> 날짜 <span></span></div></header>')
    preview=['노란 원 얼굴 → 같은 높이의 검은 눈 두 개 → 웃는 입','한 중심에서 네 방향으로 펼쳐진 청록색 삼각 날개','크기가 다른 분홍 사탕 세 개, 막대와 흰 장식 세 개씩','산 높이(m)\n8849\n8516\n8586\n낮은 산부터\n8516\n8586\n8849\n산 개수: 3\n가장 높은 산: 8849m\n가장 낮은 산: 8516m\n높이 합계: 25951m\n평균 높이: 8650m (정수 몫)'][n-1]
    B.append(block('mission','🎯 오늘의 미션',f'<p>{w["story"]}</p><div class="screen"><div class="bar">완성하면 이렇게 돼요</div><div class="body">{E(preview)}</div></div>'+(render('\n'.join(sol),w['title']) if turtle else ''), ['완성 모습을 살펴봐요.',f'워밍업 뒤 {len(w["steps"])}단계를 만들어요.','내 것으로 바꾸고 친구에게 보여 줘요.']))
    B.append(block('warmup','🔧 워밍업', '<p>1~4번 줄은 설명 주석이라 생략했어요.</p>'+gen.code(warm.splitlines()[4:],start=4)+gen.table(['줄 번호','오류 이름','고친 방법'],3)+'<p class="muted">'+('SyntaxError는 문법, NameError는 이름, TypeError는 값 종류를 확인해요.' if n==1 else 'SyntaxError는 문법, AttributeError는 도구 이름, IndentationError는 들여쓰기를 확인해요.' if n in (2,3) else 'IndexError는 목록 위치, AttributeError는 도구 이름, TypeError는 값 종류를 확인해요.')+'</p>',['코드에서 이상한 곳 세 개를 찾아요.','warmup.py를 실행하고 오류 메시지를 읽어요.','고친 방법을 표에 적어요.']))
    for i,s in enumerate(w['steps'],1):
        body=''.join(gen.tool(*t) for t in s['tool'])+c(s['lines'])
        if s.get('note'): body+='<p>'+s['note']+'</p>'
        if turtle:
            body+=('<p>그림 창을 유지하려면 맨 아래에 <code>t.done()</code>을 한 번 써요. 다음 단계는 그 줄 바로 위에 이어 써요. 실행을 마친 창은 닫고 다시 실행해요.</p>' if i==1 else '<p><code>t.done()</code> 바로 위에 이어 써요. 그림 창을 닫고 다시 실행해요.</p>')
        body+='<div class="label">▶️ 실행하고 확인: 달라진 모습을 적거나 그려요.</div><div class="write"></div>'+gen.check(s['ok'])
        if i==len(w['steps']) and n!=4:body+='<div class="label">🔍 따라가기: '+w['trace_q']+'</div>'+gen.table(w['trace_heads'],1)
        B.append(block('step',f'<span class="tag">단계 {i}</span> {s["name"]}',body,['도구 카드를 읽어요.' if s['tool'] else '앞 단계의 결과를 살펴봐요.','mini_starter.py의 단계 표시 아래에 새 코드를 써요.','실행하고 달라진 모습을 기록해요.']))
    body=gen.table(['바꿀 부분','내 계획'],1,first=[] if n==4 else [w['plan_example']])
    if n==4:
        body+=gen.tool('값 빼기와 마지막 값 꺼내기',w['hint_tool'],['numbers = [10, 20, 30]','numbers.remove(20)','last = numbers.pop()'],'numbers는 [10], last는 30이에요.')
    if n==4: body+='<div class="label">🔍 따라가기: '+w['trace_q']+'</div>'+gen.table(w['trace_heads'],1)
    body+='<p>'+w['change_guidance']+'</p>'
    body+='<div class="label">★ 꼭 하기 · 세 가지가 오늘의 완성 기준이에요.</div>'+gen.check(w['must'])+'<div class="label">➕ 더 해 보기</div>'+gen.check(w['more'])+'<div class="label">친구의 한마디</div><div class="write small"></div>'
    B.append(block('change','⭐ 내 것으로 바꾸기',body,['계획을 표에 적어요.','코드를 바꾸고 실행해요.','꼭 하기 세 가지를 체크하고 친구에게 보여 줘요.']))
    body=gen.check(w['new']+['내 아이디어'])+'<div class="draw"></div>'
    if n==4:
        body+='<p>높이와 이름을 묶는 기본 코드를 제공해요. 첫 값인 높이 순서로 함께 정렬돼요.</p>'+c('''mountains = [[8849, "에베레스트"], [8516, "로체"], [8586, "칸첸중가"]]
mountains.sort()
for mountain in mountains:
    print(mountain[0], mountain[1])''')
    body+='<h3>✅ 오늘의 마무리</h3>'+gen.check(['오류 세 개를 고쳤어요.','단계를 실행하며 만들었어요.','꼭 하기 세 가지를 완성했어요.'])+'<div class="label">내가 자랑하고 싶은 부분은?</div><div class="write small"></div>'
    B.append(block('new','💡 새로 만들기 · 선택',body,['아이디어 하나를 골라요.','만들 모습을 그리고 코드를 바꿔요.']))
    body='<p>'+w['challenge_story']+'</p><div class="draw"></div>'+gen.check(w['challenge_checks'])+'<div class="label">➕ 더 해 보기</div>'+gen.check(w['challenge_more'])
    B.append(block('challenge','🚀 도전 프로젝트 · '+w['challenge_name'],body,['extension_starter.py를 그대로 실행해요.','바꿀 모습을 먼저 그려요.','코드를 바꾸고 완성 기준을 체크해요.']))
    hints=[]
    for i,s in enumerate(w['steps'],1):hints.append((f'단계 {i}', '●○○','<p>'+s['hint']+'</p>'))
    hints += [('바꾸기·새로 만들기 1','●○○','<p>바꿀 위치나 값을 먼저 찾아요. 한 번에 하나만 바꿔 실행해요.</p>'),('바꾸기·새로 만들기 2','●●○','<p>'+w['hint_tool']+'</p>'),('바꾸기·새로 만들기 3','●●●','<p>'+w['hint_instruction']+'</p>'+c(w['hint_code'])),('도전 1','●○○','<p>시작 코드를 실행하고 어떤 숫자를 바꿀지 골라요.</p>'),('도전 2','●●○','<p>'+w['challenge_hint']+'</p>'),('도전 3','●●●','<p>'+w['challenge_instruction']+'</p>'+c(w['challenge_code']))]
    body='<div class="hints-grid">'+''.join(f'<div class="hint"><div class="hh"><span>{name}</span><span>{level}</span></div>{text}</div>' for name,level,text in hints)+'</div>'
    B.append(block('hints','🃏 힌트 카드',body,['막힌 활동의 힌트 1부터 읽어요.','부족하면 2, 3을 차례로 읽고 다시 해요.']))
    head=gen.HEAD.replace('<title>{{N}}주차 교안</title>',f'<title>2학기 {n}주차 · {w["title"]}</title>')
    head=head.replace('</style>','/* 주차별 추가: 힌트를 한 열로 읽어요. */\n.hints-grid {grid-template-columns:minmax(0,1fr);}\n.hint {min-width:0;}\n.result-preview {display:block;width:100%;max-height:260px;background:white;}\n@media print { body {font-size:10.5pt;} .block {gap:8px;padding:12px 16px;} .tool {padding:10px 14px;gap:5px;} .todo {padding:10px 14px;} pre.code {font-size:13px;line-height:1.5;} .block > h2 {font-size:1.3em;} .block.step {gap:6px;} .block.change {gap:6px;line-height:1.45;} }\n</style>')
    write(d/'lesson.html',head+'<body><main class="lesson">'+'\n'.join(B)+'</main></body></html>')
    md=[f'# 2학기 {n}주차 · {w["title"]}','', '> Codex 별도 제작본. lesson.html을 열어 활동하거나 인쇄해요.','', '## 🎯 오늘의 미션',w['story'],'','완성 모습:', '```',preview,'```','','## 🔧 워밍업','warmup.py에서 오류 세 개를 찾아 고쳐요. 줄 번호, 오류 이름, 고친 방법을 적어요.','']
    for i,s in enumerate(w['steps'],1):
        md += [f'## 🪜 단계 {i} · {s["name"]}','mini_starter.py의 해당 단계 아래에 이어 써요. 실행하고 달라진 모습을 적어요.','']
        for t in s['tool']:md += ['🧰 '+t[0]+': '+t[1],'```python']+t[2]+['```',t[3],'']
        md+=['```python']+s['lines']+['```','✅ '+s['ok'][0],'',s.get('note','')]
    if turtle:md+=['매번 맨 아래에 t.done()을 한 번 써요. 다음 단계 코드는 그 줄 위에 써요. 이전 그림 창은 닫고 다시 실행해요.','']
    md+=['🔍 따라가기: '+w['trace_q'],' / '.join(w['trace_heads']),'','## ⭐ 내 것으로 바꾸기','바꿀 부분과 계획을 적고 실행해요.','']+['- [ ] '+x for x in w['must']]+['','더 해 보기:']+['- '+x for x in w['more']]+['','친구에게 보여 주고 한마디를 받아요.','','## 💡 새로 만들기']+['- '+x for x in w['new']]
    if n==4:
        insert_at=md.index('## ⭐ 내 것으로 바꾸기')+1
        md[insert_at:insert_at]=['🧰 값 빼기와 마지막 값 꺼내기: '+w['hint_tool'],'```python','numbers = [10, 20, 30]','numbers.remove(20)','last = numbers.pop()','```','numbers는 [10], last는 30이에요.']
        trace_at=md.index('🔍 따라가기: '+w['trace_q'])
        trace_pair=md[trace_at:trace_at+2]
        del md[trace_at:trace_at+2]
        insert_at=md.index('numbers는 [10], last는 30이에요.')+1
        md[insert_at:insert_at]=trace_pair
    md.insert(md.index('## ⭐ 내 것으로 바꾸기')+1,w['change_guidance'])
    if n==4:md+=['','[높이, 이름] 기본 코드:','```python']+lines('''mountains = [[8849, "에베레스트"], [8516, "로체"], [8586, "칸첸중가"]]
mountains.sort()
for mountain in mountains:
    print(mountain[0], mountain[1])''')+['```']
    md+=['','## 🚀 도전 · '+w['challenge_name'],w['challenge_story'],'extension_starter.py를 실행하고 바꿔요.']+['- [ ] '+x for x in w['challenge_checks']]+['더 해 보기: '+x for x in w['challenge_more']]+['','## 🃏 힌트']
    for name,level,text in hints:md+=['<details>',f'<summary>{name} {level}</summary>','',text,'','</details>','']
    md+=['## ✅ 오늘의 마무리','- [ ] 오류 세 개를 고쳤어요.','- [ ] 단계를 실행하며 만들었어요.','- [ ] 꼭 하기 세 가지를 완성했어요.','내가 자랑하고 싶은 부분을 적어요.']
    write(d/'README.md','\n'.join(md)+'\n')
    a=[f'# 2학기 {n}주차 정답지 · {w["title"]}','','교사용. lesson.html의 블록 순서대로 정리했다.','','## 🎯 오늘의 미션','기본 완성 모습: '+preview,'','## 🔧 워밍업','| 줄 | 오류 이름 또는 메시지 | 고친 방법 |','|---|---|---|']+['| '+' | '.join(row)+' |' for row in w['fixes']]+['',w['warm_order'],'']
    for i,s in enumerate(w['steps'],1):a += [f'## 🪜 단계 {i} · {s["name"]}',s['ok'][0].replace('어요.','다.'), '실행해 확인함. 코드·예상 값의 검증 기록은 상위 VALIDATION.md에 있다.','']
    a+=['### 따라가기','| '+' | '.join(w['trace_heads'])+' |','| '+' | '.join(['---']*3)+' |','| '+' | '.join(w['trace_ans'])+' |','','## ⭐ 내 것으로 바꾸기','학생별 답이 다르다. 필수 세 가지를 충족하는 실행 가능한 예시는 mini_change_solution.py에 있다. 기존 코드 수정과 새 코드 추가를 구별한다. 필수 세 가지와 실제 변화가 일치하는지 확인한다. 더 해 보기는 필수가 아니다.','','## 💡 새로 만들기','그리기·계획·친구의 한마디·자랑할 점은 열린 답이다. 계획한 변화가 실행 결과에 나타나고 친구가 설명을 이해하는지 확인한다.','','## 🚀 도전 · '+w['challenge_name'],'extension_solution.py는 예시이며 유일한 정답이 아니다. '+w['challenge_hint'],'','## 🃏 힌트','힌트 코드는 해당 단계 완성 후, 그림 코드면 t.done() 앞에 넣는다. 방향·도구·코드 순서로 제공한다.']
    if n==4:a+=['','### 수치와 근거','처음 목록 합계 25951, 평균 정수 몫 8650. remove 후 [8516, 8849], pop 반환 8849, 남은 값 [8516]. 남은 개수 1, 최대·최소·합계·평균 8516.','이름과 높이 묶음 정렬 결과: 8516 로체 / 8586 칸첸중가 / 8849 에베레스트.','설문 가상 자료 [30, 90, 60, 120]: 개수 4, 합계 300, 최대 120, 최소 30, 평균 75분.','산 높이 근거: 네팔 정부 관광 통계(2022). 에베레스트 8848.86m는 8849m로 반올림했다. 로체 8516m, 칸첸중가 8586m.','https://www.tourism.gov.np/files/statistics/28.pdf']
    if n==4:
        trace_start=a.index('### 따라가기')
        change_start=a.index('## ⭐ 내 것으로 바꾸기')
        trace_rows=a[trace_start:change_start]
        del a[trace_start:change_start]
        at=a.index('## ⭐ 내 것으로 바꾸기')+1
        a[at:at]=trace_rows
    write(d/'answer_key.md','\n'.join(a)+'\n')
    guide=f'''# 2학기 {n}주차 교사 가이드

Codex 별도 제작본. 대상: 블록 코딩 경험이 있는 초등 5~6학년, 6명 미만.

## 110분 운영
| 활동 | 시간 |
|---|---:|
| 미션·워밍업 | 15분 |
| 단계별 따라 만들기 | 40분 |
| 쉬는 시간 | 10분 |
| 바꾸기·새로 만들기·친구에게 보여 주기 | 30분 |
| 도전·마무리 | 15분 |

## 준비
터틀은 Python의 tkinter와 그림 창을 표시할 수 있는 데스크톱 환경이 필요하다. 수업 전에 extension_starter.py로 확인한다. 웹 실행 환경에서는 터틀 지원 여부를 확인한다. 그림 창을 닫아 이전 실행을 끝낸 뒤 다시 실행한다.

## 진행과 설명
{w['teaching']}
{'학생이 t.done()을 맨 아래에 한 번 쓰게 하고, 다음 단계는 그 줄 위에 쓴다. 이 종료용 한 줄은 그림 창 유지 장치로 제공한다.' if turtle else '미니는 콘솔에서 자료를 정리하고 도전에서 이전 주 터틀과 연결한다.'}

## 바꾸기 확인
{w['change_guidance']}
교사용 mini_change_solution.py를 실행해 필수 세 가지를 충족하는 예시를 확인한다. 학생에게 완성 예시를 바로 주기보다 힌트부터 제공한다.

## 자주 생기는 문제
워밍업의 의도된 세 오류는 answer_key.md 순서로 고친다. for 줄의 콜론과 4칸 들여쓰기를 확인한다. 터틀이 멈춘 듯하면 그림 창이 열려 있는지 확인한다. 원치 않는 연결선은 penup() 누락 여부를 본다.
오류 문구는 Python 버전에 따라 다르다. 예를 들어 닫히지 않은 문자열은 EOL while scanning string literal 또는 unterminated string literal로 나올 수 있다. 메시지 전체 암기보다 오류 종류와 표시된 줄을 살핀다.

## 진도 차이
늦는 학생은 한 단계씩 실행하고 눈에 보이는 변화를 말하게 한다. 꼭 하기 세 가지를 먼저 완성한다. 빠른 학생만 새로 만들기나 도전으로 넘어간다. 도전 예시는 교사용이며 학생에게 바로 전체 정답을 주지 않는다.

## 평가·정리
필수 세 가지를 실제 실행으로 확인한다. 예측 표는 answer_key.md와 대조한다. 색·주제 선택에는 정답을 정하지 않는다. 마지막에는 바꾼 점 하나와 아직 궁금한 점 하나를 말하게 한다.
'''
    write(d/'teacher_guide.md',guide)

# Provenance and isolation record live only inside this new directory.
write(OUT/'README.md','''# Codex 제작 · 2학기 1~4주차

2026-11-04 사용자 요청으로 만든 별도 제작본이다. 원본 docs와 1학기 폴더·도구·진행 기록은 수정하지 않는다. 검토 후 이 폴더만 커밋·푸시하도록 사용자에게 요청받았다.

원본 기준은 초안 상태다. 이번 요청 범위만 별도로 제작했으며 기준 상태를 확정으로 바꾸지 않았다. 1주차 샘플과 2~4주차를 함께 검토할 수 있도록 제공한다.

| 주차 | 미니 | 도전 | 교안 |
|---|---|---|---|
| 1 | 기분 이모지 | 국기 그리기 챌린지 | [열기](worksheets/semester2/week01/lesson.html) |
| 2 | 바람개비 | 스피로그래프 만다라 | [열기](worksheets/semester2/week02/lesson.html) |
| 3 | 롤리팝 가게 | 제너러티브 아트 배경화면 | [열기](worksheets/semester2/week03/lesson.html) |
| 4 | 세계의 산 높이 정렬 | 우리 반 설문 막대그래프 | [열기](worksheets/semester2/week04/lesson.html) |

각 주차: lesson.html, README.md, lesson_spec.py, warmup.py, mini_starter.py, mini_solution.py, mini_change_solution.py, extension_starter.py, extension_solution.py, answer_key.md, teacher_guide.md.

lesson.html을 브라우저에서 열면 교안, 인쇄하면 학습지다. A4·배경 그래픽 켜기·머리글/바닥글 끄기를 권한다. 실습은 그림 창을 지원하는 데스크톱 Python에서 진행한다.

터틀 주차는 각 단계 실행 때 마지막에 t.done()을 한 번 둔다. 다음 단계는 그 줄 위에 이어 쓴다. 원래 템플릿의 스타일을 유지했고 힌트 한 열·인쇄 여백을 별도 스타일로 조정했다. 완성 그림은 실제 미니 코드의 이동 명령으로 생성한 정적 인라인 SVG이며 앱 화면 캡처는 아니다. 외부 그림 파일이나 웹 스크립트를 사용하지 않는다.

제작 근거: 원본 docs의 curriculum, 01~05 기준, decisions, lesson-template 및 1학기 설계 파일. 내용 수정은 각 주차 lesson_spec.py에서 하고 저장소 루트에서 `python codex-created-semester2/build.py`를 실행한다. 생성기는 설계 파일을 덮어쓰지 않는다. mini_change_solution.py는 교사용 바꾸기 완성 예시다. 원본 도구와 별도로 둔 생성기를 사용한다. 검증 범위와 결과는 VALIDATION.md에 기록한다.

교육 콘텐츠 검토 결과는 REVIEW.md에 있다. 내용 검사는 저장소 루트에서 `python codex-created-semester2/check_content.py`로 다시 실행한다. 학생과의 실제 수업 검증은 아직 수행하지 않았다.
''')
write(OUT/'PROGRESS.md','# Codex 별도 제작 기록\n\n'+ '\n'.join(f'- [x] 2학기 {w["week"]}주차: {w["title"]} / {w["challenge_name"]} (2026-11-04)' for w in weeks)+'\n\n검증 결과는 VALIDATION.md 참고. 원본 PROGRESS.md는 수정하지 않았다.\n')
print(OUT)
