# 2주 미니 프로젝트: 밸런스 게임 (정답)
# 교안의 단계 순서대로 이어 쓴 완성본이에요.

# 단계 1: 첫 번째 질문 보여 주기
print("밸런스 게임을 시작합니다!")
name = input("플레이어 이름: ")
print("[1번 질문] 평생 한 가지만 먹어야 한다면?")
print("1. 치킨   2. 피자")
answer1 = input("선택 (1 또는 2): ").strip()

# 단계 2: 고른 답에 따라 다른 말 하기
if answer1 == "1":
    print("치킨파 " + name + "! 바삭바삭 최고!")
elif answer1 == "2":
    print("피자파 " + name + "! 치즈가 쭈욱~")
else:
    print("1이나 2만 골라 주세요.")

# 단계 3: 두 번째 질문 보여 주기
print("")
print("[2번 질문] 하나만 고른다면?")
print("1. 하늘을 나는 능력   2. 순간 이동 능력")
answer2 = input("선택 (1 또는 2): ").strip()

# 단계 4: 오늘의 칭호 붙여 주기
title = "엉뚱한"
if answer2 == "1":
    title = "구름 위를 나는"
elif answer2 == "2":
    title = "순간 이동하는"
print("오늘의 칭호: [" + title + "] " + name)

# ----- 바꾸기 예시 (선생님용, 주석을 풀면 실행돼요) -----
# print("[3번 질문] 방학 때 딱 하루를 보낸다면?")
# print("1. 바다   2. 놀이공원   3. 집")
# answer3 = input("선택 (1, 2, 3): ").strip()
# if answer3 == "1":
#     print("모래성 쌓기")
# elif answer3 == "2":
#     print("롤러코스터 세 번")
# elif answer3 == "3":
#     print("집에서 쉬기")
# else:
#     print("1, 2, 3 중에 골라 주세요.")
