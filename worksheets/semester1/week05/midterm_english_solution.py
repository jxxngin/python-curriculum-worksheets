# 5주 중간 프로젝트: 영어 단어 퀴즈 (예시 답안)
# 교안의 공통 퀴즈 뼈대(시작 → 1번 문제 → 보너스 → 점수와 등급)를 영어로 바꾸고 문제 3개를 더했어요.
# 바꾸기 ★ 3개(교과로 바꾸기, 문제 3개 이상 더하기, 등급 기준 고치기)를 모두 채운 예시예요.
# 더 해 보기: 뜻 보고 영어 쓰기, 첫 글자 힌트, 무작위 단어, 숫자 영어

import random

print("🔤 영어 단어 퀴즈 🔤")
print("영어 단어는 소문자로 입력하세요.")
name = input("이름: ")
score = 0
print(f"{name}님, 문제마다 맞히면 점수를 받아요!")

# 1번 문제 (교안의 1번을 영어로 바꿈)
answer = input("1번. '사과'를 영어로 쓰면? ").strip()
if answer == "apple":
    print("⭕ 정답! +10점")
    score = score + 10
else:
    print("❌ 아쉬워요. 정답은 apple")

# 보너스 문제 (점수를 무작위로)
bonus = random.randint(1, 3) * 5
answer = input(f"보너스 문제 ({bonus}점). '친구'를 영어로 쓰면? (힌트: f로 시작) ").strip()
if answer == "friend":
    print(f"⭕ 정답! +{bonus}점")
    score = score + bonus

# ----- 더한 문제 3개 -----
# 2번: 영어 보고 뜻 쓰기 (무작위 단어)
pick = random.randint(1, 4)
if pick == 1:
    word = "dog"
    meaning = "개"
elif pick == 2:
    word = "water"
    meaning = "물"
elif pick == 3:
    word = "book"
    meaning = "책"
else:
    word = "star"
    meaning = "별"

answer = input(f"2번. '{word}'의 뜻은? ").strip()
if answer == meaning:
    print("⭕ 정답! +10점")
    score = score + 10
else:
    print(f"❌ 아쉬워요. 정답은 {meaning}")

# 3번: 숫자 영어 (숫자로 받아 비교, 차이는 abs)
pick = random.randint(1, 3)
if pick == 1:
    word = "seven"
    number = 7
elif pick == 2:
    word = "twelve"
    number = 12
else:
    word = "twenty"
    number = 20

answer = int(input(f"3번. '{word}'는 숫자로 얼마일까요? (숫자만) "))
if answer == number:
    print("⭕ 정답! +10점")
    score = score + 10
else:
    print(f"❌ 정답은 {number} (차이 {abs(answer - number)})")

# 4번: 뜻 보고 영어 쓰기 (첫 글자 힌트)
answer = input("4번. '도서관'을 영어로 쓰면? (힌트: l로 시작) ").strip()
if answer == "library":
    print("⭕ 정답! +10점")
    score = score + 10
else:
    print("❌ 아쉬워요. 정답은 library")

# 점수와 등급 (최고 55점에 맞춰 기준을 고침)
print("")
print(f"🏆 {name}님의 점수: {score}점")
if score >= 40:
    print("등급: 🌟 Word Master!")
elif score >= 20:
    print("등급: 👍 Good job!")
else:
    print("등급: 💪 Try again!")
