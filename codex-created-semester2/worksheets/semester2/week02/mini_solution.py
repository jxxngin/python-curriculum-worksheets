# 단계 1: 첫 삼각 날개 그리기
import turtle as t
t.color("teal")
for side in range(3):
    t.forward(90)
    t.left(120)

# 단계 2: 두 번째 날개 더하기
# 단계 1 코드 아래에 이어서 써요.
t.left(90)
for side in range(3):
    t.forward(90)
    t.left(120)

# 단계 3: 세 번째 날개 더하기
# 단계 2 코드 아래에 이어서 써요.
t.left(90)
for side in range(3):
    t.forward(90)
    t.left(120)

# 단계 4: 네 번째 날개 완성하기
# 단계 3 코드 아래에 이어서 써요.
t.left(90)
for side in range(3):
    t.forward(90)
    t.left(120)

# 그림 창을 열어 둬요.
t.done()

# 꼭 하기 세 가지를 모두 바꾼 예시는 mini_change_solution.py에 있다.
