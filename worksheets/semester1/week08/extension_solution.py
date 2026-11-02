# 8주 확장 프로젝트: 이상형 월드컵 (예시 답안)
# 바꾸기: 우승자까지 반복(8강→4강→결승), 라운드 이름, 잘못된 입력 다시 받기, shuffle()로 대진 섞기
# 새로 만들기: 탈락자 명단, 컴퓨터 대신 고르기('?' 입력 → random.choice)

import random

print("🏆 여름 방학 여행지 이상형 월드컵 🏆")

candidates = ["제주도", "부산 바다", "강릉", "경주", "설악산", "전주 한옥마을", "남해", "놀이공원"]
size = 8
random.shuffle(candidates)        # 보너스: 대진표를 무작위로 섞기
print(f"오늘의 대진: {candidates}")

losers = []
while size > 1:
    if size == 8:
        print("\n===== 🔥 8강 =====")
    elif size == 4:
        print("\n===== ⚡ 4강 =====")
    else:
        print("\n===== 👑 결승 =====")

    winners = []
    i = 0
    while i < size:
        left = candidates[i]
        right = candidates[i + 1]
        print(f"1번 {left}  VS  2번 {right}")
        pick = input("더 좋은 쪽 번호(1/2, 고민되면 ?): ").strip()
        if pick == "?":
            choice = random.choice([left, right])
            print(f"  🎲 컴퓨터가 {choice}을(를) 골랐어요!")
        elif pick == "1":
            choice = left
        elif pick == "2":
            choice = right
        else:
            print("  1이나 2(또는 ?)를 입력해 주세요.")
            continue            # i를 바꾸지 않았으니 같은 대결을 다시 해요
        winners.append(choice)
        if choice == left:
            losers.append(right)
        else:
            losers.append(left)
        i = i + 2

    candidates = winners        # 이긴 후보만 다음 라운드로
    size = size // 2

champion = candidates[0]
print(f"\n🎉 최종 우승: {champion}!")
print(f"아쉽게 탈락: {losers}")
if "제주도" in losers:
    print("제주도를 떨어뜨리다니, 진짜 취향 확실하네요! 😎")
