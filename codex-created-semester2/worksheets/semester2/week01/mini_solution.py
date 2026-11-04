# 단계 1: 얼굴 바탕 그리기
import turtle as t
t.color("gold")
t.begin_fill()
t.circle(80)
t.end_fill()
t.penup()

# 단계 2: 눈 두 개 찍기
# 단계 1 코드 아래에 이어서 써요.
t.goto(-30, 100)
t.dot(14, "black")
t.goto(30, 100)
t.dot(14, "black")

# 단계 3: 웃는 입 그리기
# 단계 2 코드 아래에 이어서 써요.
t.goto(-35, 65)
t.setheading(-90)
t.pencolor("black")
t.pendown()
t.circle(35, 180)
t.penup()

# 그림 창을 열어 둬요.
t.done()

# 꼭 하기 세 가지를 모두 바꾼 예시는 mini_change_solution.py에 있다.
