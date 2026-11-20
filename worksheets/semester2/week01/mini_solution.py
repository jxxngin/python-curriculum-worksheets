# 1주 미니 프로젝트: 기분 이모지 (정답)
# 교안의 단계 순서대로 이어 쓴 완성본이에요.

import turtle

# 단계 1: 노란 얼굴 그리기
turtle.color("black", "yellow")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

# 단계 2: 눈 찍기
turtle.penup()
turtle.goto(-35, 130)
turtle.dot(25)
turtle.goto(35, 130)
turtle.dot(25)

# 단계 3: 웃는 입 그리기
turtle.goto(-40, 75)
turtle.pendown()
turtle.right(30)
turtle.forward(46)
turtle.left(60)
turtle.forward(46)

# 이 줄은 늘 맨 아래에 둬요. 단계 코드는 이 줄 위에 써요.
turtle.done()

# ----- 바꾸기 예시 (선생님용). 주석을 풀어 turtle.done() 줄 위에 넣으면 실행돼요 -----
# turtle.penup()
# turtle.goto(-60, 85)
# turtle.dot(20, "pink")
# turtle.goto(60, 85)
# turtle.dot(20, "pink")
