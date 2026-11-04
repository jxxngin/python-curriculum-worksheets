# -*- coding: utf-8 -*-
# 주차 내용의 원본. 상위 build.py로 생성한다.
SPEC = {'week': 2,
 'title': '바람개비',
 'badge': '같은 모양 반복하기',
 'story': '바람이 없어도 멋진 바람개비를 그릴 수 있어요. 삼각 날개를 그리고 방향을 바꾸어 네 날개를 완성해요.',
 'steps': [{'name': '첫 삼각 날개 그리기',
            'lines': ['import turtle as t',
                      't.color("teal")',
                      'for side in range(3):',
                      '    t.forward(90)',
                      '    t.left(120)'],
            'tool': [('같은 일을 여러 번',
                      'for 아래 들여쓴 줄을 range()에 적은 횟수만큼 반복해요.',
                      ['for turn in range(2):', '    print("빙글")'],
                      '빙글이 두 번 나와요. 정삼각형은 한 바퀴 360도를 3으로 나눈 120도씩 돌아요.')],
            'ok': ['삼각형 하나를 그렸어요.'],
            'hint': 'for 줄 끝의 :와 아래 두 줄의 4칸 들여쓰기를 확인해요. range(3)은 변 세 개예요.'},
           {'name': '두 번째 날개 더하기',
            'lines': ['# 단계 1 코드 아래에 이어서 써요.',
                      't.left(90)',
                      'for side in range(3):',
                      '    t.forward(90)',
                      '    t.left(120)'],
            'tool': [('날개 사이의 각도',
                      '네 방향으로 벌어지려면 360 ÷ 4만큼 돌아요.',
                      ['t.left(45)', 't.forward(20)'],
                      '보던 방향에서 왼쪽으로 45도 돌아 20 움직여요.')],
            'ok': ['첫 날개에서 90도 돌아 두 번째 날개가 생겼어요.'],
            'hint': '삼각형을 그린 뒤 left(90)을 한 번 쓰고 같은 삼각형 반복을 이어 써요.'},
           {'name': '세 번째 날개 더하기',
            'lines': ['# 단계 2 코드 아래에 이어서 써요.',
                      't.left(90)',
                      'for side in range(3):',
                      '    t.forward(90)',
                      '    t.left(120)'],
            'tool': [],
            'ok': ['세 번째 방향에 날개가 생겼어요.'],
            'hint': '세 번째 날개도 새 삼각형을 그리기 전에 left(90)으로 방향을 바꿔요.'},
           {'name': '네 번째 날개 완성하기',
            'lines': ['# 단계 3 코드 아래에 이어서 써요.',
                      't.left(90)',
                      'for side in range(3):',
                      '    t.forward(90)',
                      '    t.left(120)'],
            'tool': [],
            'ok': ['네 방향으로 날개가 펼쳐졌어요.'],
            'hint': '네 번째 날개는 앞의 삼각형 반복을 다시 써요. 삼각형 안의 120도는 그대로 둬요.'}],
 'warm': 'import turtle as t\n'
         'for side in range(3)\n'
         '    t.forward(60)\n'
         '    t.Left(120)\n'
         't.forward("20")',
 'fixes': [('6', "SyntaxError: expected ':'", 'for 줄 끝에 :를 붙인다.'),
           ('8', "AttributeError: module 'turtle' has no attribute 'Left'", 'Left → left'),
           ('9', 'TypeError', '"20" → 20')],
 'warm_order': '6 → 8 → 9번 줄 순서다. 마지막 오류는 거리로 글자를 넘겨 생긴다. 고치면 삼각형 뒤에 길이 20인 선을 그린다.',
 'trace_q': '단계 1의 range(3)을 따라가요. side는 0부터 시작해요.',
 'trace_heads': ['side 차례', 'forward 횟수', 'left로 돈 각도 합'],
 'trace_ans': ['0, 1, 2', '3', '360도'],
 'must': ['날개 길이를 바꿨어요.', '날개마다 색을 다르게 바꿨어요.', '네 날개 사이에서 90도씩 도는 이유를 설명하고 완성했어요.'],
 'more': ['막대를 더해요.', '360 ÷ 날개 수로 각도를 계산해 여섯 날개로 바꿔요.'],
 'change_example': ['t.pencolor("orange")'],
 'new': ['세 날개 바람개비', '네모 날개 바람개비'],
 'challenge_name': '스피로그래프 만다라',
 'challenge_story': '원을 조금씩 돌려 겹치면 꽃 같은 무늬가 생겨요. 원의 수와 회전 각도를 함께 바꿔 나만의 무늬를 만들어요.',
 'challenge_checks': ['원의 수와 회전 각도를 바꿨어요.', '반지름을 바꿔 무늬 크기를 조절했어요.', '한 바퀴를 채우는 각도를 설명했어요.'],
 'challenge_more': ['같은 반복을 한 번 더 써서 안쪽 무늬를 더해요.'],
 'extension': 'import turtle as t\n'
              't.speed(0)\n'
              't.color("purple")\n'
              'for turn in range(12):\n'
              '    t.circle(65)\n'
              '    t.left(30)\n'
              't.done()',
 'extension_solution': 'import turtle as t\n'
                       't.speed(0)\n'
                       't.color("darkblue")\n'
                       'for turn in range(18):\n'
                       '    t.circle(55)\n'
                       '    t.left(20)\n'
                       't.color("orange")\n'
                       'for turn in range(12):\n'
                       '    t.circle(30)\n'
                       '    t.left(30)\n'
                       't.done()',
 'hint_tool': '삼각형 안에서는 left(120), 날개 사이에서는 left(90)을 써요.',
 'hint_code': 't.pencolor("orange")\n'
              'for side in range(3):\n'
              '    t.forward(70)\n'
              '    t.left(120)',
 'challenge_hint': '원의 수 × 돌리는 각도가 360이 되도록 골라요.',
 'challenge_code': 'for turn in range(18):\n    t.circle(55)\n    t.left(20)',
 'teaching': '삼각형의 안쪽 각 60도와 거북이가 도는 바깥각 120도를 구분한다. 중첩 반복은 다음 주이므로 이번 주에는 삼각형 반복을 나란히 쓴다.',
 'change_guidance': '네 곳의 forward(90)을 같은 길이로 바꿔요. 각 날개의 for 바로 위에서 pencolor()로 다른 색을 정해요. '
                    '삼각형 안의 회전은 120도, 날개 사이는 90도예요.',
 'change_solution': 'import turtle as t\n'
                    't.color("teal")\n'
                    't.pencolor("teal")\n'
                    'for side in range(3):\n'
                    '    t.forward(70)\n'
                    '    t.left(120)\n'
                    '# 단계 1 코드 아래에 이어서 써요.\n'
                    't.left(90)\n'
                    't.pencolor("orange")\n'
                    'for side in range(3):\n'
                    '    t.forward(70)\n'
                    '    t.left(120)\n'
                    '# 단계 2 코드 아래에 이어서 써요.\n'
                    't.left(90)\n'
                    't.pencolor("purple")\n'
                    'for side in range(3):\n'
                    '    t.forward(70)\n'
                    '    t.left(120)\n'
                    '# 단계 3 코드 아래에 이어서 써요.\n'
                    't.left(90)\n'
                    't.pencolor("red")\n'
                    'for side in range(3):\n'
                    '    t.forward(70)\n'
                    '    t.left(120)\n'
                    't.done()',
 'hint_instruction': '기존 첫 번째 날개 부분을 아래처럼 바꿔요. 다른 날개도 길이와 색을 각각 고쳐요.',
 'challenge_instruction': '기존 도전 반복문 세 줄을 아래로 바꿔요.',
 'plan_example': ['예) 네 날개의 길이', '90을 모두 70으로 바꾸기']}
