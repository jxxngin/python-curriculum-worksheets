# 5주 중간 프로젝트 (미니): 수학 연산 퀴즈
# 빈칸(___)을 채워서 기본 퀴즈를 완성한 뒤, 나만의 퀴즈로 키워 보세요.

import random

print("➕➖✖️ 수학 연산 퀴즈 ➕➖✖️")
name = input("이름: ")
score = 0

# ----- 1번: 덧셈 -----
# 빈칸 1: 10부터 99까지 무작위 정수를 뽑아요.
a = random.___(10, 99)
b = random.randint(10, 99)
# 빈칸 2: 입력받은 글자를 정수로 바꿔요.
answer = ___(input(f"[1번] {a} + {b} = "))
if answer == a + b:
    print("정답! +10점")
    score = score + 10
else:
    print(f"땡! 정답은 {a + b}")

# ----- 2번: 곱셈 -----
c = random.randint(2, 9)
d = random.randint(2, 9)
answer = int(input(f"[2번] {c} x {d} = "))
# 빈칸 3: 곱셈 기호를 넣어 정답과 비교해요.
if answer == c ___ d:
    print("정답! +10점")
    score = score + 10
else:
    print(f"땡! 정답은 {c * d}")

# ----- 3번: 나머지 -----
e = random.randint(10, 30)
f = random.randint(2, 5)
answer = int(input(f"[3번] {e}를 {f}로 나눈 나머지는? "))
# 빈칸 4: 나머지를 구하는 기호예요.
if answer == e ___ f:
    print("정답! +10점")
    score = score + 10
else:
    print(f"땡! 정답은 {e % f}")

print("")
print(f"🏆 {name}님의 점수: {score}점 / 30점")
