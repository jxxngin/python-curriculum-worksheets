# 7주 미니 프로젝트: 편의점 키오스크 (정답)
# 교안의 단계 순서대로 이어 쓴 완성본이에요.

# 단계 1: 메뉴판 보여 주기
print("반짝 편의점 키오스크")
print("1. 삼각김밥 1200원")
print("2. 바나나우유 1500원")
print("3. 컵라면 1800원")

# 단계 2: 0을 넣을 때까지 계속 묻기
total = 0
while True:
    menu = input("메뉴 번호 (끝내려면 0): ").strip()
    if menu == "0":
        break

# 단계 3: 없는 번호 건너뛰기
    if menu != "1" and menu != "2" and menu != "3":
        print("없는 번호예요. 다시 골라 주세요.")
        continue

# 단계 4: 메뉴마다 가격 정하기
    price = 1200
    if menu == "2":
        price = 1500
    elif menu == "3":
        price = 1800
    print(f"{price}원을 담았어요.")

# 단계 5: 합계 쌓고 결제 금액 보여 주기
    total = total + price
    print(f"합계: {total}원")
print(f"결제할 금액: {total}원")
print("감사합니다!")

# ----- 바꾸기 예시 (선생님용). 주석을 풀어 표시한 자리에 넣으면 실행돼요 -----
# # [메뉴 더하기] 단계 3 조건 끝에 and menu != "4" 를 더하고, 단계 4의 elif 아래에:
#     elif menu == "4":
#         price = 3000
# # [개수] 단계 5의 total = total + price 줄을 아래 두 줄로 바꾸기:
#     count = int(input("몇 개? (숫자만): "))
#     total = total + price * count
# # [거스름돈] 맨 아래에 이어서:
# paid = 0
# while paid < total:
#     money = int(input(f"넣을 돈 (지금까지 {paid}원): "))
#     paid = paid + money
# print(f"거스름돈: {paid - total}원")
