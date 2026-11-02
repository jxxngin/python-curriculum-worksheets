# 5주 중간 프로젝트 (확장): 지진 조기 경보 시스템 (예시 답안)
# 1~4주 개념 모두 사용: input/변수/f-string, if/elif/else, ==, strip(),
# int(), 산술·비교 연산자, %, //, import random, randint, abs()

import random

print("🌏 지진 조기 경보 시스템 🌏")
city = input("우리 동네 이름: ").strip()
distance = int(input("진원지까지 거리 (km): "))

p_time = distance // 6
s_time = distance // 3
warning_time = s_time - p_time

# 규모 3.0~7.9를 정수 두 개로 표현 (예: 5와 3 → 5.3)
mag_whole = random.randint(3, 7)
mag_point = random.randint(0, 9)
mag_x10 = mag_whole * 10 + mag_point   # 비교하기 쉽게 10배 한 값

print("")
print(f"📈 감지된 지진 규모: {mag_whole}.{mag_point}")
print(f"P파 도착: {p_time}초 후, S파 도착: {s_time}초 후")
print(f"⏱️ {city}에서 대피할 수 있는 시간: 약 {warning_time}초")

if warning_time >= 60:
    print(f"   = {warning_time // 60}분 {warning_time % 60}초")

# 경보 단계 정하기
print("")
if mag_x10 >= 60:
    level = "심각"
    print("🔴 [심각] 강한 흔들림! 즉시 대피하세요!")
elif mag_x10 >= 50:
    level = "경계"
    print("🟠 [경계] 책상 아래로 몸을 숨기세요!")
elif mag_x10 >= 40:
    level = "주의"
    print("🟡 [주의] 흔들림이 느껴질 수 있어요.")
else:
    level = "관심"
    print("🟢 [관심] 대부분 느끼지 못하는 약한 지진이에요.")

# 거리가 가까우면 대피 시간이 거의 없어요
if warning_time < 10:
    print("⚠️ 진원지가 가까워 대피 시간이 매우 짧아요. 가장 가까운 안전한 곳으로!")

# 대피 훈련: 내가 예상한 대피 시간과 실제 경보 시간 비교
print("")
my_time = int(input("우리 집에서 안전한 곳까지 몇 초 걸리나요? "))
gap = abs(warning_time - my_time)
if my_time <= warning_time:
    print(f"✅ 대피 가능! {gap}초 여유가 있어요.")
else:
    print(f"❌ {gap}초 부족해요. 더 가까운 대피 장소를 정해 두세요.")

# 무작위 여진
print("")
aftershock = random.randint(1, 3)
if aftershock == 1:
    print("🔁 여진 예보: 몇 시간 안에 작은 여진이 올 수 있어요.")
else:
    print("🔁 여진 예보: 현재 큰 여진 징후는 없어요.")

print("")
print(f"📋 보고서: {city} / 거리 {distance}km / 규모 {mag_whole}.{mag_point} / 단계 {level}")
