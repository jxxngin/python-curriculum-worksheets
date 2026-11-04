# -*- coding: utf-8 -*-
# 주차 내용의 원본. 상위 build.py로 생성한다.
SPEC = {'week': 3,
 'title': '롤리팝 가게',
 'badge': '반복 속에서 모양 바꾸기',
 'story': '막대사탕 가게에 크기가 다른 사탕을 진열해요. 반복 속 숫자를 이용해 위치와 크기를 바꾸고 무늬도 넣어요.',
 'steps': [{'name': '사탕 세 개 놓기',
            'lines': ['import turtle as t',
                      't.penup()',
                      'for number in range(3):',
                      '    t.goto(-150 + number * 150, 40)',
                      '    t.dot(60, "pink")'],
            'tool': [('반복할 때 바뀌는 숫자',
                      'range(3)의 숫자는 0, 1, 2가 돼요. 위치 계산에 써요.',
                      ['for number in range(3):', '    print(number * 10)'],
                      '0, 10, 20이 차례로 나와요.')],
            'ok': ['가로로 사탕 세 개가 나왔어요.'],
            'hint': 'number가 0, 1, 2일 때 -150 + number * 150을 계산해요. 세 x는 -150, 0, 150이에요.'},
           {'name': '막대와 다른 크기 더하기',
            'lines': ['# 단계 1 코드 아래에 이어서 써요.',
                      'for number in range(3):',
                      '    t.goto(-150 + number * 150, 40)',
                      '    t.dot(60 + number * 20, "hotpink")',
                      '    t.pendown()',
                      '    t.goto(-150 + number * 150, -100)',
                      '    t.penup()'],
            'tool': [('반복 속에서 크기 바꾸기',
                      '반복 숫자에 20씩 곱해서 차이를 만들어요.',
                      ['for number in range(3):', '    print(40 + number * 20)'],
                      '40, 60, 80이 나와요.')],
            'ok': ['세 사탕의 크기가 다르고 아래로 막대가 생겼어요.'],
            'hint': '크기는 60 + number * 20, 막대 끝의 y는 -100이에요. 다음 사탕으로 가기 전에 penup()을 써요.'},
           {'name': '사탕마다 작은 장식 세 개 찍기',
            'lines': ['# 단계 2 코드 아래에 이어서 써요.',
                      'for number in range(3):',
                      '    for spot in range(3):',
                      '        t.goto(-165 + number * 150 + spot * 15, 40)',
                      '        t.dot(8, "white")'],
            'tool': [('반복 안에 반복',
                      '사탕 하나마다 장식을 세 번 찍어요. 안쪽은 8칸 들여써요.',
                      ['for row in range(2):',
                       '    for col in range(3):',
                       '        print("*", end="")',
                       '    print()'],
                      '별 3개짜리 줄이 2줄 나와요. end=""는 줄바꿈을 미뤄요.')],
            'ok': ['사탕마다 흰 장식이 세 개씩 나왔어요.'],
            'hint': '안쪽 for와 그 안의 goto·dot 들여쓰기를 비교해요. 사탕 하나마다 spot이 다시 0부터 시작해요.'}],
 'warm': 'for row in range(2)\n'
         '    for col in range(3):\n'
         '    print("*", end="")\n'
         '    print("줄 끝")',
 'fixes': [('5', "SyntaxError: expected ':'", 'for 줄 끝에 :를 붙인다.'),
           ('7', 'IndentationError: expected an indented block', 'print를 8칸 들여쓴다.'),
           ('8', '메시지 없는 오류', 'print("줄 끝") → print()')],
 'warm_order': '5 → 7번 줄 순서로 문법 오류를 고친다. 그 뒤 8번 줄을 고치면 ***가 두 줄 나온다.',
 'trace_q': '단계 3에서 number=1인 사탕만 따라가요.',
 'trace_heads': ['spot 차례', 'x 좌표 차례', '이 사탕의 점 개수'],
 'trace_ans': ['0, 1, 2', '-15, 0, 15', '3'],
 'must': ['사탕 색을 내 가게 색으로 바꿨어요.', '사탕 크기가 반복 숫자에 따라 달라져요.', '중첩 반복으로 사탕마다 장식을 두 개 이상 넣었어요.'],
 'more': ['사탕 수와 간격을 함께 바꿔요.', '장식을 다른 높이에도 찍어요.'],
 'change_example': ['# 단계 1과 2의 사탕 색을 skyblue로 바꿔요.'],
 'new': ['초콜릿 가게', '두 줄 사탕 진열대'],
 'challenge_name': '제너러티브 아트 배경화면',
 'challenge_story': '줄과 칸은 규칙적으로 놓고, 원의 크기는 무작위로 정해요. 질서와 우연이 섞인 배경을 만들어요.',
 'challenge_checks': ['줄 수나 칸 수를 바꿨어요.', '좌표 간격을 바꿨어요.', '무작위 크기 범위를 바꾸고 여러 번 실행했어요.'],
 'challenge_more': ['random.choice()로 색도 골라요.'],
 'extension': 'import turtle as t\n'
              'import random\n'
              't.speed(0)\n'
              't.penup()\n'
              'for row in range(4):\n'
              '    for col in range(5):\n'
              '        t.goto(-160 + col * 80, -120 + row * 80)\n'
              '        size = random.randint(10, 50)\n'
              '        t.dot(size, "teal")\n'
              't.done()',
 'extension_solution': 'import turtle as t\n'
                       'import random\n'
                       't.speed(0)\n'
                       't.penup()\n'
                       'colors = ["teal", "gold", "coral"]\n'
                       'for row in range(5):\n'
                       '    for col in range(6):\n'
                       '        t.goto(-175 + col * 70, -140 + row * 70)\n'
                       '        size = random.randint(12, 45)\n'
                       '        t.dot(size, random.choice(colors))\n'
                       't.done()',
 'hint_tool': '바깥 number는 사탕 위치, 안쪽 spot은 장식 위치에 써요.',
 'hint_code': 'for number in range(3):\n'
              '    for spot in range(3):\n'
              '        t.goto(-165 + number * 150 + spot * 15, 55)\n'
              '        t.dot(8, "white")',
 'challenge_hint': 'row는 y 좌표에, col은 x 좌표에 써요. 크기는 size라는 상자에 뽑아 담아요.',
 'challenge_code': 'size = random.randint(12, 45)\nt.dot(size, "coral")',
 'teaching': '바깥 반복 한 번마다 안쪽 반복이 처음부터 끝까지 돈다. 단계 3의 점은 총 9개다. 8칸 들여쓰기를 점검한다. 앞의 사탕을 더 큰 진분홍 '
             '점으로 덮는 의도를 설명한다.',
 'change_guidance': '단계 1·2의 분홍색 이름을 모두 내 색으로 바꿔요. 같은 자리에서 더 큰 점을 덮는 방식이에요. 60 + number * 20의 '
                    '숫자와 단계 3의 장식 반복을 바꿔요.',
 'change_solution': 'import turtle as t\n'
                    't.penup()\n'
                    'for number in range(3):\n'
                    '    t.goto(-150 + number * 150, 40)\n'
                    '    t.dot(60, "skyblue")\n'
                    '# 단계 1 코드 아래에 이어서 써요.\n'
                    'for number in range(3):\n'
                    '    t.goto(-150 + number * 150, 40)\n'
                    '    t.dot(70 + number * 15, "skyblue")\n'
                    '    t.pendown()\n'
                    '    t.goto(-150 + number * 150, -100)\n'
                    '    t.penup()\n'
                    '# 단계 2 코드 아래에 이어서 써요.\n'
                    'for number in range(3):\n'
                    '    for spot in range(2):\n'
                    '        t.goto(-165 + number * 150 + spot * 15, 40)\n'
                    '        t.dot(8, "white")\n'
                    't.done()',
 'hint_instruction': '단계 3 아래, t.done() 바로 위에 넣어요.',
 'challenge_instruction': '도전 반복문 안의 size와 dot 두 줄을 아래로 바꿔요. 들여쓰기는 원래처럼 8칸으로 맞춰요.',
 'plan_example': ['예) 사탕 크기', '70 + number * 15로 바꾸기']}
