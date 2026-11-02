# 4주 확장 프로젝트: 피자 가성비 계산기
# 이 코드는 그대로 실행돼요. 피자 두 판의 크기와 가격으로 어느 쪽이 이득인지 계산해요.
# 바꾸기부터 시작해서 나만의 가성비 계산기로 키워 보세요.

import math

print("🍕 피자 가성비 계산기 🍕")

size_a = int(input("A 피자 지름(cm): "))
price_a = int(input("A 피자 가격(원): "))
size_b = int(input("B 피자 지름(cm): "))
price_b = int(input("B 피자 가격(원): "))

# 원의 넓이 = 원주율 × 반지름 × 반지름
radius_a = size_a / 2
area_a = math.pi * pow(radius_a, 2)
radius_b = size_b / 2
area_b = math.pi * pow(radius_b, 2)

# 1cm²당 가격 (소수 첫째 자리까지 반올림)
per_a = round(price_a / area_a, 1)
per_b = round(price_b / area_b, 1)

print("")
print(f"A 피자: 넓이 {round(area_a)}cm², 1cm²당 {per_a}원")
print(f"B 피자: 넓이 {round(area_b)}cm², 1cm²당 {per_b}원")

if per_a < per_b:
    print("👉 A 피자가 더 이득이에요!")
elif per_b < per_a:
    print("👉 B 피자가 더 이득이에요!")
else:
    print("👉 가성비가 똑같아요!")
