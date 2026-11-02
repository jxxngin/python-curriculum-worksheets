# 4주 미니 프로젝트: 비밀의 문 (정답)

import random

# ===== 1단계 따라 하기 완성본 =====
print("🚪 비밀의 문에 오신 것을 환영합니다 🚪")
name = input("탐험가 이름: ")
score = 0

print("")
print("[1관문] 문이 3개 있어요. 하나 뒤에만 보물이 있어요!")
treasure_door = random.randint(1, 3)
pick = int(input("몇 번 문을 열까요? (1~3): "))

if pick == treasure_door:
    print("💎 보물을 찾았어요!")
    score = score + 10
else:
    print(f"꽝! 보물은 {treasure_door}번 문에 있었어요.")

print("")
print("[2관문] 1부터 20 사이의 비밀번호를 맞혀 보세요. 기회는 한 번!")
secret = random.randint(1, 20)
guess = int(input("비밀번호: "))
gap = abs(guess - secret)

if gap == 0:
    print("🔓 딸깍! 문이 열렸어요!")
    score = score + 20
elif gap <= 3:
    print(f"아까워요! 비밀번호는 {secret}이었어요. (차이 {gap})")
    score = score + 5
else:
    print(f"멀었어요! 비밀번호는 {secret}이었어요. (차이 {gap})")

# ===== 2단계 바꾸기 예시 =====
# 3관문 추가: 함정 문 5개 중 하나에 함정이 있어요. 함정만 피하면 통과!
print("")
print("[3관문] 문이 5개! 이번엔 함정 문 하나만 피하면 돼요.")
trap_door = random.randint(1, 5)
pick3 = int(input("몇 번 문을 열까요? (1~5): "))

if pick3 == trap_door:
    print("🕳️ 으악, 함정이에요! 점수 -5")
    score = score - 5
else:
    print(f"휴, 무사 통과! 함정은 {trap_door}번이었어요. 점수 +10")
    score = score + 10

# 4관문 추가: 행운의 주사위 (보너스 점수가 무작위)
print("")
print("[4관문] 행운의 주사위를 굴려요!")
input("Enter를 누르면 주사위를 굴려요...")
bonus = random.randint(1, 6)
print(f"🎲 {bonus}이(가) 나왔어요! 보너스 {bonus * 2}점")
score = score + bonus * 2

print("")
print(f"🏆 {name}님의 최종 점수: {score}점")
if score >= 40:
    print("전설의 탐험가! 🌟")
elif score >= 20:
    print("꽤 실력 있는 탐험가예요!")
else:
    print("다음엔 행운이 함께할 거예요!")
