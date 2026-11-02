# 8주 확장 프로젝트: 이상형 월드컵
# 이 코드는 그대로 실행돼요. 후보 8개 중 둘씩 짝지어 더 좋은 쪽을 고르면,
# 이긴 후보가 새 리스트(winners)에 append() 돼요. 지금은 8강까지만 해요.
# 바꾸기부터 시작해서 우승자가 나올 때까지 이어지는 진짜 월드컵으로 키워 보세요.

print("🏆 급식 메뉴 이상형 월드컵 🏆")

candidates = ["떡볶이", "돈가스", "카레", "짜장면", "치킨", "김치볶음밥", "스파게티", "비빔밥"]
size = 8          # 후보 수 (리스트 길이를 세는 법은 2학기에 배워요)

winners = []      # 이긴 후보를 담을 빈 리스트
i = 0             # 지금 비교할 첫 번째 후보의 칸 번호
while i < size:
    left = candidates[i]
    right = candidates[i + 1]
    print(f"\n1번 {left}  VS  2번 {right}")
    pick = input("더 좋은 쪽 번호(1/2): ").strip()
    if pick == "1":
        winners.append(left)
    else:
        winners.append(right)
    i = i + 2     # 다음 짝으로 두 칸 이동

print(f"\n✨ 4강 진출: {winners}")
