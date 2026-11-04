# 9주 보충 미니 문제 6개 (1~8주 복습)
# 문제마다 빈칸(___)을 채우고 실행해 보세요. 다 푼 문제는 주석 처리(#)하고 다음 문제로 가도 돼요.
# 빈칸이 남아 있으면 실행이 안 되니, 아직 안 푼 문제는 통째로 주석 처리해 두세요.
# (Thonny: 줄을 고르고 Alt+3 주석, Alt+4 주석 풀기)

import random

# ===== 문제 1 (1주): 별명 카드 =====
name = input("이름: ")
# 빈칸 1: 질문하고 대답을 받는 함수예요.
nickname = ___("별명: ")
# 빈칸 2: 문자열을 이어 붙이는 기호예요.
print("[" + name + "] 별명은 " ___ nickname + "!")

# ===== 문제 2 (2주): 음료수 자판기 =====
drink = input("콜라 / 사이다 / 주스 중 고르세요: ").strip()
if drink == "콜라":
    print("🥤 콜라가 나왔어요.")
# 빈칸 3: 앞 조건이 아닐 때 다른 조건을 하나 더 검사하는 키워드예요.
___ drink == "사이다":
    print("🫧 사이다가 나왔어요.")
elif drink == "주스":
    print("🧃 주스가 나왔어요.")
else:
    print("그런 음료는 없어요.")

# ===== 문제 3 (3·4주): 주사위 두 개 =====
a = random.randint(1, 6)
b = random.randint(1, 6)
total = a + b
print(f"🎲 {a} + {b} = {total}")
# 빈칸 4: 나눈 나머지를 구하는 연산자예요. (짝수는 2로 나눈 나머지가 0)
if total ___ 2 == 0:
    print("짝수가 나왔어요!")
else:
    print("홀수가 나왔어요!")

# ===== 문제 4 (6주): 영화 관람 판정 =====
age = int(input("나이: "))
with_parent = input("보호자와 함께 왔나요? ").strip()
# 빈칸 5: 두 조건 중 하나만 참이어도 참이 되는 키워드예요.
can_watch = False
if age >= 12 ___ with_parent == "네":
    can_watch = True
if can_watch:
    print("🎬 입장할 수 있어요!")
else:
    print("다음에 보호자와 함께 와요.")

# ===== 문제 5 (7주): 저금통 =====
saved = 0
while True:
    coin = int(input("넣을 돈 (그만하려면 0): "))
    if coin == 0:
        break
    # 빈칸 6: 지금까지 모은 돈에 이번 돈을 더해 쌓아요.
    saved = ___ + coin
print(f"🐷 모은 돈: {saved}원")

# ===== 문제 6 (8주): 소풍 가방 =====
bag = ["물", "김밥"]
item = input("가방에 넣을 물건: ").strip()
# 빈칸 7: 리스트에 들어 있는지 검사하는 키워드예요.
if item ___ bag:
    print("이미 들어 있어요!")
else:
    # 빈칸 8: 리스트 맨 뒤에 붙이는 함수예요.
    bag.___(item)
print(f"🎒 가방: {bag}")
print(f"오늘 먼저 먹을 것: {random.choice(bag)}")
