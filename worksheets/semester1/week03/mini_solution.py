# 3주 미니 프로젝트: 인생 숫자 계산기 (정답)

# ===== 1단계 따라 하기 완성본 =====
print("🔢 인생 숫자 계산기 🔢")
print("")

name = input("이름: ")
birth_year = int(input("태어난 해 (예: 2014): "))
birth_month = int(input("태어난 달 (1~12): "))
birth_day = int(input("태어난 날 (1~31): "))
this_year = int(input("올해는 몇 년? "))

age = this_year - birth_year
days = age * 365
hours = days * 24
heartbeats = days * 24 * 60 * 80

print("")
print(f"{name}님은 올해 {age}살이에요.")
print(f"지금까지 약 {days}일, {hours}시간을 살았어요.")
print(f"심장은 약 {heartbeats}번 뛰었어요! 💓")

life_number = (birth_year + birth_month + birth_day) % 9 + 1
print("")
print(f"✨ {name}님의 인생 숫자는 {life_number}!")

# ===== 2단계 바꾸기 예시 =====
# 인생 숫자 뜻을 9개 모두 지었어요.
if life_number == 1:
    print("앞장서는 리더의 숫자예요.")
elif life_number == 2:
    print("친구를 잘 도와주는 숫자예요.")
elif life_number == 3:
    print("재미있는 아이디어가 넘치는 숫자예요.")
elif life_number == 4:
    print("차근차근 쌓아 올리는 성실한 숫자예요.")
elif life_number == 5:
    print("새로운 곳을 좋아하는 모험가의 숫자예요.")
elif life_number == 6:
    print("모두를 챙기는 따뜻한 숫자예요.")
elif life_number == 7:
    print("궁금한 건 끝까지 파고드는 탐구자의 숫자예요.")
elif life_number == 8:
    print("목표를 꼭 이루는 끈기의 숫자예요.")
else:
    print("마음이 넓은 평화주의자의 숫자예요.")

# 잠, 밥, 웃음 횟수를 계산해서 추가했어요.
sleep_hours = days * 9
meals = days * 3
print("")
print(f"😴 잠잔 시간: 약 {sleep_hours}시간 (하루 9시간이라면)")
print(f"🍚 먹은 끼니: 약 {meals}끼")
print(f"📅 {age}살은 {age // 10}번의 10년과 {age % 10}년이에요.")

# 비교 연산자로 나이 구간 알려 주기
if age < 13:
    print("초등학생 나이대예요!")
elif age < 16:
    print("중학생 나이대예요!")
else:
    print("고등학생 이상 나이대예요!")

# 새로 만들기 예시: 100살까지 남은 날
left = (100 - age) * 365
print(f"🎂 100살이 되려면 약 {left}일 남았어요.")
