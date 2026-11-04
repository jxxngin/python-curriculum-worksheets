# 교사용: 꼭 하기 세 가지를 만족하는 바꾸기 예시
import turtle as t
t.color("skyblue")
t.begin_fill()
t.circle(80)
t.end_fill()
t.penup()
# 단계 1 코드 아래에 이어서 써요.
t.goto(-30, 100)
t.dot(18, "black")
t.goto(30, 100)
t.dot(18, "black")
# 단계 2 코드 아래에 이어서 써요.
t.goto(-35, 65)
t.setheading(-90)
t.pencolor("black")
t.pendown()
t.circle(35, 120)
t.penup()
t.done()
