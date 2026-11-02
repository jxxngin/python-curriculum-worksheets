# 6주 확장 프로젝트: 자율주행차 판단 AI
# 이 코드는 그대로 실행돼요. 센서 정보를 보고 자동차가 어떻게 움직일지 판단해요.
# and/or/not, 중첩 if, 깃발 변수를 써서 더 똑똑한 AI로 키워 보세요.

print("🚗 자율주행차 판단 AI 🚗")

light = input("신호등 색 (빨강/노랑/초록): ").strip()
person = input("횡단보도에 사람이 있나요? (네/아니요): ").strip()
distance = int(input("앞차와의 거리(m): "))

danger = False
if person == "네":
    danger = True
if distance < 10:
    danger = True

print("")
if light == "빨강" or danger:
    print("🛑 판단: 정지")
elif light == "노랑":
    print("⚠️ 판단: 속도를 줄이며 정지 준비")
else:
    print("✅ 판단: 출발")
