"""python codex-created-semester2/check_content.py

터틀 창을 열지 않고 교육 자료의 값·학습 흐름·재생성을 검증한다.
실제 그림 창과 브라우저 인쇄 검수는 별도로 수행한다.
"""
import ast
import contextlib
import hashlib
import html
import importlib.util
import io
import os
from pathlib import Path
import pprint
import random
import runpy
import shutil
import subprocess
import sys
import tempfile
from preview import Pen

ROOT=Path(__file__).resolve().parent
REPO=Path(os.environ.get('CURRICULUM_REPO',str(ROOT.parent)))

def run(src):
    pen=Pen();previous=sys.modules.get('turtle');sys.modules['turtle']=pen
    output=io.StringIO();ns={}
    try:
        with contextlib.redirect_stdout(output):exec(compile(src,'practice.py','exec'),ns)
    finally:
        if previous is None:del sys.modules['turtle']
        else:sys.modules['turtle']=previous
    return pen,output.getvalue(),ns

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()

for d in sorted(ROOT.glob('worksheets/semester2/week*')):
    w=runpy.run_path(str(d/'lesson_spec.py'))['SPEC'];n=w['week']
    lesson=(d/'lesson.html').read_text(encoding='utf-8')
    markdown=(d/'README.md').read_text(encoding='utf-8')
    assert len(w['must'])<=3
    assert not ast.parse((d/'mini_starter.py').read_text(encoding='utf-8')).body
    for p in d.glob('*.py'):
        if p.name!='warmup.py':compile(p.read_text(encoding='utf-8'),str(p),'exec')
    prefix=[]
    for step in w['steps']:
        assert 3<=len([s for s in step['lines'] if not s.startswith('#')])<=6
        prefix+=step['lines'];run('\n'.join(prefix))
        for line in step['lines']:
            assert html.escape(line,quote=False) in lesson
            assert line in markdown
    for name in ('mini_solution.py','mini_change_solution.py','extension_starter.py','extension_solution.py'):
        for seed in range(3):
            random.seed(seed);run((d/name).read_text(encoding='utf-8'))
    warm=(d/'warmup.py').read_text(encoding='utf-8')
    repairs={
        1:[(SyntaxError,'print("이모지 준비 완료)','print("이모지 준비 완료")'),(NameError,'print(nam)','print(name)'),(TypeError,'score = "10"','score = 10')],
        2:[(SyntaxError,'range(3)\n','range(3):\n'),(AttributeError,'t.Left','t.left'),(TypeError,'t.forward("20")','t.forward(20)')],
        3:[(SyntaxError,'range(2)\n','range(2):\n'),(IndentationError,'    print("*"','        print("*"'),(None,'print("줄 끝")','print()')],
        4:[(IndexError,'heights[3]','heights[2]'),(AttributeError,'.apend(','.append('),(TypeError,'print("산 개수: " + len(heights))','print(f"산 개수: {len(heights)}")')]
    }
    for error,before,after in repairs[n]:
        if error:
            try:run(warm)
            except error:pass
            else:raise AssertionError('의도한 워밍업 오류가 나타나지 않았다.')
        warm=warm.replace(before,after)
    _,warm_output,_=run(warm)
    expected={1:'하린\n15\n이모지 준비 완료\n',2:'',3:'***\n***\n',4:'8586\n산 개수: 4\n'}
    assert warm_output==expected[n]
    p,output,ns=run((d/'mini_solution.py').read_text(encoding='utf-8'))
    if n<4:assert '<svg ' in lesson and '<script' not in lesson
    if n==1:
        assert p.dots==[(-30,100,14,'black'),(30,100,14,'black')]
        assert p.circles==[(80,360),(35,180)]
        changed,_,_=run(w['change_solution'])
        assert changed.circles[-1]==(35,120) and changed.dots[0][2]==18
    elif n==2:
        assert len(p.moves)==12 and abs(p.x)<1e-7 and abs(p.y)<1e-7
        changed,_,_=run(w['change_solution'])
        assert len(set(changed.colors))==4 and len(changed.moves)==12
    elif n==3:
        assert len([dot for dot in p.dots if dot[3]=='white'])==9
        changed,_,_=run(w['change_solution'])
        assert len([dot for dot in changed.dots if dot[3]=='white'])==6
    else:
        assert ns['heights']==[8516,8586,8849] and ns['total']==25951
        assert '8650m' in output
        _,_,changed=run(w['change_solution']);assert changed['heights']==[8516] and changed['removed']==8849
        assert lesson.index('도구 카드 · 값 빼기')<lesson.index('🔍 따라가기:')
        for values in ([0],[0,0,0],[30,90,60,120],[1440,1000,0],[1,2,3,4,5,6],[],[-1,5]):
            src=w['extension_solution'].replace('minutes = [30, 90, 60, 120]','minutes = '+repr(values))
            graph,text,_=run(src)
            if not values or min(values)<0:
                assert '0 이상의 시간' in text and not graph.moves
            else:
                assert len(graph.dots)==len(values)
                assert all(-150-1e-7<=x<=150+1e-7 and -140<=y<=140 for x,y in graph.moves)
                assert f'응답 수: {len(values)}' in text
    print(f'PASS week{n:02d}: 단계, 문법, 코드 일치, 기본·바꾸기·도전 결과')

# Source edits must survive generation and appear in the generated lesson.
with tempfile.TemporaryDirectory(prefix='curriculum-review-') as tmp:
    copy=Path(tmp)/'materials';shutil.copytree(ROOT,copy,ignore=shutil.ignore_patterns('__pycache__'))
    paths=sorted(copy.glob('worksheets/semester2/week*/lesson_spec.py'))
    before={p:digest(p) for p in paths}
    env=dict(os.environ,CURRICULUM_REPO=str(REPO))
    subprocess.run([sys.executable,str(copy/'build.py')],check=True,env=env,stdout=subprocess.DEVNULL)
    assert before=={p:digest(p) for p in paths}
    generated=[p for p in copy.rglob('*') if p.is_file() and '__pycache__' not in str(p)]
    first={p:digest(p) for p in generated}
    subprocess.run([sys.executable,str(copy/'build.py')],check=True,env=env,stdout=subprocess.DEVNULL)
    assert first=={p:digest(p) for p in generated}
    w=runpy.run_path(str(paths[0]))['SPEC'];w['title']='재생성 검증 제목'
    paths[0].write_text('SPEC = '+pprint.pformat(w,sort_dicts=False),encoding='utf-8')
    subprocess.run([sys.executable,str(copy/'build.py')],check=True,env=env,stdout=subprocess.DEVNULL)
    assert '재생성 검증 제목' in paths[0].with_name('lesson.html').read_text(encoding='utf-8')
print('PASS regeneration: 원본 보존·반복 결과 동일·설계 수정 반영')

sp=importlib.util.spec_from_file_location('checker',REPO/'tools/check_worksheet.py')
checker=importlib.util.module_from_spec(sp);sp.loader.exec_module(checker)
checker.playwright=lambda:None
for file in ROOT.rglob('lesson.html'):
    with contextlib.redirect_stdout(io.StringIO()):errors=checker.check(file)
    assert not errors,(str(file),errors)
print('PASS original checker: 블록 순서·공통 스타일·외부 리소스·편집기 중립')
