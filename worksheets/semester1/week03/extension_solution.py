# 3주 확장 프로젝트: 내가 태어난 요일 계산기 (예시 답안)
# 바꾸기: 요일 7개 모두 출력, 범위를 벗어난 달·날 안내, 주말/평일 판정
# 새로 만들기: 올해 내 생일은 무슨 요일인지도 계산

print("📅 내가 태어난 요일 계산기 📅")

name = input("이름: ")
year = int(input("태어난 해: "))
month = int(input("태어난 달: "))
day = int(input("태어난 날: "))
this_year = int(input("올해는 몇 년? "))

# 달과 날이 범위를 벗어나면 미리 알려 줘요.
if month > 12:
    print("⚠️ 달은 12까지예요. 결과가 이상할 수 있어요.")
if day > 31:
    print("⚠️ 날은 31까지예요. 결과가 이상할 수 있어요.")

# 태어난 날의 요일
y = year
m = month
if m < 3:
    m = m + 12
    y = y - 1
k = y % 100
j = y // 100
h = (day + (13 * (m + 1)) // 5 + k + k // 4 + j // 4 + 5 * j) % 7

if h == 0:
    weekday = "토요일"
elif h == 1:
    weekday = "일요일"
elif h == 2:
    weekday = "월요일"
elif h == 3:
    weekday = "화요일"
elif h == 4:
    weekday = "수요일"
elif h == 5:
    weekday = "목요일"
else:
    weekday = "금요일"

print("")
print(f"{name}님은 {year}년 {month}월 {day}일 {weekday}에 태어났어요!")

if h < 2:
    print("주말에 태어난 여유로운 사람! 🛋️")
else:
    print("평일에 태어난 부지런한 사람! 🏃")

# 새로 만들기: 올해 생일의 요일
y2 = this_year
m2 = month
if m2 < 3:
    m2 = m2 + 12
    y2 = y2 - 1
k2 = y2 % 100
j2 = y2 // 100
h2 = (day + (13 * (m2 + 1)) // 5 + k2 + k2 // 4 + j2 // 4 + 5 * j2) % 7

if h2 == 0:
    weekday2 = "토요일"
elif h2 == 1:
    weekday2 = "일요일"
elif h2 == 2:
    weekday2 = "월요일"
elif h2 == 3:
    weekday2 = "화요일"
elif h2 == 4:
    weekday2 = "수요일"
elif h2 == 5:
    weekday2 = "목요일"
else:
    weekday2 = "금요일"

age = this_year - year
print(f"🎂 {this_year}년 생일({age}번째)은 {weekday2}이에요.")
if h2 < 2:
    print("올해 생일은 주말! 파티하기 딱 좋아요.")
else:
    print("올해 생일은 평일! 학교에서 축하받겠네요.")
