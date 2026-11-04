# 단계 1: 사탕 세 개 놓기
import turtle as t
t.penup()
for number in range(3):
    t.goto(-150 + number * 150, 40)
    t.dot(60, "pink")

# 단계 2: 막대와 다른 크기 더하기
# 단계 1 코드 아래에 이어서 써요.
for number in range(3):
    t.goto(-150 + number * 150, 40)
    t.dot(60 + number * 20, "hotpink")
    t.pendown()
    t.goto(-150 + number * 150, -100)
    t.penup()

# 단계 3: 사탕마다 작은 장식 세 개 찍기
# 단계 2 코드 아래에 이어서 써요.
for number in range(3):
    for spot in range(3):
        t.goto(-165 + number * 150 + spot * 15, 40)
        t.dot(8, "white")

# 그림 창을 열어 둬요.
t.done()

# 꼭 하기 세 가지를 모두 바꾼 예시는 mini_change_solution.py에 있다.
