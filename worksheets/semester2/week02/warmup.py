# 2학기 2주 워밍업: 창문 그리기
# 이 코드에는 오류가 3개 숨어 있어요. 실행해서 오류 메시지를 읽고 고쳐 보세요!
# 오류 2개는 메시지가 나오고, 1개는 메시지 없이 그림만 틀려요.
# 다 고치면 파란 네모 창문 가운데에 + 모양 십자가 보여요.

import turtle

# 네모 창문: 변 4개
turtle.color("blue")
for i in range(4)
    turtle.forward(100)
    turtle.left(90)

# 창문 가운데 십자: 가운데에서 막대 4개
turtle.penup()
turtle.goto(50, 50)
turtle.pendown()
for i in range(4):
turtle.forward(50)
    turtle.backward(50)
    turtle.left(60)

turtle.done()
