# 3주 미니 프로젝트: 인생 숫자 계산기
# 빈칸(___)을 채워서 내가 살아온 시간을 숫자로 계산해 보세요.

print("🔢 인생 숫자 계산기 🔢")
print("")

name = input("이름: ")
# 빈칸 1: 글자로 들어온 값을 정수(숫자)로 바꿔 주는 함수예요.
birth_year = ___(input("태어난 해 (예: 2014): "))
birth_month = int(input("태어난 달 (1~12): "))
birth_day = int(input("태어난 날 (1~31): "))
this_year = int(input("올해는 몇 년? "))

# 빈칸 2: 올해에서 태어난 해를 빼면 나이가 나와요. 알맞은 변수를 넣어 보세요.
age = this_year - ___
days = age * 365
hours = days * 24
# 빈칸 3: 심장은 1분에 약 80번 뛰어요. 하루는 몇 분일까요? (24 * 60)
heartbeats = days * 24 * ___ * 80

print("")
# 빈칸 4: 문자열 따옴표 앞에 이 글자를 붙이면 {} 안에 변수를 넣을 수 있어요.
print(___"{name}님은 올해 {age}살이에요.")
print(f"지금까지 약 {days}일, {hours}시간을 살았어요.")
print(f"심장은 약 {heartbeats}번 뛰었어요! 💓")

# 인생 숫자: 태어난 해 + 달 + 날을 9로 나눈 나머지에 1을 더해요. (1~9)
# 빈칸 5: 나눗셈의 나머지를 구하는 기호예요.
life_number = (birth_year + birth_month + birth_day) ___ 9 + 1
print("")
print(f"✨ {name}님의 인생 숫자는 {life_number}!")

if life_number == 1:
    print("앞장서는 리더의 숫자예요.")
elif life_number == 2:
    print("친구를 잘 도와주는 숫자예요.")
elif life_number == 3:
    print("재미있는 아이디어가 넘치는 숫자예요.")
else:
    print("아직 뜻이 정해지지 않은 숫자! 직접 뜻을 지어 보세요.")
