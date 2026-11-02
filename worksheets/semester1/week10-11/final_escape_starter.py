# 기말 프로젝트 (미니): 수학 문제 방탈출 — 시작 코드
# 이 코드는 그대로 실행돼요. 지금은 '방 1개, 덧셈 문제'만 있어요.
# 최소 완성 기준까지 키워 보세요!
#   [ ] 방 3개 (방마다 다른 종류의 문제)
#   [ ] 방마다 무작위 문제를 맞힐 때까지 반복
#   [ ] 목숨 3개 (틀리면 하나씩 줄고, 0이 되면 게임 오버)
#   [ ] 열쇠 리스트 (방을 나갈 때마다 열쇠를 append)

import random
import time

print("🔐 수학 문제 방탈출 🔐")
print("문제를 풀어야 다음 방 문이 열려요!")
time.sleep(1)            # 1초 기다리기 (명령 카드: time.sleep)

lives = 3                # 목숨
keys = []                # 모은 열쇠 리스트

print("\n=== 1번 방: 덧셈의 방 ===")
while True:              # 맞힐 때까지 반복
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    reply = int(input(f"{a} + {b} = "))
    if reply == a + b:
        print("철컥! 문이 열렸어요. 🔑")
        keys.append("덧셈 열쇠")
        break
    else:
        print("땡! 다시 풀어 봐요.")
        # TODO: 틀리면 목숨을 하나 줄이고, 0이 되면 게임 오버

# TODO: 2번 방, 3번 방 만들기 (곱셈, 나머지 등 다른 문제)
# TODO: 마지막에 열쇠 리스트를 보고 탈출 성공/실패 판정

print(f"\n모은 열쇠: {keys}")
