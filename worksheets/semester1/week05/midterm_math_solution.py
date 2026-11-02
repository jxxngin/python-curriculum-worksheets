# 5주 중간 프로젝트 (미니): 수학 연산 퀴즈 (예시 답안)
# 기본 퀴즈 + 바꾸기(난이도 선택, 문제 추가, 오차 알려 주기, 등급)

import random

print("➕➖✖️ 수학 연산 퀴즈 ➕➖✖️")
name = input("이름: ")
level = input("난이도를 고르세요 (1. 쉬움  2. 어려움): ").strip()

if level == "2":
    top = 999
    print("🔥 어려움 모드! 세 자리 수가 나와요.")
else:
    top = 99
    print("🌱 쉬움 모드! 두 자리 수가 나와요.")

score = 0

# 1번: 덧셈
a = random.randint(10, top)
b = random.randint(10, top)
answer = int(input(f"[1번] {a} + {b} = "))
if answer == a + b:
    print("정답! +10점")
    score = score + 10
else:
    print(f"땡! 정답은 {a + b} (내 답과 {abs(answer - (a + b))} 차이)")

# 2번: 뺄셈 (큰 수에서 작은 수를 빼도록 max와 abs 사용)
a = random.randint(10, top)
b = random.randint(10, top)
big = max(a, b)
small = a + b - big
answer = int(input(f"[2번] {big} - {small} = "))
if answer == abs(a - b):
    print("정답! +10점")
    score = score + 10
else:
    print(f"땡! 정답은 {abs(a - b)}")

# 3번: 곱셈
c = random.randint(2, 9)
d = random.randint(2, 9)
answer = int(input(f"[3번] {c} x {d} = "))
if answer == c * d:
    print("정답! +10점")
    score = score + 10
else:
    print(f"땡! 정답은 {c * d}")

# 4번: 몫
d = random.randint(2, 9)
q = random.randint(2, 9)
total = d * q
answer = int(input(f"[4번] {total} ÷ {d} = "))
if answer == total // d:
    print("정답! +10점")
    score = score + 10
else:
    print(f"땡! 정답은 {total // d}")

# 5번: 나머지
e = random.randint(10, 30)
f = random.randint(2, 5)
answer = int(input(f"[5번] {e}를 {f}로 나눈 나머지는? "))
if answer == e % f:
    print("정답! +10점")
    score = score + 10
else:
    print(f"땡! 정답은 {e % f}")

print("")
print(f"🏆 {name}님의 점수: {score}점 / 50점")
if score == 50:
    print("등급: 🥇 연산 마스터")
elif score >= 30:
    print("등급: 🥈 연산 고수")
else:
    print("등급: 🥉 연산 수련생 - 다시 도전!")
