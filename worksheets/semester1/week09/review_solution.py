# 9주 보충 문제: 1~8주 복습 (예시 답안)
# 문제마다 교안의 미션을 한 예시예요. 학생마다 문구와 값은 달라도 돼요.

import random

pick = input("몇 번 문제를 풀까요? (1~6): ").strip()

if pick == "1":
    # 문제 1 (1주): 별명 카드 / 미션: 좋아하는 음식도 묻고 한 줄 더 보여 주기
    name = input("이름: ")
    nickname = input("별명: ")
    food = input("좋아하는 음식: ")
    print("[" + name + "] 별명: " + nickname)
    print("좋아하는 음식: " + food)

elif pick == "2":
    # 문제 2 (2주): 음료수 자판기 / 미션: 음료 하나 더하기
    drink = input("콜라 / 사이다 / 주스 / 우유 중 고르세요: ").strip()
    if drink == "콜라":
        print("콜라가 나왔어요.")
    elif drink == "사이다":
        print("사이다가 나왔어요.")
    elif drink == "주스":
        print("주스가 나왔어요.")
    elif drink == "우유":
        print("우유가 나왔어요.")
    else:
        print("그런 음료는 없어요.")

elif pick == "3":
    # 문제 3 (3·4주): 주사위 두 개 / 미션: 두 주사위가 같으면 "더블!"
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    total = a + b
    print(f"주사위: {a} + {b} = {total}")
    if total % 2 == 0:
        print("짝수가 나왔어요.")
    else:
        print("홀수가 나왔어요.")
    if a == b:
        print("더블!")

elif pick == "4":
    # 문제 4 (6주): 영화 관람 판정 / 미션: 12살 이상이고 보호자와 왔으면 팝콘 쿠폰
    age = int(input("나이 (숫자만): "))
    with_parent = input("보호자와 함께 왔나요? (네/아니요): ").strip()
    can_watch = False
    if age >= 12 or with_parent == "네":
        can_watch = True
    if can_watch:
        print("입장할 수 있어요.")
    else:
        print("다음에 보호자와 함께 와요.")
    if age >= 12 and with_parent == "네":
        print("팝콘 쿠폰을 드려요.")

elif pick == "5":
    # 문제 5 (7주): 저금통 / 미션: 5000원 이상 모으면 저절로 멈추기
    saved = 0
    while True:
        coin = int(input("넣을 돈 (그만하려면 0): "))
        if coin == 0:
            break
        saved = saved + coin
        if saved >= 5000:
            print("목표 5000원 달성!")
            break
    print(f"모은 돈: {saved}원")

elif pick == "6":
    # 문제 6 (8주): 소풍 가방 / 미션: "끝"을 넣을 때까지 여러 개 넣기
    bag = ["물", "김밥"]
    while True:
        item = input("가방에 넣을 물건 (그만하려면 끝): ").strip()
        if item == "끝":
            break
        if item in bag:
            print("이미 들어 있어요.")
        else:
            bag.append(item)
    print(f"가방: {bag}")
    print(f"먼저 먹을 것: {random.choice(bag)}")

else:
    print("1~6 중에서 골라요.")
