# 5주 중간 프로젝트 (확장): 지진 조기 경보 시스템
# 이 코드는 그대로 실행돼요. 지진이 나면 빠르지만 약한 P파가 먼저, 느리지만 강한 S파가
# 나중에 도착해요. 그 시간 차이가 바로 '대피할 수 있는 시간'이에요.
# 1~4주 개념을 모두 섞어 나만의 경보 시스템으로 키워 보세요.

import random

print("🌏 지진 조기 경보 시스템 🌏")

city = input("우리 동네 이름: ")
distance = int(input("진원지까지 거리 (km): "))

# P파는 1초에 약 6km, S파는 1초에 약 3km 간다고 할게요. (단순화)
p_time = distance // 6
s_time = distance // 3
warning_time = s_time - p_time

magnitude = random.randint(3, 7)

print("")
print(f"📈 감지된 지진 규모: {magnitude}")
print(f"P파 도착: {p_time}초 후, S파 도착: {s_time}초 후")
print(f"⏱️ {city}에서 대피할 수 있는 시간: 약 {warning_time}초")

if magnitude >= 5:
    print("🚨 강한 지진! 즉시 대피하세요!")
else:
    print("ℹ️ 약한 지진입니다. 침착하게 상황을 지켜보세요.")
