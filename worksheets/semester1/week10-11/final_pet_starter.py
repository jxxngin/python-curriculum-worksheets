# 기말 프로젝트 (미니): 펫과 함께하는 하루 — 시작 코드
# 이 코드는 그대로 실행돼요. 지금은 '밥 주기' 행동만 있어요.
# 최소 완성 기준까지 키워 보세요!
#   [ ] 10턴
#   [ ] 행동 3개 (밥, 놀기, 재우기)
#   [ ] 배고픔·기분 수치 2개
#   [ ] 마지막에 행복도로 성공·실패 판정

import time

pet = input("펫 이름을 지어 주세요: ").strip()
print(f"🐾 {pet}와(과) 함께하는 하루가 시작됐어요!")

hunger = 5      # 배고픔 (0~10, 높을수록 배고파요)
mood = 5        # 기분 (0~10, 높을수록 좋아요)
turn = 1

while turn <= 10:
    print(f"\n[{turn}턴] 배고픔 {hunger} / 기분 {mood}")
    action = input("1. 밥 주기 > ").strip()
    if action == "1":
        hunger = hunger - 3
        print(f"냠냠! {pet}가 밥을 먹었어요.")
    # TODO: 2. 놀기, 3. 재우기 행동 추가
    # TODO: 수치가 0보다 작거나 10보다 커지지 않게 막기
    hunger = hunger + 1          # 시간이 지나면 배가 고파져요
    time.sleep(0.5)
    turn = turn + 1

# TODO: 행복도를 계산해서 성공/실패 판정
print(f"\n하루 끝! 배고픔 {hunger} / 기분 {mood}")
