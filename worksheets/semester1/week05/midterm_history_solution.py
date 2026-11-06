# 5주 중간 프로젝트: 역사 인물 퀴즈 (예시 답안)
# 교안의 공통 퀴즈 뼈대(시작 → 1번 문제 → 보너스 → 점수와 등급)를 역사로 바꾸고 문제 3개를 더했어요.
# 바꾸기 ★ 3개(교과로 바꾸기, 문제 3개 이상 더하기, 등급 기준 고치기)를 모두 채운 예시예요.
# 더 해 보기: 정답 뒤 인물 한 줄 설명, 4번은 무작위 인물 + 힌트 기회(새로 만들기)

import random

print("📜 역사 인물 퀴즈 📜")
name = input("이름: ")
score = 0
print(f"{name}님, 문제마다 맞히면 점수를 받아요!")

# 1번 문제 (교안의 1번을 역사로 바꿈)
answer = input("1번. 한글(훈민정음)을 만든 조선의 왕은? ").strip()
if answer == "세종대왕":
    print("⭕ 정답! +10점")
    score = score + 10
else:
    print("❌ 아쉬워요. 정답은 세종대왕")
print("📖 백성이 쉽게 글을 읽고 쓰도록 1443년에 훈민정음을 만들었어요.")

# 보너스 문제 (점수를 무작위로)
bonus = random.randint(1, 3) * 5
answer = input(f"보너스 문제 ({bonus}점). 거북선을 이끌고 바다를 지킨 장군은? ").strip()
if answer == "이순신":
    print(f"⭕ 정답! +{bonus}점")
    score = score + bonus
print("📖 임진왜란 때 한산도 대첩 등에서 큰 승리를 거두었어요.")

# ----- 더한 문제 3개 -----
# 2번: 객관식
print("")
print("2번. 측우기와 해시계(앙부일구) 제작에 힘쓴 과학자는?")
print("1. 장영실   2. 정약용   3. 김정호")
answer = input("번호: ").strip()
if answer == "1":
    print("⭕ 정답! +10점")
    score = score + 10
else:
    print("❌ 아쉬워요. 정답은 1번 장영실")

# 3번: O/X
answer = input("3번. O/X 퀴즈: 고구려의 광개토대왕은 영토를 크게 넓힌 왕이다. (O/X) ").strip()
if answer == "O":
    print("⭕ 정답! +10점")
    score = score + 10
else:
    print("❌ 아쉬워요. 정답은 O")

# 4번: 무작위 인물 + 힌트 기회 (points)
pick = random.randint(1, 3)
if pick == 1:
    question = "3·1 운동 때 아우내 장터에서 만세를 외친 독립운동가는?"
    correct = "유관순"
    hint = "유○○"
elif pick == 2:
    question = "대동여지도를 만든 지리학자는?"
    correct = "김정호"
    hint = "김○○"
else:
    question = "수원 화성 설계에 참여하고 거중기를 고안한 실학자는?"
    correct = "정약용"
    hint = "정○○"

answer = input(f"4번. {question} (모르면 '힌트') ").strip()
points = 10
if answer == "힌트":
    print(f"💡 힌트: {hint} (맞히면 5점)")
    answer = input("다시 대답: ").strip()
    points = 5
if answer == correct:
    print(f"⭕ 정답! +{points}점")
    score = score + points
else:
    print(f"❌ 아쉬워요. 정답은 {correct}")

# 점수와 등급 (최고 55점에 맞춰 기준을 고침)
print("")
print(f"🏆 {name}님의 점수: {score}점")
if score >= 40:
    print("등급: 👑 역사 박사")
elif score >= 20:
    print("등급: 📚 역사 탐험가")
else:
    print("등급: 🌱 다시 도전! 인물 이야기를 더 찾아봐요")
