# 2주 확장 프로젝트: 밸런스 게임 성향 테스트 - 좀비 생존 편 (예시 답안)
# 바꾸기: 주제 바꾸기, 질문 3개로 늘려 성향 8가지, 결과마다 설명 추가
# 새로 만들기: 결과에 어울리는 "생존 동료" 추천

print("🧟 좀비 사태! 나의 생존 스타일 테스트 🧟")
print("A 또는 B를 입력하세요.")
print("")
name = input("생존자 이름: ").strip()

print("")
print("Q1. 좀비 경보가 울렸다!")
print("A. 집 문을 잠그고 숨는다   B. 가방을 챙겨 밖으로 나간다")
q1 = input("> ").strip()

print("Q2. 식량을 구하러 간다면?")
print("A. 혼자 조용히   B. 친구들과 함께")
q2 = input("> ").strip()

print("Q3. 무기를 하나 고른다면?")
print("A. 튼튼한 프라이팬   B. 빠른 자전거")
q3 = input("> ").strip()

code = q1 + q2 + q3
print("")
print(name + "님의 생존 코드: " + code)
print("-----------------------------")

if code == "AAA":
    result = "🏠 철벽 방어 은둔자"
    info = "집을 요새로 만드는 데 천재! 좀비가 문 앞에서 포기해요."
elif code == "AAB":
    result = "🦉 조용한 정찰병"
    info = "몰래 나가서 정보를 모아 오는 눈치 백단이에요."
elif code == "ABA":
    result = "🍳 피난처 요리사"
    info = "모두를 먹여 살리는 든든한 살림꾼이에요."
elif code == "ABB":
    result = "📻 무전기 연락병"
    info = "다른 생존자들을 이어 주는 연결 고리예요."
elif code == "BAA":
    result = "🧭 외로운 개척자"
    info = "혼자서도 길을 찾아내는 모험가예요."
elif code == "BAB":
    result = "🚴 질주하는 배달부"
    info = "좀비보다 빠르게! 물자를 나르는 속도왕이에요."
elif code == "BBA":
    result = "🛡️ 맨 앞의 대장"
    info = "친구들을 지키며 앞장서는 리더예요."
elif code == "BBB":
    result = "🚌 탈출 버스 기사"
    info = "모두를 태우고 안전 지대로 떠나는 희망이에요."
else:
    result = "❓ 미확인 생존자"
    info = "A나 B 대신 다른 걸 입력했어요. 대문자로 다시 해 보세요."

print("결과: " + result)
print(info)

# 새로 만들기: 첫 번째 답으로 어울리는 동료 추천
print("")
if q1 == "A":
    print("추천 동료: 밖으로 나가 물자를 구해 올 용감한 친구")
elif q1 == "B":
    print("추천 동료: 기지를 지켜 줄 꼼꼼한 친구")
else:
    print("추천 동료: 먼저 테스트를 다시 해 봐요!")
