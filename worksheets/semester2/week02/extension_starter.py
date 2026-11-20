# 2학기 2주 도전 프로젝트: 스피로그래프 만다라
# 이 코드는 그대로 실행돼요. 원을 조금씩 돌려 가며 겹쳐 그려서 만다라 무늬를 만들어요.
# 원 개수, 도는 각도, 크기, 색을 바꾸고 무늬를 하나 더 겹쳐 보세요.

import turtle

turtle.speed(0)   # 가장 빠르게 그려요

# 무늬 1: 반지름 80인 원 12개, 30도씩 돌기 (12 × 30 = 360)
turtle.color("purple")
for i in range(12):
    turtle.circle(80)
    turtle.left(30)

turtle.hideturtle()
# 이 줄은 늘 맨 아래에 둬요. 새 코드는 이 줄 위에 써요.
turtle.done()
