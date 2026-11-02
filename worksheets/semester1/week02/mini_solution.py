# 2주 미니 프로젝트: 밸런스 게임 (정답)

# ===== 1단계 따라 하기 완성본 =====
print("⚖️  밸런스 게임을 시작합니다! ⚖️")
print("")

name = input("플레이어 이름: ")

print("")
print("[1번 질문] 평생 한 가지만 먹어야 한다면?")
print("1. 치킨   2. 피자")
answer1 = input("선택 (1 또는 2): ").strip()

if answer1 == "1":
    print("치킨파 " + name + "! 바삭바삭 최고!")
elif answer1 == "2":
    print("피자파 " + name + "! 치즈가 쭈욱~")
else:
    print("앗, 1이나 2만 골라 주세요.")

print("")
print("[2번 질문] 하나만 고른다면?")
print("1. 하늘을 나는 능력   2. 순간 이동 능력")
answer2 = input("선택 (1 또는 2): ").strip()

if answer2 == "1":
    print("구름 위를 날아다니는 " + name + "!")
elif answer2 == "2":
    print("어디든 순식간에! 지각은 이제 없어요.")
else:
    print("앗, 1이나 2만 골라 주세요.")

# ===== 2단계 바꾸기 예시 =====
# 내 질문으로 바꾸고, 선택지를 3개로 늘리고, 고른 것에 따라 칭호를 붙였어요.
print("")
print("[3번 질문] 방학 때 딱 하루를 보낸다면?")
print("1. 바다   2. 놀이공원   3. 집에서 뒹굴")
answer3 = input("선택 (1, 2, 3): ").strip()

if answer3 == "1":
    title = "파도 타는"
    print("파도 소리 들으며 모래성 쌓기!")
elif answer3 == "2":
    title = "롤러코스터 왕"
    print("롤러코스터 세 번 연속 도전!")
elif answer3 == "3":
    title = "이불 속 휴식왕"
    print("이불 밖은 위험해! 최고의 휴식이에요.")
else:
    title = "엉뚱한"
    print("1, 2, 3 중에 골라 주세요.")

print("")
print("오늘의 칭호: [" + title + "] " + name)
print("")
print("게임 끝! " + name + "님의 선택을 친구와 비교해 보세요.")
