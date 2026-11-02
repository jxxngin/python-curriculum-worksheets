# 1주 확장 프로젝트: RPG 파티원 모집 퀘스트 창 (예시 답안)
# 바꾸기: 레벨 조건, 보상, 집합 장소, 파티장 한마디 추가
# 새로 만들기: 지원자 입력을 받아 "파티 합류 메시지"까지 출력

print("+===================================+")
print("|        ⚔  파티원 모집 게시판  ⚔        |")
print("+===================================+")

# 파티장 정보
leader = input("파티장 닉네임: ")
leader_job = input("파티장 직업: ")
quest = input("도전할 퀘스트 이름: ")

# 모집 조건
role = input("모집하는 직업: ")
level = input("최소 레벨: ")
reward = input("퀘스트 보상: ")
meet = input("집합 장소: ")
comment = input("파티장 한마디: ")

print("")
print("+-----------------------------------+")
print("  📜 퀘스트: " + quest)
print("  👑 파티장: " + leader + " (" + leader_job + ")")
print("  🔍 모집: " + role + " / Lv." + level + " 이상")
print("  💰 보상: " + reward)
print("  📍 집합: " + meet)
print("+-----------------------------------+")
print('  💬 "' + comment + '"')
print("+-----------------------------------+")

# 새로 만들기: 지원자 등장
print("")
applicant = input("지원자 닉네임: ")
greeting = input("지원자 인사말: ")

print("")
print("[시스템] " + applicant + "님이 파티 가입을 신청했습니다.")
print("[" + applicant + "] " + greeting)
print("[시스템] " + leader + "님이 " + applicant + "님을 " + role + "(으)로 받아들였습니다!")
print("[시스템] 파티 '" + leader + "와 친구들'이 " + quest + "에 출발합니다! 🗡️")
