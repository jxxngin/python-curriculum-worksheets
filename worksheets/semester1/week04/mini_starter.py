# 4주 미니 프로젝트: 비밀의 문
# 빈칸(___)을 채워서 무작위로 바뀌는 비밀의 문 게임을 완성해 보세요.

# 빈칸 1: 다른 사람이 만든 기능(모듈)을 가져오는 키워드예요.
___ random

print("🚪 비밀의 문에 오신 것을 환영합니다 🚪")
name = input("탐험가 이름: ")
score = 0

# ----- 1관문: 세 개의 문 -----
print("")
print("[1관문] 문이 3개 있어요. 하나 뒤에만 보물이 있어요!")
# 빈칸 2: 1부터 3까지 중 무작위 정수를 뽑는 함수예요. random.____(1, 3)
treasure_door = random.___(1, 3)
pick = int(input("몇 번 문을 열까요? (1~3): "))

if pick == treasure_door:
    print("💎 보물을 찾았어요!")
    score = score + 10
else:
    print(f"꽝! 보물은 {treasure_door}번 문에 있었어요.")

# ----- 2관문: 비밀번호 -----
print("")
print("[2관문] 1부터 20 사이의 비밀번호를 맞혀 보세요. 기회는 한 번!")
secret = random.randint(1, 20)
guess = int(input("비밀번호: "))
# 빈칸 3: 두 수의 차이를 항상 양수로 만들어 주는 함수예요. (거리 구하기)
gap = ___(guess - secret)

if gap == 0:
    print("🔓 딸깍! 문이 열렸어요!")
    score = score + 20
# 빈칸 4: 차이가 3 이하이면 "아깝다"고 알려 줘요. 알맞은 비교 기호를 넣어 보세요.
elif gap ___ 3:
    print(f"아까워요! 비밀번호는 {secret}이었어요. (차이 {gap})")
    score = score + 5
else:
    print(f"멀었어요! 비밀번호는 {secret}이었어요. (차이 {gap})")

print("")
print(f"🏆 {name}님의 점수: {score}점")
