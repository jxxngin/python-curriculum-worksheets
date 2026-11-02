# 7주 확장 프로젝트 (택1): 독감 유행 시뮬레이터 (예시 답안)
# 바꾸기: 예방 접종률, 회복(완치), 마스크 정책, 최대 30일
# 새로 만들기: 매일 무작위 변화, 가장 많이 아팠던 날 기록, 결과 평가

import random

print("🦠 독감 유행 시뮬레이터 🦠")
students = int(input("학교 학생 수: "))
vaccine = int(input("예방 접종률 (0~100%): "))
mask = input("마스크 쓰기 정책을 할까요? (네/아니요): ").strip() == "네"

# 접종한 학생은 걸리지 않는다고 단순화
can_get = students - students * vaccine // 100
print(f"💉 접종하지 않은 학생: {can_get}명")

sick = 1            # 지금 아픈 사람
recovered = 0       # 다 나은 사람 (다시 걸리지 않음)
total_sick = 1      # 지금까지 한 번이라도 걸린 사람 (누적)
day = 0
peak = 1
peak_day = 0

while day < 30:
    day = day + 1

    # 오늘 옮기는 정도: 기본 1~3명, 마스크를 쓰면 줄어듦
    spread = random.randint(1, 3)
    if mask:
        spread = spread - 1

    # 아직 안 걸린 사람 수만큼만 새로 걸릴 수 있어요
    healthy = can_get - total_sick
    new = sick * spread
    if new > healthy:
        new = healthy

    # 3명 중 1명꼴로 회복 (아픈 사람의 1/3)
    heal = sick // 3

    sick = sick + new - heal
    recovered = recovered + heal
    total_sick = total_sick + new

    if sick > peak:
        peak = sick
        peak_day = day

    print(f"{day}일째: 새 감염 {new}명 | 아픈 사람 {sick}명 | 회복 {recovered}명")

    if sick == 0:
        print("🎉 아픈 사람이 한 명도 없어요! 유행이 끝났어요.")
        break

print("")
print("📊 결과 보고서")
print(f"  지금까지 걸린 사람: {total_sick}명 / 전체 {students}명")
print(f"  가장 많이 아팠던 날: {peak_day}일째 ({peak}명)")
rate = total_sick * 100 // students
print(f"  감염률: {rate}%")
if rate < 20:
    print("  평가: 🟢 잘 막아 냈어요!")
elif rate < 50:
    print("  평가: 🟡 조금 더 조심해야 해요.")
else:
    print("  평가: 🔴 대유행! 예방 접종과 마스크가 필요해요.")
