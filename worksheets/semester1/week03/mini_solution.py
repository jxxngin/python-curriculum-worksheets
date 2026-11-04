# 3주 미니 프로젝트: 인생 숫자 계산기 (정답)
# 교안의 단계 순서대로 이어 쓴 완성본이에요.

# 단계 1: 나이 계산하기
print("🔢 인생 숫자 계산기 🔢")
name = input("이름: ")
birth_year = int(input("태어난 해 (예: 2015): "))
this_year = int(input("올해는 몇 년? "))
age = this_year - birth_year
print(f"{name}님은 올해 {age}번째 생일을 맞아요.")

# 단계 2: 살아온 날과 시간 계산하기
days = age * 365
hours = days * 24
heartbeats = hours * 60 * 80
print(f"지금까지 약 {days}일, {hours}시간을 살았어요.")
print(f"심장은 약 {heartbeats}번 뛰었어요! 💓")

# 단계 3: 인생 숫자 뽑기
birth_month = int(input("태어난 달 (1~12): "))
birth_day = int(input("태어난 날 (1~31): "))
life_number = (birth_year + birth_month + birth_day) % 9 + 1
print(f"✨ {name}님의 인생 숫자는 {life_number}!")

# 단계 4: 인생 숫자 뜻 알려 주기
if life_number <= 3:
    print("🔥 앞장서는 리더 타입!")
elif life_number <= 6:
    print("🤝 친구를 잘 챙기는 타입!")
else:
    print("🔍 끝까지 파고드는 탐구자 타입!")

# ----- 바꾸기 예시 (선생님용, 주석을 풀면 실행돼요) -----
# meals = days * 3
# print(f"🍚 먹은 끼니: 약 {meals}끼")
# print(f"📅 {age}년은 {age // 10}번의 10년과 {age % 10}년이에요.")
