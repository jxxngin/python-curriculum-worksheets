# -*- coding: utf-8 -*-
# 주차 내용의 원본. 상위 build.py로 생성한다.
SPEC = {'week': 1,
 'title': '기분 이모지',
 'badge': '펜으로 마음 그리기',
 'story': '오늘 내 마음은 어떤 얼굴인가요? 둥근 얼굴에 눈과 입을 더해 나만의 기분 이모지를 만들어요.',
 'steps': [{'name': '얼굴 바탕 그리기',
            'lines': ['import turtle as t',
                      't.color("gold")',
                      't.begin_fill()',
                      't.circle(80)',
                      't.end_fill()',
                      't.penup()'],
            'tool': [('그림 펜과 채우기',
                      '선을 닫으면 그 안을 색으로 채울 수 있어요.',
                      ['import turtle as t', 't.color("skyblue")', 't.circle(30)'],
                      '하늘색 원을 그려요. begin_fill()과 end_fill() 사이에 닫힌 도형을 그리면 속도 채워요.')],
            'ok': ['노란 얼굴 바탕이 나왔어요.'],
            'note': 'begin_fill() 뒤에 원을 그리고 end_fill()로 채워요. penup()은 펜을 들어 이동선을 남기지 않아요.',
            'hint': '채우기 시작과 끝 사이에 circle(80)이 있는지 확인해요. 얼굴을 다 그린 뒤 펜을 들어요.'},
           {'name': '눈 두 개 찍기',
            'lines': ['# 단계 1 코드 아래에 이어서 써요.',
                      't.goto(-30, 100)',
                      't.dot(14, "black")',
                      't.goto(30, 100)',
                      't.dot(14, "black")'],
            'tool': [('좌표로 이동하기',
                      '가운데는 (0, 0), 오른쪽은 x가 커지고 위쪽은 y가 커져요.',
                      ['t.penup()', 't.goto(40, 60)', 't.dot(10, "blue")'],
                      '선을 남기지 않고 오른쪽 위에 파란 점을 찍어요.')],
            'ok': ['같은 높이에 검은 눈이 두 개 나왔어요.'],
            'note': 'dot(크기, 색)은 현재 위치에 점을 찍어요. 두 눈의 y가 같으면 나란히 놓여요.',
            'hint': '두 goto의 x는 서로 반대 부호, y는 100으로 같아요. goto 다음 줄에 dot을 써요.'},
           {'name': '웃는 입 그리기',
            'lines': ['# 단계 2 코드 아래에 이어서 써요.',
                      't.goto(-35, 65)',
                      't.setheading(-90)',
                      't.pencolor("black")',
                      't.pendown()',
                      't.circle(35, 180)',
                      't.penup()'],
            'tool': [('방향과 둥근 선',
                      '0도는 오른쪽, 90도는 위쪽이에요. circle(반지름, 각도)는 원의 일부를 그려요.',
                      ['t.setheading(0)', 't.forward(25)', 't.left(90)'],
                      '오른쪽으로 25 움직인 뒤 위를 봐요. backward()는 뒤로, right()는 오른쪽으로 돌아요.')],
            'ok': ['양 끝이 올라간 웃는 입이 생겼어요.'],
            'note': 'pencolor()는 선 색, pendown()은 펜 내리기예요. setheading(-90)은 아래쪽을 보게 해요.',
            'hint': '입에 선이 없으면 pendown()을 확인해요. 아래쪽을 본 뒤 반지름 35인 반원을 그려요.'}],
 'warm': 'name = "하린"\nscore = "10"\nprint(nam)\nprint(score + 5)\nprint("이모지 준비 완료)',
 'fixes': [('7', "NameError: name 'nam' is not defined", 'nam → name'),
           ('8',
            'TypeError: can only concatenate str (not "int") to str',
            'score = 10으로 바꾼다.'),
           ('9', 'SyntaxError: unterminated string literal', '닫는 큰따옴표를 추가한다.')],
 'warm_order': '9번 줄의 SyntaxError → 7번 줄의 NameError → 8번 줄의 TypeError. 고친 출력: 하린 / 15 / 이모지 '
               '준비 완료.',
 'trace_q': '단계 2의 두 goto를 순서대로 따라가요.',
 'trace_heads': ['첫 눈의 x, y', '둘째 눈의 x, y', '눈 사이 거리'],
 'trace_ans': ['-30, 100', '30, 100', '60'],
 'must': ['얼굴 색을 내 기분에 맞게 바꿨어요.', '눈의 크기나 위치를 바꿨어요.', '입 모양을 바꾸고 어떤 기분인지 친구에게 설명했어요.'],
 'more': ['볼에 점을 찍어 꾸며요.', '눈썹을 더해요.'],
 'change_example': ['t.goto(-50, 75)', 't.dot(16, "pink")'],
 'new': ['졸린 얼굴', '깜짝 놀란 얼굴'],
 'challenge_name': '국기 그리기 챌린지',
 'challenge_story': '국기를 관찰하고 색과 도형으로 나누어 봐요. 시작 파일의 일본 국기를 바꿔 스위스 국기에 도전해요. 공식 규격 재현보다 도형 배치 '
                    '연습에 집중해요.',
 'challenge_checks': ['배경과 중심 도형의 색을 구분했어요.',
                      '선을 남기지 않고 도형 사이를 이동했어요.',
                      '색을 채우는 시작과 끝을 짝지었어요.'],
 'challenge_more': ['태극기나 영국 국기는 교사와 도형을 나눠 설계해요.'],
 'extension': 'import turtle as t\n'
              't.bgcolor("white")\n'
              't.penup()\n'
              't.goto(0, -55)\n'
              't.color("red")\n'
              't.pendown()\n'
              't.begin_fill()\n'
              't.circle(55)\n'
              't.end_fill()\n'
              't.done()',
 'extension_solution': 'import turtle as t\n'
                       't.bgcolor("red")\n'
                       't.color("white")\n'
                       't.pensize(35)\n'
                       't.penup()\n'
                       't.goto(-65, 0)\n'
                       't.pendown()\n'
                       't.goto(65, 0)\n'
                       't.penup()\n'
                       't.goto(0, -65)\n'
                       't.pendown()\n'
                       't.goto(0, 65)\n'
                       't.done()',
 'hint_tool': '얼굴 색은 color(), 눈은 dot(크기, 색), 입 모양은 circle(반지름, 각도)의 숫자를 고쳐요.',
 'hint_code': 't.goto(-35, 65)\n'
              't.setheading(-90)\n'
              't.pencolor("black")\n'
              't.pendown()\n'
              't.circle(35, 120)\n'
              't.penup()',
 'challenge_hint': '흰 십자가는 굵은 가로선과 세로선으로 나눌 수 있어요.',
 'challenge_code': 't.pencolor("white")\nt.pensize(35)\nt.goto(65, 0)',
 'teaching': '얼굴 원의 중심은 (0, 80)이다. circle(80)은 현재 위치를 원의 아래쪽 점으로 삼는다. 이동 중 선이 생기면 penup 여부를 '
             '확인한다. 채우기 시작·끝을 한 쌍으로 묶는다.',
 'change_guidance': '기존 코드의 얼굴 색, 눈의 크기·위치, 입의 각도를 고쳐요. 예를 들어 circle(35, 180)을 circle(35, '
                    '120)으로 바꾸면 입 모양이 달라져요. 새 코드를 덧붙이기보다 해당 줄을 바꿔요.',
 'change_solution': 'import turtle as t\n'
                    't.color("skyblue")\n'
                    't.begin_fill()\n'
                    't.circle(80)\n'
                    't.end_fill()\n'
                    't.penup()\n'
                    '# 단계 1 코드 아래에 이어서 써요.\n'
                    't.goto(-30, 100)\n'
                    't.dot(18, "black")\n'
                    't.goto(30, 100)\n'
                    't.dot(18, "black")\n'
                    '# 단계 2 코드 아래에 이어서 써요.\n'
                    't.goto(-35, 65)\n'
                    't.setheading(-90)\n'
                    't.pencolor("black")\n'
                    't.pendown()\n'
                    't.circle(35, 120)\n'
                    't.penup()\n'
                    't.done()',
 'hint_instruction': '기존 단계 3의 여섯 줄을 아래로 바꿔요.',
 'challenge_instruction': '도전 시작 코드의 원 그리기 부분을 지우고 십자가 선으로 바꿔요. 먼저 penup()과 goto(-65, 0), '
                          'pendown()으로 가로선 시작점으로 가요.',
 'plan_example': ['예) 얼굴 색', 'skyblue로 바꾸기']}
