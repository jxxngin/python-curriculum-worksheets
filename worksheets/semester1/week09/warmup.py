# 9주 워밍업: 보물 상자 열기
# 열쇠 리스트에서 맞는 열쇠를 골라 보물 상자를 여는 프로그램이에요. 기회는 3번!
# 이 코드에는 오류가 3개 숨어 있어요. 고쳐 보세요!

keys = ["금 열쇠", "은 열쇠", "동 열쇠"]
print(f"가진 열쇠: {keys}")

tries = 0
while tries < 3:
    pick = input("어떤 열쇠를 쓸까요? ").strip()
    tries = tries + 1
    if pick = "금 열쇠":
        print("🎁 상자가 열렸어요!")
        break
    print("철컥... 안 맞아요. 남은 기회: " + (3 - tries))

print(f"사용한 기회: {tires}번")
