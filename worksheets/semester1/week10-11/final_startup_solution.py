# 기말 프로젝트 (확장): 청소년 창업 시뮬레이션 — 예시 답안
# 최소 완성 기준: 7일 영업, 돈·평판 수치 2개, 판매 상품 리스트, 무작위 사건 3개, 목표 금액 달성 여부 판정
# 추가 기능: 새 상품 개발(append), 가격에 따른 평판 변화, 최고 매출일 기록

import random
import time

print("🏪 청소년 창업 시뮬레이션 🏪")
shop = input("가게 이름: ").strip()
goal = 100000

money = 10000
reputation = 50                  # 평판 (0~100)
products = ["레모네이드", "쿠키"]
best_day = 0
best_sales = 0
day = 1

print(f"목표: 7일 뒤 {goal}원 모으기!")
time.sleep(1)

while day <= 7:
    print(f"\n☀️ {day}일째 - {shop} / 💰 {money}원 / ⭐ 평판 {reputation}")
    print(f"판매 상품: {products}")

    if money >= 8000 and "아이스티" not in products:
        new = input("8000원으로 '아이스티'를 개발할까요? (네/아니오) ").strip()
        if new == "네":
            money = money - 8000
            products.append("아이스티")
            print("🧊 아이스티가 메뉴에 추가됐어요!")

    item = input("오늘 팔 상품: ").strip()
    if item not in products:
        print("메뉴에 없는 상품이에요. 다시 골라 주세요.")
        continue

    price = int(input(f"{item} 가격(원): "))
    customers = random.randint(3, 8) + reputation // 20
    if item == "아이스티":
        customers = customers + 5

    if price > 3000:
        customers = customers // 2
        reputation = reputation - 5
        print("😒 '너무 비싸요!' 평판 -5")
    elif price <= 1500:
        reputation = reputation + 3
        print("😊 '가성비 최고!' 평판 +3")

    # 무작위 사건 3개
    event = random.randint(1, 5)
    if event == 1:
        print("🌧️ 소나기! 손님이 절반으로 줄었어요.")
        customers = customers // 2
    elif event == 2:
        print("📱 인플루언서가 다녀갔어요! 손님 +10, 평판 +10")
        customers = customers + 10
        reputation = reputation + 10
    elif event == 3:
        print("📈 재료값이 올랐어요. 재료비 +3000원")
        money = money - 3000

    if reputation > 100:
        reputation = 100
    if reputation < 0:
        reputation = 0

    sales = customers * price
    money = money + sales - 5000
    print(f"손님 {customers}명 → 매출 {sales}원 (재료비 5000원)")
    if sales > best_sales:
        best_sales = sales
        best_day = day

    time.sleep(0.5)
    day = day + 1

print("\n📊 7일 영업 결과를 계산하는 중...")
time.sleep(1)
print(f"최종 금액 {money}원 / 평판 {reputation} / 최고 매출 {best_day}일째 {best_sales}원")
if money >= goal:
    print(f"🎉 목표 {goal}원 달성! {shop}는 동네 맛집이 됐어요.")
else:
    print(f"😢 목표까지 {goal - money}원 부족해요. 전략을 바꿔 다시 도전!")
