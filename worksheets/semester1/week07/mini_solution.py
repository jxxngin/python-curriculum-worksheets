# 7주 미니 프로젝트: 편의점 키오스크 (정답)

# ===== 1단계 따라 하기 완성본 =====
print("🏪 반짝 편의점 키오스크 🏪")
print("1. 삼각김밥  1200원")
print("2. 바나나우유 1500원")
print("3. 컵라면    1800원")
print("0. 주문 끝내기")

total = 0
items = 0

while True:
    menu = input("메뉴 번호: ").strip()

    if menu == "0":
        break
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
        continue

    total = total + price
    items = items + 1
    print(f"🛒 {name} 담았어요! (현재 {items}개, {total}원)")

print("")
print(f"🧾 총 {items}개, 결제 금액은 {total}원입니다. 감사합니다!")

# ===== 2단계 바꾸기 예시 =====
# 수량 입력, 메뉴 추가, 1만 원 이상 10% 할인, 돈 내고 거스름돈 받기(돈이 모자라면 다시 받기)
print("")
print("===== 💳 새 키오스크 =====")
print("1. 삼각김밥 1200원  2. 바나나우유 1500원  3. 컵라면 1800원")
print("4. 아이스크림 1000원  5. 도시락 4500원  0. 주문 끝")

total = 0
items = 0
while True:
    menu = input("메뉴 번호: ").strip()
    if menu == "0":
        break
    elif menu == "1":
        price = 1200
    elif menu == "2":
        price = 1500
    elif menu == "3":
        price = 1800
    elif menu == "4":
        price = 1000
    elif menu == "5":
        price = 4500
    else:
        print("없는 번호예요.")
        continue

    count = int(input("몇 개? "))
    if count <= 0:
        print("1개 이상 골라 주세요.")
        continue
    total = total + price * count
    items = items + count
    print(f"   현재 {items}개, {total}원")

if total >= 10000:
    discount = total // 10
    total = total - discount
    print(f"🎉 1만 원 이상! {discount}원 할인")

print(f"결제할 금액: {total}원")

paid = 0
while paid < total:
    money = int(input(f"넣을 돈 (지금까지 {paid}원): "))
    paid = paid + money

print(f"💰 거스름돈: {paid - total}원")
print("영수증을 가져가세요. 또 오세요! 👋")
