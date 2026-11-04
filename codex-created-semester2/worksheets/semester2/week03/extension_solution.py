# 제너러티브 아트 배경화면
import turtle as t
import random
t.speed(0)
t.penup()
colors = ["teal", "gold", "coral"]
for row in range(5):
    for col in range(6):
        t.goto(-175 + col * 70, -140 + row * 70)
        size = random.randint(12, 45)
        t.dot(size, random.choice(colors))
t.done()
