# 2학기 1주 워밍업: 해 그리기
# 이 코드에는 오류가 3개 숨어 있어요. 실행해서 오류 메시지를 읽고 고쳐 보세요!
# 오류 2개는 메시지가 나오고, 1개는 메시지 없이 그림만 틀려요.
# 다 고치면 노란 해 하나와 해 오른쪽의 햇살 선 하나만 보여요.

import turtle
# 해: 노란 원
turtle.color("orange", "yellow)
turtle.begin_fill()
turtle.circle(60)
turtle.end_fill()

# 햇살: 해 오른쪽에 짧은 선 하나
turtle.goto(80, 60)
turtle.pendown()
turtle.fowrard(50)
turtle.done()
