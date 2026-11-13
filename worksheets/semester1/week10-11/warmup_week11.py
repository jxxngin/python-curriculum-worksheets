# 11주 워밍업: 방탈출 목숨 계산기
# 문제를 맞히면 열쇠를 얻고, 틀리면 목숨이 하나씩 줄어요. 목숨이 0이 되면 게임 오버예요.
# 오류가 3개 있어요. 고쳐 보세요.

lives = 3
keys = []

while lives > 0:
    answer = input("7 x 6 = ").strip()
    if answer == "42":
    keys.append("1번 열쇠")
        print("철컥! 열쇠를 얻었어요.")
        break

    print("땡! 남은 목숨: " + lives)

if lives > 0:
    print(f"탈출 성공! 모은 열쇠: {keys}")
else:
    print("게임 오버")
