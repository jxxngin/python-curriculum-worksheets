# 9주 워밍업: 보물 상자 열기
# 열쇠 명단(리스트)에서 맞는 열쇠를 골라 보물 상자를 여는 프로그램이에요. 기회는 3번!
# 오류가 3개 있어요. 고쳐 보세요.

keys = ["금 열쇠", "은 열쇠", "동 열쇠"]
print(f"가진 열쇠: {keys}")
print(f"마지막 열쇠: {keys[3]}")

tries = 0
while tries < 3:
    pick = input("어떤 열쇠를 쓸까요? ").strip()
    tries = tries + 1
    if pick = "금 열쇠":
        print("🎁 상자가 열렸어요!")
        break
    print(f"철컥... 안 맞아요. 남은 기회: {tries - 3}")
