# 5주 미니 프로젝트: 교과 퀴즈 (정답)
# 교안의 단계 순서대로 이어 쓴 완성본이에요.

# 단계 1: 퀴즈 시작하기
import random
print("수학 연산 퀴즈")
name = input("이름: ")
score = 0
print(f"{name}님, 문제마다 맞히면 점수를 받아요!")

# 단계 2: 1번 문제 내고 채점하기
answer = input("1번. 7 x 8 = ").strip()
if answer == "56":
    print("정답! +10점")
    score = score + 10
else:
    print("아쉬워요. 정답은 56")

# 단계 3: 보너스 문제: 점수를 무작위로
bonus = random.randint(1, 3) * 5
answer = input(f"보너스 문제 ({bonus}점). 100 나누기 4 = ").strip()
if answer == "25":
    print(f"정답! +{bonus}점")
    score = score + bonus

# 단계 4: 점수와 등급 보여 주기
print(f"{name}님의 점수: {score}점")
if score >= 20:
    print("등급: 퀴즈 박사")
elif score >= 10:
    print("등급: 퀴즈 탐험가")
else:
    print("등급: 다시 도전!")

# ----- 바꾸기 예시 (선생님용). 주석을 풀어 단계 4(점수와 등급) 코드 바로 위에 넣으면 실행돼요 -----
# a = random.randint(2, 9)
# b = random.randint(2, 9)
# answer2 = int(input(f"2번. {a} x {b} = "))
# if answer2 == a * b:
#     print("정답! +10점")
#     score = score + 10
# else:
#     print(f"아쉬워요. 정답은 {a * b}")
