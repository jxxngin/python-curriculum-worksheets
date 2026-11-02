# 5주 중간 프로젝트 (확장): 화성 탐사 미션 센터
# 이 코드는 그대로 실행돼요. 1~4주 개념(입력, 조건, 계산, f-string, random, abs)을
# 모두 섞어서 나만의 미션 센터로 키워 보세요.

import random

print("🚀 화성 탐사 미션 센터 🚀")
crew = input("탐사 대장 이름: ")

# 지구와 화성 사이 거리는 약 5,500만 km ~ 4억 km로 계속 바뀌어요.
distance = random.randint(55, 400) * 1000000
speed = int(input("우주선 속도 (km/일, 예: 2000000): "))

days = distance // speed
print("")
print(f"📡 이번 발사 때 화성까지 거리: {distance}km")
print(f"🕒 예상 비행 기간: {days}일")

# 우주 비행사 한 명이 하루에 쓰는 산소는 약 1kg
oxygen = int(input("실을 산소량 (kg): "))
need = days * 1

if oxygen >= need:
    print(f"✅ 산소 충분! ({oxygen - need}kg 남아요)")
else:
    print(f"❌ 산소 부족! {need - oxygen}kg 더 필요해요.")
