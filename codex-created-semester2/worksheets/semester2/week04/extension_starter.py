# 우리 반 설문 막대그래프
import turtle as t
minutes = [30, 90, 60, 120]
if len(minutes) == 0 or min(minutes) < 0:
    print("0 이상의 시간을 한 개 이상 넣어요.")
else:
    scale = 1
    if max(minutes) > 0:
        scale = 300 / max(minutes)
    gap = 280 / len(minutes)
    y = 140
    number = 1
    t.pensize(18)
    print("하루 폰 사용 시간 / 단위: 분 / 가상 자료")
    for value in minutes:
        t.penup()
        t.goto(-150, y)
        t.dot(4, "gray")
        t.pendown()
        t.forward(value * scale)
        print(f"위에서 {number}번: {value}분")
        number = number + 1
        y = y - gap
    print(f"최대: {max(minutes)}, 최소: {min(minutes)}")
    print(f"평균: {sum(minutes) // len(minutes)}분 (정수 몫)")
t.done()
