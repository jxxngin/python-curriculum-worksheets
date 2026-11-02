# 5주 중간 프로젝트 (미니): 영어 단어 퀴즈
# 빈칸(___)을 채워서 기본 퀴즈를 완성한 뒤, 나만의 단어장 퀴즈로 키워 보세요.
# 실행할 때마다 무작위로 단어가 나와요.

import random

print("🔤 영어 단어 퀴즈 🔤")
print("영어 단어는 소문자로 입력하세요.")
name = input("이름: ")
score = 0

# ----- 1번: 뜻 보고 영어 쓰기 -----
pick = random.randint(1, 3)
if pick == 1:
    meaning = "사과"
    word = "apple"
elif pick == 2:
    meaning = "학교"
    word = "school"
else:
    meaning = "친구"
    word = "friend"

print("")
# 빈칸 1: f-string으로 뜻(meaning) 변수를 문장 안에 넣어요.
print(f"[1번] '{___}'를 영어로 쓰면?")
answer = input("> ").strip()
# 빈칸 2: 내 답과 정답 단어가 같으면 정답이에요.
if answer == ___:
    print("⭕ 정답! +10점")
    score = score + 10
else:
    print(f"❌ 정답은 {word}")

# ----- 2번: 영어 보고 뜻 쓰기 -----
# 빈칸 3: 1부터 3까지 무작위 정수를 뽑는 코드를 완성해요.
pick = ___.randint(1, 3)
if pick == 1:
    word = "dog"
    meaning = "개"
elif pick == 2:
    word = "water"
    meaning = "물"
else:
    word = "book"
    meaning = "책"

print("")
print(f"[2번] '{word}'의 뜻은?")
answer = input("> ").strip()
if answer == meaning:
    print("⭕ 정답! +10점")
    # 빈칸 4: 점수에 10을 더해 다시 score에 넣어요.
    score = ___ + 10
else:
    print(f"❌ 정답은 {meaning}")

print("")
print(f"🏆 {name}님의 점수: {score}점 / 20점")
