# 교사용: 꼭 하기 세 가지를 만족하는 바꾸기 예시
import turtle as t
t.penup()
for number in range(3):
    t.goto(-150 + number * 150, 40)
    t.dot(60, "skyblue")
# 단계 1 코드 아래에 이어서 써요.
for number in range(3):
    t.goto(-150 + number * 150, 40)
    t.dot(70 + number * 15, "skyblue")
    t.pendown()
    t.goto(-150 + number * 150, -100)
    t.penup()
# 단계 2 코드 아래에 이어서 써요.
for number in range(3):
    for spot in range(2):
        t.goto(-165 + number * 150 + spot * 15, 40)
        t.dot(8, "white")
t.done()
