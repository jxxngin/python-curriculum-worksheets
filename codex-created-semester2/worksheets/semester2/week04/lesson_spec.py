# -*- coding: utf-8 -*-
# 주차 내용의 원본. 상위 build.py로 생성한다.
SPEC = {'week': 4,
 'title': '세계의 산 높이 정렬',
 'badge': '목록을 정리하고 비교하기',
 'story': '산 높이 탐험대의 기록이 뒤섞였어요. 낮은 산부터 줄을 세우고 가장 높은 값과 평균도 찾아요. 이번 주 미니는 글자 기록표, 도전은 터틀 '
          '그래프예요.',
 'steps': [{'name': '산 높이를 하나씩 보여 주기',
            'lines': ['heights = [8849, 8516, 8586]',
                      'print("산 높이(m)")',
                      'for height in heights:',
                      '    print(height)'],
            'tool': [('목록의 값을 하나씩',
                      'for 뒤에 목록을 쓰면 안의 값을 차례로 꺼내요.',
                      ['scores = [3, 7]', 'for score in scores:', '    print(score)'],
                      '3과 7이 차례로 나와요.')],
            'ok': ['입력한 순서대로 높이 세 개가 나왔어요.'],
            'hint': 'for height in heights: 아래 print(height)를 4칸 들여써요.'},
           {'name': '낮은 순서로 정렬하기',
            'lines': ['# 단계 1 코드 아래에 이어서 써요.',
                      'heights.sort()',
                      'print("낮은 산부터")',
                      'for height in heights:',
                      '    print(height)'],
            'tool': [('작은 값부터 정리하기',
                      'sort()는 원래 목록의 순서를 바꿔요.',
                      ['scores = [8, 2, 5]', 'scores.sort()', 'print(scores)'],
                      '[2, 5, 8]. sort() 결과를 다른 변수에 담지 않아요.')],
            'ok': ['8516, 8586, 8849 순서로 나왔어요.'],
            'hint': 'heights.sort()를 따로 실행한 뒤 for로 정리된 목록을 보여 줘요.'},
           {'name': '탐험대 요약표 만들기',
            'lines': ['# 단계 2 코드 아래에 이어서 써요.',
                      'print(f"산 개수: {len(heights)}")',
                      'print(f"가장 높은 산: {max(heights)}m")',
                      'print(f"가장 낮은 산: {min(heights)}m")',
                      'total = sum(heights)',
                      'print(f"높이 합계: {total}m")',
                      'print(f"평균 높이: {total // len(heights)}m (정수 몫)")'],
            'tool': [('개수와 대표 값',
                      '빈 목록에서는 max(), min(), 평균을 구할 수 없어요.',
                      ['scores = [2, 4, 6]',
                       'print(len(scores), sum(scores))',
                       'print(max(scores), min(scores))'],
                      '개수 3, 합계 12 / 가장 큰 값 6, 가장 작은 값 2예요.')],
            'ok': ['개수, 최댓값, 최솟값, 합계와 평균이 나왔어요.'],
            'hint': 'len은 개수, max·min은 양 끝 값, sum은 합계예요. 평균은 합계 ÷ 개수이며 여기서는 //로 소수 부분을 버려요.'}],
 'warm': 'heights = [8849, 8516, 8586]\n'
         'print(heights[3])\n'
         'heights.apend(8000)\n'
         'print("산 개수: " + len(heights))',
 'fixes': [('6', 'IndexError: list index out of range', 'heights[3] → heights[2]'),
           ('7', "AttributeError: 'list' object has no attribute 'apend'", 'apend → append'),
           ('8',
            'TypeError: can only concatenate str (not "int") to str',
            'print(f"산 개수: {len(heights)}")')],
 'warm_order': '6 → 7 → 8번 줄 순서다. 고친 출력: 8586 / 산 개수: 4.',
 'trace_q': '위 도구 카드의 remove()와 pop()을 살펴본 뒤 예상해요. 단계 2 직후 heights=[8516, 8586, 8849]에서 '
            'remove(8586) → pop()을 차례로 실행해요.',
 'trace_heads': ['remove 뒤 목록', 'pop이 꺼낸 값', '마지막 목록'],
 'trace_ans': ['[8516, 8849]', '8849', '[8516]'],
 'must': ['remove(8586)으로 산 하나를 뺀 뒤 다시 sort() 했어요.',
          'pop()으로 마지막 높이를 꺼내 별도 변수에 담아 보여 줬어요.',
          '남은 목록의 개수와 최댓값·최솟값·합계·평균을 다시 보여 줬어요.'],
 'more': ['목록에 실제 산 높이를 더해요.', '높은 순서로 보여 주는 방법을 찾아요.'],
 'change_example': ['heights.remove(8586)',
                    'heights.sort()',
                    'removed = heights.pop()',
                    'print(f"꺼낸 높이: {removed}")',
                    'print(heights)',
                    'print(len(heights), max(heights), min(heights))',
                    'print(sum(heights), sum(heights) // len(heights))'],
 'new': ['[높이, 이름]을 함께 정렬하기', '우리 가족 키 정렬하기'],
 'challenge_name': '우리 반 설문 막대그래프',
 'challenge_story': '시작 파일은 가상 학생 네 명의 하루 폰 사용 시간(분)이에요. 내 설문으로 바꾸고 번호별 값을 콘솔 기록표와 막대로 비교해요. '
                    '막대 길이는 가장 큰 값에 맞춰 자동으로 조절돼요. 음악 취향은 항목별 인원수로 바꿀 수 있어요.',
 'challenge_checks': ['설문 주제와 단위를 정하고 기록표에서 각 막대의 번호를 확인했어요.',
                      '응답 수만큼 막대 또는 0을 나타내는 시작점이 생겼어요.',
                      '최댓값과 최솟값, 평균을 글자로 보여 줬어요.'],
 'challenge_more': ['자료 수에 맞춰 세로 간격을 조절해요.'],
 'extension': 'import turtle as t\n'
              'minutes = [30, 90, 60, 120]\n'
              'if len(minutes) == 0 or min(minutes) < 0:\n'
              '    print("0 이상의 시간을 한 개 이상 넣어요.")\n'
              'else:\n'
              '    scale = 1\n'
              '    if max(minutes) > 0:\n'
              '        scale = 300 / max(minutes)\n'
              '    gap = 280 / len(minutes)\n'
              '    y = 140\n'
              '    number = 1\n'
              '    t.pensize(18)\n'
              '    print("하루 폰 사용 시간 / 단위: 분 / 가상 자료")\n'
              '    for value in minutes:\n'
              '        t.penup()\n'
              '        t.goto(-150, y)\n'
              '        t.dot(4, "gray")\n'
              '        t.pendown()\n'
              '        t.forward(value * scale)\n'
              '        print(f"위에서 {number}번: {value}분")\n'
              '        number = number + 1\n'
              '        y = y - gap\n'
              '    print(f"최대: {max(minutes)}, 최소: {min(minutes)}")\n'
              '    print(f"평균: {sum(minutes) // len(minutes)}분 (정수 몫)")\n'
              't.done()',
 'extension_solution': 'import turtle as t\n'
                       'minutes = [30, 90, 60, 120]\n'
                       'if len(minutes) == 0 or min(minutes) < 0:\n'
                       '    print("0 이상의 시간을 한 개 이상 넣어요.")\n'
                       'else:\n'
                       '    scale = 1\n'
                       '    if max(minutes) > 0:\n'
                       '        scale = 300 / max(minutes)\n'
                       '    gap = 280 / len(minutes)\n'
                       '    y = 140\n'
                       '    number = 1\n'
                       '    t.pensize(18)\n'
                       '    print("하루 폰 사용 시간 / 단위: 분 / 가상 자료")\n'
                       '    for value in minutes:\n'
                       '        t.penup()\n'
                       '        t.goto(-150, y)\n'
                       '        t.dot(4, "gray")\n'
                       '        t.pencolor("teal")\n'
                       '        if value == max(minutes):\n'
                       '            t.pencolor("coral")\n'
                       '        t.pendown()\n'
                       '        t.forward(value * scale)\n'
                       '        print(f"위에서 {number}번: {value}분")\n'
                       '        number = number + 1\n'
                       '        y = y - gap\n'
                       '    print(f"응답 수: {len(minutes)}")\n'
                       '    print(f"최대: {max(minutes)}, 최소: {min(minutes)}")\n'
                       '    print(f"평균: {sum(minutes) // len(minutes)}분 (정수 몫)")\n'
                       't.done()',
 'hint_tool': 'remove(값)는 같은 값을 하나 지워요. pop()은 마지막 값을 꺼내 돌려줘요. 둘 다 원래 목록을 바꿔요.',
 'hint_code': 'heights.remove(8586)\n'
              'heights.sort()\n'
              'removed = heights.pop()\n'
              'print(removed)\n'
              'print(heights)',
 'challenge_hint': 'value는 분 단위 자료, scale은 가장 긴 막대를 300으로 맞추는 배율이에요. gap은 막대 사이 간격이에요. 번호는 '
                   'number에 담아요. 자료는 0 이상의 수를 한 개 이상 넣어요.',
 'challenge_code': 'print(f"응답 수: {len(minutes)}")\n'
                   'print(f"평균: {sum(minutes) // len(minutes)}분 (정수 몫)")',
 'teaching': '세계 산 중 네팔의 세 산을 예로 쓴다. 에베레스트 8848.86m는 정수 8849m로 반올림한 수업용 값이다. 로체 8516m, 칸첸중가 '
             '8586m를 쓴다. 수치의 합계는 크기 비교 연습이며 지리적 의미를 과장하지 않는다. sort는 None을 반환하므로 heights = '
             'heights.sort()로 쓰지 않는다. remove와 pop 후에도 한 값이 남게 설계했다. // 평균은 소수 부분을 버린 정수 몫이다. '
             'remove와 pop은 바꾸기 블록에서 설명한 후 예측한다. 설문은 가장 긴 막대를 300 화면 단위로 맞추며 y 간격도 응답 수에 따라 '
             '바뀐다. 가상 자료의 콘솔 기록표는 위에서부터 막대와 대응한다. 음악 취향으로 바꾸면 제목·단위를 항목명·명으로 함께 고친다. 빈 목록·음수 '
             '자료는 안내만 출력하고 통계를 계산하지 않는다.',
 'change_guidance': '처음 세 높이에서 시작해요. remove → sort → pop은 한 번씩만 추가하고, 남은 목록으로 통계를 다시 계산해요.',
 'change_solution': 'heights = [8849, 8516, 8586]\n'
                    'print("산 높이(m)")\n'
                    'for height in heights:\n'
                    '    print(height)\n'
                    '# 단계 1 코드 아래에 이어서 써요.\n'
                    'heights.sort()\n'
                    'print("낮은 산부터")\n'
                    'for height in heights:\n'
                    '    print(height)\n'
                    '# 단계 2 코드 아래에 이어서 써요.\n'
                    'print(f"산 개수: {len(heights)}")\n'
                    'print(f"가장 높은 산: {max(heights)}m")\n'
                    'print(f"가장 낮은 산: {min(heights)}m")\n'
                    'total = sum(heights)\n'
                    'print(f"높이 합계: {total}m")\n'
                    'print(f"평균 높이: {total // len(heights)}m (정수 몫)")\n'
                    'heights.remove(8586)\n'
                    'heights.sort()\n'
                    'removed = heights.pop()\n'
                    'print(f"꺼낸 높이: {removed}")\n'
                    'print(heights)\n'
                    'print(len(heights), max(heights), min(heights))\n'
                    'print(sum(heights), sum(heights) // len(heights))',
 'hint_instruction': '단계 3 아래에 이어 써요. remove와 pop은 각각 한 번만 실행해요.',
 'challenge_instruction': '도전 코드의 else 안, t.done() 앞에 4칸 들여쓰기로 넣어요.',
 'plan_example': ['예) 기록 정리 순서', 'remove → sort → pop → 남은 값 요약']}
