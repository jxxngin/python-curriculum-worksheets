# 5주 중간 프로젝트 (미니): 영어 단어 퀴즈 (예시 답안)
# 기본 퀴즈 + 바꾸기(단어 늘리기, 첫 글자 힌트, 철자 개수 문제, 등급)

import random

print("🔤 영어 단어 퀴즈 🔤")
print("영어 단어는 소문자로 입력하세요.")
name = input("이름: ")
score = 0

# 1번: 뜻 보고 영어 쓰기 (5개 중 하나, 첫 글자 힌트)
pick = random.randint(1, 5)
if pick == 1:
    meaning = "사과"
    word = "apple"
    first = "a"
elif pick == 2:
    meaning = "학교"
    word = "school"
    first = "s"
elif pick == 3:
    meaning = "친구"
    word = "friend"
    first = "f"
elif pick == 4:
    meaning = "나비"
    word = "butterfly"
    first = "b"
else:
    meaning = "도서관"
    word = "library"
    first = "l"

print("")
print(f"[1번] '{meaning}'를 영어로 쓰면? (힌트: {first}로 시작)")
answer = input("> ").strip()
if answer == word:
    print("⭕ 정답! +10점")
    score = score + 10
else:
    print(f"❌ 정답은 {word}")

# 2번: 영어 보고 뜻 쓰기
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

print("")
print(f"[2번] '{word}'의 뜻은?")
answer = input("> ").strip()
if answer == meaning:
    print("⭕ 정답! +10점")
    score = score + 10
else:
    print(f"❌ 정답은 {meaning}")

# 3번: 숫자 영어 (random + 숫자 비교)
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

print("")
print(f"[3번] '{word}'는 숫자로 얼마일까요?")
answer = int(input("> "))
if answer == number:
    print("⭕ 정답! +10점")
    score = score + 10
else:
    print(f"❌ 정답은 {number} (차이 {abs(answer - number)})")

print("")
print(f"🏆 {name}님의 점수: {score}점 / 30점")
if score == 30:
    print("등급: 🌟 Word Master!")
elif score >= 10:
    print("등급: 👍 Good job!")
else:
    print("등급: 💪 Try again!")
