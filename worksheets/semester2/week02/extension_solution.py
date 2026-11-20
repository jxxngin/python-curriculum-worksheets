# 2학기 2주 도전 프로젝트: 스피로그래프 만다라 (예시 답안)
# 무늬 1은 원 36개로 늘려 꽉 채우고, 무늬 2(작은 주황 원)를 겹쳤어요.

import turtle

turtle.speed(0)   # 가장 빠르게 그려요

# 무늬 1: 반지름 80인 원 36개, 10도씩 돌기 (36 × 10 = 360)
turtle.pensize(2)
turtle.color("purple")
for i in range(36):
    turtle.circle(80)
    turtle.left(10)

# 무늬 2: 반지름 40인 원 12개, 30도씩 돌기 (12 × 30 = 360)
turtle.color("orange")
for i in range(12):
    turtle.circle(40)
    turtle.left(30)

turtle.hideturtle()
# 이 줄은 늘 맨 아래에 둬요. 새 코드는 이 줄 위에 써요.
turtle.done()
