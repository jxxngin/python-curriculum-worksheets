# 기말 프로젝트 (미니): 수학 문제 방탈출 — 예시 답안
# 최소 완성 기준: 방 3개, 방마다 무작위 문제를 맞힐 때까지 반복, 목숨 3개, 열쇠 리스트
# 추가 기능: 방마다 다른 연산, 남은 목숨 하트 표시, 탈출 등급

import random
import time

print("🔐 수학 문제 방탈출 🔐")
print("방 3개를 모두 지나 열쇠 3개를 모으면 탈출이에요. 목숨은 3개!")
time.sleep(1)

lives = 3
keys = []
room = 1

while room <= 3 and lives > 0:
    if room == 1:
        print("\n=== 1번 방: 덧셈의 방 ➕ ===")
    elif room == 2:
        print("\n=== 2번 방: 구구단의 방 ✖️ ===")
    else:
        print("\n=== 3번 방: 나머지의 방 ➗ ===")
    time.sleep(1)

    while lives > 0:                    # 맞힐 때까지 반복 (목숨이 남아 있는 동안)
        if room == 1:
            a = random.randint(10, 50)
            b = random.randint(10, 50)
            question = f"{a} + {b} = "
            answer = a + b
        elif room == 2:
            a = random.randint(2, 9)
            b = random.randint(2, 9)
            question = f"{a} × {b} = "
            answer = a * b
        else:
            a = random.randint(10, 50)
            b = random.randint(3, 9)
            question = f"{a}을(를) {b}로 나눈 나머지는? "
            answer = a % b

        reply = int(input(question))
        if reply == answer:
            keys.append(f"{room}번 열쇠")
            print(f"철컥! 🔑 {room}번 열쇠를 얻었어요.")
            break
        lives = lives - 1
        if lives == 3:
            hearts = "❤️❤️❤️"
        elif lives == 2:
            hearts = "❤️❤️🤍"
        elif lives == 1:
            hearts = "❤️🤍🤍"
        else:
            hearts = "🤍🤍🤍"
        print(f"땡! 정답은 {answer}. 남은 목숨 {hearts}")

    room = room + 1

print("\n문을 확인하는 중...")
time.sleep(1)
print(f"모은 열쇠: {keys}")
if "3번 열쇠" in keys:
    print("🎉 탈출 성공! 바깥 공기가 상쾌해요.")
    if lives == 3:
        print("등급: 🏆 한 번도 안 틀린 수학 천재")
    elif lives == 2:
        print("등급: 🥈 침착한 탐험가")
    else:
        print("등급: 🥉 아슬아슬 생존자")
else:
    print("💀 목숨을 모두 잃었어요. 다시 도전해 봐요!")
