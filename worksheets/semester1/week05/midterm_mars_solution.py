# 5주 중간 프로젝트 (확장): 화성 탐사 미션 센터 (예시 답안)
# 1~4주 개념 모두 사용: input/변수/f-string, if/elif/else, ==, strip(),
# int(), 산술·비교 연산자, %, //, import random, randint, abs()

import random

print("🚀 화성 탐사 미션 센터 🚀")
crew = input("탐사 대장 이름: ").strip()
members = int(input("탐사 대원 수 (대장 포함): "))
mission_score = 100

# ---- 1단계: 비행 계획 ----
distance = random.randint(55, 400) * 1000000
speed = int(input("우주선 속도 (km/일, 예: 2000000): "))
days = distance // speed
weeks = days // 7
rest_days = days % 7

print("")
print(f"📡 화성까지 거리: {distance}km")
print(f"🕒 예상 비행 기간: {days}일 ({weeks}주 {rest_days}일)")

if days > 300:
    print("⚠️ 비행이 너무 길어요. 대원들이 지칠 수 있어요. (-20점)")
    mission_score = mission_score - 20

# ---- 2단계: 산소 보급 ----
oxygen = int(input("실을 산소량 (kg): "))
need = days * members
if oxygen >= need:
    print(f"✅ 산소 충분! ({oxygen - need}kg 남아요)")
else:
    print(f"❌ 산소 부족! {need - oxygen}kg 더 필요해요. (-40점)")
    mission_score = mission_score - 40

# ---- 3단계: 무작위 우주 사건 ----
print("")
event = random.randint(1, 4)
if event == 1:
    print("☄️ 사건: 작은 운석과 충돌! 수리에 성공했지만 점수 -10")
    mission_score = mission_score - 10
elif event == 2:
    print("🌪️ 사건: 화성 모래 폭풍 예보! 착륙 지점을 바꿔야 해요. 점수 -15")
    mission_score = mission_score - 15
elif event == 3:
    print("🛰️ 사건: 지구에서 응원 메시지 도착! 사기 상승 +10")
    mission_score = mission_score + 10
else:
    print("🌌 사건: 아무 일 없이 조용한 항해예요.")

# ---- 4단계: 착륙 (abs로 목표 지점과의 오차) ----
print("")
print("🎯 착륙 목표 지점은 0~100 사이 어딘가! 숫자를 골라 착륙하세요.")
target = random.randint(0, 100)
land = int(input("착륙 좌표: "))
error = abs(land - target)
print(f"목표 좌표: {target}, 오차: {error}")

if error == 0:
    print("🏅 완벽한 착륙! +20점")
    mission_score = mission_score + 20
elif error <= 10:
    print("👍 안전한 착륙!")
elif error <= 30:
    print("😰 거친 착륙... 장비 일부 손상 (-15점)")
    mission_score = mission_score - 15
else:
    print("💥 착륙 실패 위험! 비상 착륙 (-30점)")
    mission_score = mission_score - 30

# ---- 결과 ----
print("")
print("==============================")
print(f"🧑‍🚀 대장 {crew}의 미션 점수: {mission_score}점")
if mission_score >= 90:
    print("평가: 🌟 인류 최초의 영웅!")
elif mission_score >= 60:
    print("평가: ✅ 미션 성공")
else:
    print("평가: 🔁 미션 재도전 필요")
