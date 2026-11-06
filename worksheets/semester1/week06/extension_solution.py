# 6주 확장 프로젝트: 자율주행차 판단 AI (예시 답안)
# 바꾸기: 속도·날씨 센서 추가, 판단 4가지(정지/감속/차선 변경/주행), 위험 깃발 여러 개
# 새로 만들기: 무작위 센서 상황 테스트 모드, 사람 판단과 AI 판단 비교

import random

print("🚗 자율주행차 판단 AI 🚗")
mode = input("1. 직접 입력  2. 무작위 테스트 : ").strip()

if mode == "2":
    # 무작위 센서 상황 만들기
    n = random.randint(1, 3)
    if n == 1:
        light = "빨강"
    elif n == 2:
        light = "노랑"
    else:
        light = "초록"
    person_n = random.randint(1, 4)
    person = person_n == 1          # 4번 중 1번꼴로 보행자
    distance = random.randint(2, 60)
    speed = random.randint(20, 90)
    rain_n = random.randint(1, 3)
    rain = rain_n == 1
    side_n = random.randint(1, 2)
    side_clear = side_n == 1
    print(f"📡 센서: 신호 {light}, 보행자 {person}, 앞차 {distance}m, 속도 {speed}km/h, 비 {rain}, 옆 차선 비었음 {side_clear}")
else:
    light = input("신호등 색 (빨강/노랑/초록): ").strip()
    person = input("횡단보도에 사람이 있나요? (네/아니요): ").strip() == "네"
    distance = int(input("앞차와의 거리(m): "))
    speed = int(input("현재 속도(km/h): "))
    rain = input("비가 오나요? (네/아니요): ").strip() == "네"
    side_clear = input("옆 차선이 비어 있나요? (네/아니요): ").strip() == "네"

# 안전거리: 속도의 절반(m). 비가 오면 더 길게.
safe_distance = speed // 2
if rain:
    safe_distance = safe_distance + speed // 4

# 위험 깃발들
too_close = distance < safe_distance
must_stop = light == "빨강" or person
emergency = person and distance < 10

print("")
print(f"📏 필요한 안전거리: {safe_distance}m / 현재 {distance}m")

# AI 판단: 결과는 4가지(정지/감속/차선 변경/주행). 긴급 상황은 정지의 특별 메시지로 보여 준다
if emergency:
    decision = "정지"
    print("🛑 판단: 정지 (🚨 긴급! 보행자 보호가 최우선)")
elif must_stop:
    decision = "정지"
    print("🛑 판단: 정지")
elif too_close:
    if side_clear and not rain:
        decision = "차선 변경"
        print("↔️ 판단: 옆 차선으로 차선 변경")
    else:
        decision = "감속"
        print("🐢 판단: 감속하며 거리 확보")
elif light == "노랑":
    decision = "감속"
    print("⚠️ 판단: 속도를 줄이며 정지 준비")
else:
    decision = "주행"
    print("✅ 판단: 그대로 주행")

# 안전 점수
safety = 100
if too_close:
    safety = safety - 30
if rain:
    safety = safety - 10
if speed > 80:
    safety = safety - 20
print(f"🛡️ 현재 상황 안전 점수: {safety}점")

if not too_close and not rain and speed <= 60:
    print("😊 아주 안전한 상황이에요.")

# 사람 판단과 비교
print("")
print("당신이 운전자라면? (정지/감속/차선 변경/주행)")
human = input("> ").strip()
if human == decision:
    print("🤝 AI와 같은 판단이에요!")
else:
    print(f"🤔 AI의 판단은 '{decision}'이었어요. 누구의 판단이 더 안전할까요?")
