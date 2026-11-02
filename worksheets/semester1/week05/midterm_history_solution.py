# 5주 중간 프로젝트 (미니): 역사 인물 퀴즈 (예시 답안)
# 기본 퀴즈 + 바꾸기(인물 추가, 힌트 기회, 라운드 추가, 인물 한 줄 설명, 등급)

import random

print("📜 역사 인물 퀴즈 📜")
name = input("이름: ")
score = 0

# 1라운드: 무작위 인물 문제 (5명 중 하나)
pick = random.randint(1, 5)
if pick == 1:
    question = "한글(훈민정음)을 만든 조선의 왕은?"
    correct = "세종대왕"
    hint = "세○대왕"
    info = "백성이 쉽게 글을 읽고 쓰도록 1443년에 훈민정음을 만들었어요."
elif pick == 2:
    question = "거북선을 이끌고 바다를 지킨 장군은?"
    correct = "이순신"
    hint = "이○○"
    info = "임진왜란 때 한산도 대첩 등에서 큰 승리를 거두었어요."
elif pick == 3:
    question = "3·1 운동 때 아우내 장터에서 만세를 외친 독립운동가는?"
    correct = "유관순"
    hint = "유○○"
    info = "열여섯 살 나이에 독립 만세 운동을 이끌었어요."
elif pick == 4:
    question = "대동여지도를 만든 지리학자는?"
    correct = "김정호"
    hint = "김○○"
    info = "전국을 자세히 담은 지도 대동여지도를 목판으로 만들었어요."
else:
    question = "수원 화성 설계에 참여하고 거중기를 고안한 실학자는?"
    correct = "정약용"
    hint = "정○○"
    info = "백성에게 도움이 되는 학문(실학)을 연구했어요."

print("")
print(f"[1라운드] {question}")
answer = input("정답 (모르면 '힌트'): ").strip()

points = 10
if answer == "힌트":
    print(f"💡 힌트: {hint} (맞히면 5점)")
    answer = input("정답: ").strip()
    points = 5

if answer == correct:
    print(f"⭕ 정답! +{points}점")
    score = score + points
else:
    print(f"❌ 아쉬워요. 정답은 {correct}")
print(f"📖 {info}")

# 2라운드: 객관식
print("")
print("[2라운드] 측우기와 해시계(앙부일구) 제작에 힘쓴 과학자는?")
print("1. 장영실   2. 정약용   3. 김정호")
answer = input("번호: ").strip()
if answer == "1":
    print("⭕ 정답! +10점")
    score = score + 10
else:
    print("❌ 아쉬워요. 정답은 1번 장영실")

# 3라운드: O/X
print("")
print("[3라운드] O/X 퀴즈: 고구려의 광개토대왕은 영토를 크게 넓힌 왕이다.")
answer = input("O 또는 X: ").strip()
if answer == "O":
    print("⭕ 정답! +10점")
    score = score + 10
else:
    print("❌ 아쉬워요. 정답은 O")

print("")
print(f"🏆 {name}님의 점수: {score}점 / 30점")
if score >= 30:
    print("등급: 👑 역사 박사")
elif score >= 15:
    print("등급: 📚 역사 탐험가")
else:
    print("등급: 🌱 역사 새싹 - 인물 이야기를 더 찾아봐요!")
