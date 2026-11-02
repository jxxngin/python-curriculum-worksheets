# 7주 미니 프로젝트: 편의점 키오스크
# 빈칸(___)을 채워서 계속 주문을 받는 키오스크를 완성해 보세요.

print("🏪 반짝 편의점 키오스크 🏪")
print("1. 삼각김밥  1200원")
print("2. 바나나우유 1500원")
print("3. 컵라면    1800원")
print("0. 주문 끝내기")

total = 0       # 누적 변수: 지금까지 쌓인 금액
items = 0       # 누적 변수: 지금까지 고른 개수

# 빈칸 1: 조건이 참인 동안 계속 반복하는 키워드예요. (True면 영원히 반복!)
___ True:
    menu = input("메뉴 번호: ").strip()

    if menu == "0":
        # 빈칸 2: 반복문을 바로 빠져나가는 키워드예요.
        ___
    elif menu == "1":
        price = 1200
        name = "삼각김밥"
    elif menu == "2":
        price = 1500
        name = "바나나우유"
    elif menu == "3":
        price = 1800
        name = "컵라면"
    else:
        print("없는 번호예요. 다시 골라 주세요.")
        # 빈칸 3: 아래 코드를 건너뛰고 반복의 처음으로 돌아가는 키워드예요.
        ___

    # 빈칸 4: 지금까지의 금액(total)에 이번 가격(price)을 더해 쌓아요.
    total = ___ + price
    items = items + 1
    print(f"🛒 {name} 담았어요! (현재 {items}개, {total}원)")

print("")
print(f"🧾 총 {items}개, 결제 금액은 {total}원입니다. 감사합니다!")
