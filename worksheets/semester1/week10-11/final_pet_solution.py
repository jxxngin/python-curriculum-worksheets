# 기말 프로젝트 (미니): 펫과 함께하는 하루 — 예시 답안
# 최소 완성 기준: 10턴, 행동 3개(밥, 놀기, 재우기), 배고픔·기분 수치 2개, 행복도로 성공·실패 판정
# 추가 기능: 무작위 사건, 장난감 리스트, 하루 일기 리스트

import random
import time

pet = input("펫 이름을 지어 주세요: ").strip()
print(f"🐾 {pet}와(과) 함께하는 하루가 시작됐어요!")

hunger = 5
mood = 5
turn = 1
toys = ["공", "인형"]
diary = []

while turn <= 10:
    print(f"\n[{turn}턴] 🍖 배고픔 {hunger} / 😊 기분 {mood}")
    action = input("1. 밥 주기  2. 놀기  3. 재우기 > ").strip()

    if action == "1":
        hunger = hunger - 3
        print(f"냠냠! {pet}가 밥을 먹었어요.")
        diary.append("밥")
    elif action == "2":
        toy = random.choice(toys)
        mood = mood + 3
        hunger = hunger + 1
        print(f"{pet}가 {toy}을(를) 가지고 신나게 놀았어요!")
        diary.append("놀기")
    elif action == "3":
        mood = mood + 1
        print(f"쿨쿨... {pet}가 낮잠을 잤어요. 💤")
        diary.append("잠")
    else:
        print(f"{pet}가 고개를 갸웃해요. (1~3 중에서 골라요)")
        continue                      # 턴을 쓰지 않고 다시 고르기

    # 무작위 사건
    event = random.randint(1, 6)
    if event == 1:
        print("🌧️ 비가 와서 산책을 못 갔어요. 기분 -2")
        mood = mood - 2
    elif event == 2:
        print("🎁 새 장난감 '깃털'을 주웠어요!")
        if "깃털" not in toys:
            toys.append("깃털")

    hunger = hunger + 1               # 시간이 지나면 배고파져요
    if hunger > 10:
        hunger = 10
    if hunger < 0:
        hunger = 0
    if mood > 10:
        mood = 10
    if mood < 0:
        mood = 0

    time.sleep(0.5)
    turn = turn + 1

print("\n🌙 하루가 끝났어요...")
time.sleep(1)
happy = mood * 10 - hunger * 5
print(f"배고픔 {hunger} / 기분 {mood} → 행복도 {happy}점")
print(f"오늘의 일기: {diary}")
if happy >= 60:
    print(f"🎉 성공! {pet}는 오늘 정말 행복했어요.")
else:
    print(f"😢 실패... {pet}가 조금 서운했대요. 내일 다시 도전!")
