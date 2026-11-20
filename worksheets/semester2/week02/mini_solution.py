# 2주 미니 프로젝트: 바람개비 (정답)
# 교안의 단계 순서대로 이어 쓴 완성본이에요.

import turtle

# 단계 1: 막대 손잡이 그리기
turtle.pensize(6)
turtle.color("brown")
turtle.right(90)
turtle.forward(200)
turtle.backward(200)
turtle.left(90)

# 단계 2: 날개 자리 그리기
turtle.pensize(2)
turtle.color("black", "red")
for i in range(4):
    turtle.forward(100)
    turtle.backward(100)
    turtle.left(90)

# 단계 3: 날개 칠하기
for i in range(4):
    turtle.begin_fill()
    turtle.circle(50, 180)
    turtle.left(90)
    turtle.forward(100)
    turtle.end_fill()

# 이 줄은 늘 맨 아래에 둬요. 단계 코드는 이 줄 위에 써요.
turtle.done()

# ----- 바꾸기 예시 (선생님용). 주석을 풀어 단계 3 코드 대신 넣으면 실행돼요 -----
# turtle.color("black", "orange")
# for i in range(8):
#     turtle.begin_fill()
#     turtle.circle(50, 180)
#     turtle.left(90)
#     turtle.forward(100)
#     turtle.end_fill()
#     turtle.left(45)
