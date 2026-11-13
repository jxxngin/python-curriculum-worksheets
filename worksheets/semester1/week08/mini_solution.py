# 8주 미니 프로젝트: 탐정의 용의자 명단 (정답)
# 교안의 단계 순서대로 이어 쓴 완성본이에요.

# 단계 1: 용의자 명단 만들기
print("사라진 생일 케이크 사건")
suspects = ["옆집 고양이", "배고픈 동생", "택배 기사님"]
print(f"용의자 명단: {suspects}")
print(f"가장 먼저 의심받는 사람: {suspects[0]}")

# 단계 2: 수상한 사람 더하기
new = input("수상한 사람을 한 명 더 적어 주세요: ").strip()
suspects.append(new)
print(f"새 명단: {suspects}")

# 단계 3: 범인 몰래 뽑기
import random
culprit = random.choice(suspects)
tries = 0
print("범인이 정해졌어요. 기회는 3번!")

# 단계 4: 명단에 있는 사람만 조사하기
while tries < 3:
    guess = input("범인은 누구일까요? ").strip()
    if guess not in suspects:
        print("명단에 없는 사람이에요.")
        continue
    tries = tries + 1

# 단계 5: 범인 판정하기
    if guess == culprit:
        print("정답! 범인을 찾았어요.")
        break
    print(f"{guess}: 알리바이가 있어요.")
print(f"사건 기록: 범인은 {culprit}")

# ----- 바꾸기 예시 (선생님용). 주석을 풀어 표시한 자리에 넣으면 실행돼요 -----
# # [용의자 여러 명] 단계 2의 세 줄을 아래로 바꾸기:
# while True:
#     new = input("용의자 추가 (그만하려면 끝): ").strip()
#     if new == "끝":
#         break
#     if new in suspects:
#         print("이미 명단에 있어요.")
#         continue
#     suspects.append(new)
# print(f"새 명단: {suspects}")
# # [단서] 단계 3의 culprit 줄 아래에:
# clues = ["바닥에 파란 발자국", "열려 있는 창문", "물감 묻은 휴지"]
# # 단계 5의 알리바이 줄 아래에:
#     print(f"새 단서: {random.choice(clues)}")
