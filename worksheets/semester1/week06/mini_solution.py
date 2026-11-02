# 6주 미니 프로젝트: 놀이공원 입장 판정기 (정답)

# ===== 1단계 따라 하기 완성본 =====
print("🎢 꿈나라 놀이공원 탑승 판정기 🎢")
name = input("이름: ")
age = int(input("나이: "))
height = int(input("키(cm): "))
ticket = input("자유이용권이 있나요? (네/아니요): ").strip()

print("")
print("[회전목마]")
if age <= 7:
    print("보호자와 함께 타요. 🐴")
else:
    print("혼자 탈 수 있어요! 🐴")

print("[바이킹]")
if height >= 120 and age >= 10:
    print("탑승 가능! ⛵")
else:
    print("아직은 탈 수 없어요.")

print("[롤러코스터]")
can_ride = True
if height < 130:
    print("키가 130cm 이상이어야 해요.")
    can_ride = False
if age < 12:
    print("12살 이상이어야 해요.")
    can_ride = False
if can_ride:
    print("탑승 가능! 🎢 소리 질러~")

print("[유령의 집]")
if ticket == "네":
    if age >= 9:
        print("입장 가능! 👻 무서워도 울지 않기!")
    else:
        print("9살 이상만 들어갈 수 있어요.")
else:
    print("자유이용권이 필요해요. 🎫")

# ===== 2단계 바꾸기 예시 =====
# 새 놀이기구 2개, or와 not 사용, 탈 수 있는 기구 수 세기
print("")
print("--- 새 놀이기구 ---")
heart = input("심장이 약하거나 임산부인가요? (네/아니요): ").strip()
with_parent = input("보호자와 함께 왔나요? (네/아니요): ").strip()
count = 0

# 자이로드롭: 키 140 이상, 심장 질환이 없어야 함 (not 사용)
print("[자이로드롭]")
is_weak = heart == "네"
if height >= 140 and not is_weak:
    print("탑승 가능! 🗼 하늘 끝까지!")
    count = count + 1
else:
    print("안전을 위해 탈 수 없어요.")

# 범퍼카: 10살 이상이거나 보호자와 함께면 OK (or 사용)
print("[범퍼카]")
if age >= 10 or with_parent == "네":
    print("탑승 가능! 🚗 쿵쿵!")
    count = count + 1
else:
    print("10살 미만은 보호자와 함께 와야 해요.")

if height >= 120 and age >= 10:
    count = count + 1
if can_ride:
    count = count + 1

print("")
print(f"🎟️ {name}님이 탈 수 있는 스릴 기구: {count}개 (바이킹·롤러코스터·자이로드롭·범퍼카 중)")

# 새로 만들기: 오늘의 VIP 판정 (중첩 if + 깃발)
vip = False
if ticket == "네":
    if count >= 3:
        vip = True
if vip:
    print("👑 오늘의 VIP! 줄 서기 없이 바로 탑승하세요.")
