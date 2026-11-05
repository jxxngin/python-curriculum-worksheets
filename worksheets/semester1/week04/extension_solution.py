# 4주 확장 프로젝트: 피자 가성비 계산기 (예시 답안)
# 바꾸기: 피자 이름 입력, max()로 더 큰 피자 찾기, 1인당 넓이 계산
# 새로 만들기: 오늘의 할인 쿠폰(random), 두 피자의 가격 차이(abs())

import math
import random

print("🍕 피자 가성비 계산기 🍕")

name_a = input("A 피자 이름: ")
size_a = int(input(f"{name_a} 지름(cm): "))
price_a = int(input(f"{name_a} 가격(원): "))
name_b = input("B 피자 이름: ")
size_b = int(input(f"{name_b} 지름(cm): "))
price_b = int(input(f"{name_b} 가격(원): "))
people = int(input("먹을 사람 수: "))

# 새로 만들기: 오늘의 할인 쿠폰 (10%, 20%, 30% 중 무작위, A 피자에만 적용)
coupon = random.randint(1, 3) * 10
print("")
print(f"🎟️ 오늘의 쿠폰: {name_a} {coupon}% 할인!")
price_a = price_a - price_a * coupon // 100
print(f"   할인된 {name_a} 가격: {price_a}원")

area_a = math.pi * pow(size_a / 2, 2)
area_b = math.pi * pow(size_b / 2, 2)

per_a = round(price_a / area_a, 1)
per_b = round(price_b / area_b, 1)

print("")
print(f"{name_a}: 넓이 {round(area_a)}cm², 1cm²당 {per_a}원")
print(f"{name_b}: 넓이 {round(area_b)}cm², 1cm²당 {per_b}원")

# max()로 더 넓은 피자의 넓이 찾기
biggest = max(area_a, area_b)
if biggest == area_a:
    print(f"📏 더 큰 피자는 {name_a} ({round(biggest)}cm²)")
else:
    print(f"📏 더 큰 피자는 {name_b} ({round(biggest)}cm²)")

# abs()로 두 피자의 가격 차이
diff = abs(price_a - price_b)
print(f"💸 두 피자의 가격 차이: {diff}원")

print("")
if per_a < per_b:
    print(f"👉 이득인 피자: {name_a}")
    best_area = area_a
elif per_b < per_a:
    print(f"👉 이득인 피자: {name_b}")
    best_area = area_b
else:
    print("👉 가성비가 똑같아요!")
    best_area = area_a

print(f"🍽️ 이득인 피자를 {people}명이 나누면 한 사람당 약 {round(best_area / people)}cm²")

# 지름이 2배면 넓이는 몇 배? (pow로 확인)
print(f"🔍 참고: 지름이 2배가 되면 넓이는 {pow(2, 2)}배가 돼요!")
