# 5주 중간 프로젝트 (미니): 역사 인물 퀴즈
# 빈칸(___)을 채워서 기본 퀴즈를 완성한 뒤, 나만의 인물 퀴즈로 키워 보세요.
# 문제는 무작위로 하나씩 뽑혀서 실행할 때마다 순서가 달라져요.

import random

print("📜 역사 인물 퀴즈 📜")
name = input("이름: ")
score = 0

# ----- 1라운드: 무작위 인물 문제 -----
# 빈칸 1: 1부터 3까지 무작위 정수를 뽑아 문제 번호로 써요.
pick = random.randint(1, ___)

if pick == 1:
    question = "한글(훈민정음)을 만든 조선의 왕은?"
    correct = "세종대왕"
elif pick == 2:
    question = "거북선을 이끌고 바다를 지킨 장군은?"
    correct = "이순신"
else:
    question = "3·1 운동 때 아우내 장터에서 만세를 외친 독립운동가는?"
    correct = "유관순"

print("")
print(f"[1라운드] {question}")
# 빈칸 2: 입력 앞뒤의 빈칸을 없애 주는 함수예요.
answer = input("정답: ").___()

# 빈칸 3: 입력한 답(answer)과 정답(correct)이 같은지 비교해요.
if answer ___ correct:
    print("⭕ 정답! +10점")
    score = score + 10
else:
    print(f"❌ 아쉬워요. 정답은 {correct}")

# ----- 2라운드: 객관식 -----
print("")
print("[2라운드] 측우기와 해시계(앙부일구) 제작에 힘쓴 과학자는?")
print("1. 장영실   2. 정약용   3. 김정호")
answer = input("번호: ").strip()
# 빈칸 4: 정답 번호는 "1"이에요. 글자로 비교하니까 따옴표를 붙여요.
if answer == ___:
    print("⭕ 정답! +10점")
    score = score + 10
else:
    print("❌ 아쉬워요. 정답은 1번 장영실")

print("")
print(f"🏆 {name}님의 점수: {score}점 / 20점")
