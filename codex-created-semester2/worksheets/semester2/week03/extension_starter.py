# 제너러티브 아트 배경화면
import turtle as t
import random
t.speed(0)
t.penup()
for row in range(4):
    for col in range(5):
        t.goto(-160 + col * 80, -120 + row * 80)
        size = random.randint(10, 50)
        t.dot(size, "teal")
t.done()
