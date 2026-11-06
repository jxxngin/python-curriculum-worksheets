# 6주 미니 프로젝트: 놀이공원 입장 판정기 (정답)
# 교안의 단계 순서대로 이어 쓴 완성본이에요.

# 단계 1: 손님 정보 물어보기
print("꿈나라 놀이공원 탑승 판정기")
name = input("이름: ")
age = int(input("나이 (숫자만): "))
height = int(input("키 cm (숫자만): "))
ticket = input("자유이용권이 있나요? (네/아니요): ").strip()

# 단계 2: 바이킹: 두 조건이 모두 맞아야 탄다
if height >= 120 and age >= 10:
    print("[바이킹] 탑승 가능!")
else:
    print("[바이킹] 키 120cm 이상, 10살 이상이어야 해요.")

# 단계 3: 범퍼카: 하나만 맞아도 탄다
with_parent = input("보호자와 함께 왔나요? (네/아니요): ").strip()
if age >= 10 or with_parent == "네":
    print("[범퍼카] 탑승 가능!")
else:
    print("[범퍼카] 10살 미만은 보호자와 함께 타요.")

# 단계 4: 롤러코스터: 깃발로 판정하기
can_ride = True
if height < 130:
    can_ride = False
if age < 12:
    can_ride = False
print(f"[롤러코스터] 탈 수 있나요? {can_ride}")

# 단계 5: 유령의 집: if 안에 if
if ticket == "네":
    if age >= 9:
        print("[유령의 집] 입장 가능! 무서워도 울지 않기!")
    else:
        print("[유령의 집] 9살 이상만 들어갈 수 있어요.")
else:
    print("[유령의 집] 자유이용권이 필요해요.")

# ----- 바꾸기 예시 (선생님용). 주석을 풀어 맨 아래에 이어서 넣으면 실행돼요 -----
# if not can_ride:
#     print("[롤러코스터] 키 130cm, 12살이 되면 다시 와요.")
# if height >= 140 and age >= 12:
#     print("[자이로드롭] 탑승 가능!")
# else:
#     print("[자이로드롭] 키 140cm 이상, 12살 이상이어야 해요.")
