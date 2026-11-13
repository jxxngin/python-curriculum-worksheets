# 9주 보충 문제: 1~8주 복습
# 실행하면 문제 번호를 물어요. 고른 문제만 실행돼요.
# 교안의 미션대로 고른 문제 안(4칸 들여 쓴 곳)을 고쳐요.

import random

pick = input("몇 번 문제를 풀까요? (1~6): ").strip()

if pick == "1":
    # 문제 1 (1주): 별명 카드
    name = input("이름: ")
    nickname = input("별명: ")
    print("[" + name + "] 별명: " + nickname)

elif pick == "2":
    # 문제 2 (2주): 음료수 자판기
    drink = input("콜라 / 사이다 / 주스 중 고르세요: ").strip()
    if drink == "콜라":
        print("콜라가 나왔어요.")
    elif drink == "사이다":
        print("사이다가 나왔어요.")
    elif drink == "주스":
        print("주스가 나왔어요.")
    else:
        print("그런 음료는 없어요.")

elif pick == "3":
    # 문제 3 (3·4주): 주사위 두 개
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    total = a + b
    print(f"주사위: {a} + {b} = {total}")
    if total % 2 == 0:
        print("짝수가 나왔어요.")
    else:
        print("홀수가 나왔어요.")

elif pick == "4":
    # 문제 4 (6주): 영화 관람 판정
    age = int(input("나이 (숫자만): "))
    with_parent = input("보호자와 함께 왔나요? (네/아니요): ").strip()
    can_watch = False
    if age >= 12 or with_parent == "네":
        can_watch = True
    if can_watch:
        print("입장할 수 있어요.")
    else:
        print("다음에 보호자와 함께 와요.")

elif pick == "5":
    # 문제 5 (7주): 저금통
    saved = 0
    while True:
        coin = int(input("넣을 돈 (그만하려면 0): "))
        if coin == 0:
            break
        saved = saved + coin
    print(f"모은 돈: {saved}원")

elif pick == "6":
    # 문제 6 (8주): 소풍 가방
    bag = ["물", "김밥"]
    item = input("가방에 넣을 물건: ").strip()
    if item in bag:
        print("이미 들어 있어요.")
    else:
        bag.append(item)
    print(f"가방: {bag}")
    print(f"먼저 먹을 것: {random.choice(bag)}")

else:
    print("1~6 중에서 골라요.")
