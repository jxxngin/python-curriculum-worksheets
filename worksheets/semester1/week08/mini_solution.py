# 8주 미니 프로젝트: 탐정의 용의자 명단 (정답)

import random

# ===== 1단계 따라 하기 완성본 =====
print("🔍 사라진 생일 케이크 사건 🔍")
suspects = ["옆집 고양이", "배고픈 동생", "택배 기사님"]
print(f"용의자 명단: {suspects}")
print(f"가장 먼저 의심받는 사람: {suspects[0]}")

new = input("수상한 사람을 한 명 더 적어 주세요: ").strip()
suspects.append(new)
print(f"새 명단: {suspects}")

culprit = random.choice(suspects)

tries = 0
while tries < 3:
    guess = input("범인은 누구일까요? ").strip()
    if guess in suspects:
        tries = tries + 1
        if guess == culprit:
            print(f"🎉 정답! 범인은 {culprit}이었어요!")
            break
        else:
            print(f"❌ {guess}에게는 알리바이가 있어요.")
    else:
        print("명단에 없는 사람이에요. 다시 골라 주세요.")

print(f"사건 기록: 범인은 {culprit}")

# ===== 2단계 바꾸기 예시 =====
# 내 사건으로 바꾸기, 용의자를 '끝'까지 여러 명 추가(중복 검사), 단서 리스트에서 무작위 단서,
# 이미 조사한 사람 기록, 기회 3번 다 쓰면 정답 공개
print("")
print("🕵️ 미술실 물감 실종 사건 🕵️")
suspects = ["미술부 반장", "청소 당번", "옆 반 학생"]

while True:
    name = input("용의자 추가 (그만하려면 '끝'): ").strip()
    if name == "끝":
        break
    if name in suspects:
        print("이미 명단에 있어요!")
        continue
    suspects.append(name)
    print(f"  현재 명단: {suspects}")

clues = ["바닥에 파란 발자국", "창문이 열려 있음", "물감 묻은 휴지", "급하게 뛰어가는 소리"]
culprit = random.choice(suspects)
print(f"📌 현장 단서: {random.choice(clues)}")

checked = []
tries = 0
solved = False
while tries < 3:
    guess = input(f"[{tries + 1}/3] 범인은? ").strip()
    if guess not in suspects:
        print("명단에 없는 사람이에요.")
        continue
    if guess in checked:
        print("이미 조사한 사람이에요. 다른 사람을 골라요.")
        continue
    checked.append(guess)
    tries = tries + 1
    if guess == culprit:
        solved = True
        break
    print(f"❌ {guess}은(는) 범인이 아니에요. 새 단서: {random.choice(clues)}")

print(f"조사한 사람: {checked}")
if solved:
    print(f"🎉 사건 해결! 범인은 {culprit}!")
else:
    print(f"😢 범인을 놓쳤어요. 진짜 범인은 {culprit}이었어요.")
