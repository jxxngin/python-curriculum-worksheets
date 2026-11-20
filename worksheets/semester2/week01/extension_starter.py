# 2학기 1주 도전 프로젝트: 국기 그리기 챌린지
# 이 코드는 그대로 실행돼요. 왼쪽에 일본 국기를 그려요.
# 오른쪽에 스위스 국기를 더하고, 다른 나라 국기에도 도전해 보세요.

import turtle

# 일본 국기 바탕: 가로 240, 세로 160인 흰 직사각형
turtle.penup()
turtle.goto(-260, -80)
turtle.pendown()
turtle.color("black", "white")
turtle.begin_fill()
turtle.goto(-20, -80)
turtle.goto(-20, 80)
turtle.goto(-260, 80)
turtle.goto(-260, -80)
turtle.end_fill()

# 가운데 빨간 원: 가운데 (-140, 0), 반지름 48
turtle.penup()
turtle.goto(-140, -48)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
turtle.circle(48)
turtle.end_fill()

# 스위스 국기는 여기부터: 바탕은 (40, -80)에서 (200, 80)까지인 빨간 정사각형

turtle.hideturtle()
# 이 줄은 늘 맨 아래에 둬요. 새 코드는 이 줄 위에 써요.
turtle.done()
