# 기말 프로젝트 (확장): 청소년 창업 시뮬레이션 — 시작 코드
# 이 코드는 그대로 실행돼요. 지금은 '상품 하나를 7일 동안 파는 것'만 있어요.
# 최소 완성 기준까지 키워 보세요!
#   [ ] 7일 영업
#   [ ] 돈·평판 수치 2개
#   [ ] 판매 상품 리스트 (고를 수 있고, 새 상품을 추가할 수 있게)
#   [ ] 무작위 사건 3개
#   [ ] 마지막에 목표 금액 달성 여부 판정

import random
import time

print("🏪 청소년 창업 시뮬레이션 🏪")
shop = input("가게 이름: ").strip()

money = 10000        # 가진 돈
products = ["레모네이드"]
day = 1

while day <= 7:
    print(f"\n☀️ {day}일째 - {shop} / 돈 {money}원")
    print(f"판매 상품: {products}")
    price = int(input("오늘 레모네이드 가격(원): "))
    customers = random.randint(5, 15)
    if price > 2000:                  # 너무 비싸면 손님이 줄어요
        customers = customers // 2
    sales = customers * price
    money = money + sales - 5000      # 재료비 5000원
    print(f"손님 {customers}명, 매출 {sales}원 (재료비 5000원)")
    time.sleep(0.5)
    day = day + 1

# TODO: 평판 수치, 상품 고르기·추가, 무작위 사건 3개, 목표 금액 판정
print(f"\n7일 영업 끝! 최종 금액: {money}원")
