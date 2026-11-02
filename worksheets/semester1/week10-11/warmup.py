# 10~11주 워밍업: 탐험가의 가방
# 가방을 여는 척 2초 기다렸다가(time.sleep), 찾는 물건이 가방에 있는지 알려 주는 프로그램이에요.
# 이 코드에는 오류가 3개 숨어 있어요. 고쳐 보세요!

import time

items = ["손전등", "열쇠", "지도"]
print("가방을 여는 중...")
time.slep(2)
print(f"가방 속: {items}")

while True:
    want = input("찾을 물건: ").strip()
    if want in items
        print(f"{want}을(를) 찾았어요!")
        break
    print("가방에 없어요...")
    tries = tries + 1
    print(f"못 찾은 횟수: {tries}")
