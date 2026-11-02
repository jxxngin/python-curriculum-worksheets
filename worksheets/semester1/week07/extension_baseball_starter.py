# 7주 확장 프로젝트 (택1): 숫자 야구 게임
# 이 코드는 그대로 실행돼요. 컴퓨터가 정한 서로 다른 세 자리 숫자를 맞히는 게임이에요.
# 지금은 '스트라이크'만 알려 줘요. 바꾸기부터 시작해서 진짜 숫자 야구로 키워 보세요.
#   스트라이크: 숫자와 자리가 모두 맞음
#   볼: 숫자는 있지만 자리가 다름

import random

# ===== [따라 하기 코드] 서로 다른 세 자리 숫자 뽑기 =====
# 이 부분은 그대로 따라 써요. while로 '겹치지 않을 때까지 다시 뽑기'를 해요.
s1 = random.randint(1, 9)          # 백의 자리 (0이면 세 자리가 아니니까 1~9)
s2 = random.randint(0, 9)          # 십의 자리
while s2 == s1:                    # 백의 자리와 같으면 다시 뽑기
    s2 = random.randint(0, 9)
s3 = random.randint(0, 9)          # 일의 자리
while s3 == s1 or s3 == s2:        # 앞의 두 숫자와 같으면 다시 뽑기
    s3 = random.randint(0, 9)
# =====================================================

print("⚾ 숫자 야구 게임 ⚾")
print("서로 다른 숫자로 된 세 자리 수를 맞혀 보세요!")

tries = 0
while True:
    guess = int(input("세 자리 숫자: "))
    tries = tries + 1

    # 세 자리 숫자를 한 자리씩 나누기
    g1 = guess // 100
    g2 = guess // 10 % 10
    g3 = guess % 10

    strike = 0
    if g1 == s1:
        strike = strike + 1
    if g2 == s2:
        strike = strike + 1
    if g3 == s3:
        strike = strike + 1

    print(f"  {strike} 스트라이크")

    if strike == 3:
        print(f"🎉 정답! {tries}번 만에 맞혔어요.")
        break
