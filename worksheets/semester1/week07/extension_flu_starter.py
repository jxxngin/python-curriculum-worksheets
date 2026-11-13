# 7주 확장 프로젝트 (택1): 독감 유행 시뮬레이터
# 이 코드는 그대로 실행돼요. 감염자 한 명이 하루에 몇 명에게 옮기는지에 따라
# 독감이 학교에 얼마나 빨리 퍼지는지 하루씩 계산해요.
# 바꾸기부터 시작해서 더 진짜 같은 시뮬레이터로 키워 보세요.

print("🦠 독감 유행 시뮬레이터 🦠")

students = int(input("학교 학생 수: "))
spread = int(input("감염자 한 명이 하루에 옮기는 사람 수 (1 이상): "))

infected = 1     # 처음 감염자
day = 0

while infected < students:
    day = day + 1
    new = infected * spread           # 오늘 새로 감염된 사람
    if infected + new > students:     # 학생 수보다 많이 걸릴 수는 없어요
        new = students - infected
    infected = infected + new         # 누적 감염자
    print(f"{day}일째: 새 감염 {new}명, 누적 {infected}명")

print(f"😷 {day}일 만에 학교 전체가 감염됐어요!")
