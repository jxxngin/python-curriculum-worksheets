# 8주 미니 프로젝트: 탐정의 용의자 명단
# 빈칸(___)을 채워서 용의자 명단(리스트)에서 범인을 찾는 추리 게임을 완성해 보세요.

import random

print("🔍 사라진 생일 케이크 사건 🔍")
suspects = ["옆집 고양이", "배고픈 동생", "택배 기사님"]
print(f"용의자 명단: {suspects}")
# 빈칸 1: 리스트의 첫 번째 칸 번호예요. (파이썬은 몇부터 셀까요?)
print(f"가장 먼저 의심받는 사람: {suspects[___]}")

new = input("수상한 사람을 한 명 더 적어 주세요: ").strip()
# 빈칸 2: 리스트 맨 뒤에 새 값을 붙이는 함수예요.
suspects.___(new)
print(f"새 명단: {suspects}")

# 빈칸 3: 리스트에서 하나를 무작위로 골라 주는 함수예요.
culprit = random.___(suspects)

tries = 0
while tries < 3:
    guess = input("범인은 누구일까요? ").strip()
    # 빈칸 4: guess가 명단에 들어 있는지 검사하는 키워드예요.
    if guess ___ suspects:
        tries = tries + 1
        if guess == culprit:
            print(f"🎉 정답! 범인은 {culprit}이었어요!")
            break
        else:
            print(f"❌ {guess}에게는 알리바이가 있어요.")
    else:
        print("명단에 없는 사람이에요. 다시 골라 주세요.")

print(f"사건 기록: 범인은 {culprit}")
