# 4주 워밍업: 주사위 굴리기
# 주사위 두 개를 굴려서 합과 차이를 알려 주는 프로그램이에요.
# 이 코드에는 오류가 3개 숨어 있어요. 실행해서 오류 메시지를 읽고 고쳐 보세요!

print("🎲 주사위 두 개를 굴려요!")

dice1 = random.randint(1, 6)
dice2 = random.randInt(1, 6)

print(f"첫 번째 주사위: {dice1}")
print(f"두 번째 주사위: {dice2}")
print(f"합: {dice1 + dice2}")
print(f"차이: {abs(dice1 - dice2}")
