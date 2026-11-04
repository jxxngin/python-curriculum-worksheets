# 4주 미니 프로젝트: 비밀의 문 게임 (정답)
# 교안의 단계 순서대로 이어 쓴 완성본이에요.

# 단계 1: 보물 문을 무작위로 정하기
import random
name = input("탐험가 이름: ")
score = 0
treasure_door = random.randint(1, 3)
# print(f"(쉿! 테스트용) 보물은 {treasure_door}번 문")

# 단계 2: 1관문: 문을 골라 보물 찾기
pick = int(input("[1관문] 몇 번 문을 열까요? (1~3): "))
if pick == treasure_door:
    print("💎 보물을 찾았어요! +10점")
    score = score + 10
else:
    print(f"꽝! 보물은 {treasure_door}번 문에 있었어요.")

# 단계 3: 2관문: 비밀번호가 얼마나 가까운지 알려 주기
secret = random.randint(1, 20)
guess = int(input("[2관문] 1~20 중 비밀번호는? "))
gap = abs(guess - secret)
print(f"비밀번호와 {gap}만큼 차이 나요!")

# 단계 4: 점수를 주고 게임 끝내기
if gap == 0:
    score = score + 20
elif gap <= 3:
    score = score + 5
print(f"비밀번호는 {secret}이었어요.")
print(f"🏆 {name}님의 점수: {score}점")

# ----- 바꾸기 예시 (선생님용, 주석을 풀면 실행돼요) -----
# if score >= 30:
#     print("👑 전설의 탐험가!")
# elif score >= 15:
#     print("🗺️ 용감한 탐험가!")
# else:
#     print("🌱 초보 탐험가")
