# 7주 확장 프로젝트 (택1): 숫자 야구 게임 (예시 답안)
# 바꾸기: 볼 판정, 아웃 표시, 잘못된 입력 continue, 기회 10번 제한
# 새로 만들기: 'pass' 입력 시 힌트(백의 자리 공개), 기회에 따라 등급

import random

# [따라 하기 코드] 서로 다른 세 자리 숫자 뽑기
s1 = random.randint(1, 9)
s2 = random.randint(0, 9)
while s2 == s1:
    s2 = random.randint(0, 9)
s3 = random.randint(0, 9)
while s3 == s1 or s3 == s2:
    s3 = random.randint(0, 9)

print("⚾ 숫자 야구 게임 ⚾")
print("서로 다른 숫자로 된 세 자리 수를 맞혀 보세요! 기회는 10번.")
print("힌트가 필요하면 'pass'를 입력하세요. (기회 1번 사용)")

tries = 0
max_tries = 10
win = False

while tries < max_tries:
    text = input(f"[{tries + 1}/{max_tries}] 세 자리 숫자: ").strip()

    if text == "pass":
        tries = tries + 1
        print(f"  💡 힌트: 백의 자리는 {s1}이에요.")
        continue

    guess = int(text)
    if guess < 100 or guess > 999:
        print("  세 자리 숫자를 입력해 주세요. (기회는 그대로)")
        continue

    g1 = guess // 100
    g2 = guess // 10 % 10
    g3 = guess % 10
    if g1 == g2 or g2 == g3 or g1 == g3:
        print("  서로 다른 숫자 세 개로 입력해 주세요. (기회는 그대로)")
        continue

    tries = tries + 1
    strike = 0
    ball = 0

    # 첫째 자리
    if g1 == s1:
        strike = strike + 1
    elif g1 == s2 or g1 == s3:
        ball = ball + 1
    # 둘째 자리
    if g2 == s2:
        strike = strike + 1
    elif g2 == s1 or g2 == s3:
        ball = ball + 1
    # 셋째 자리
    if g3 == s3:
        strike = strike + 1
    elif g3 == s1 or g3 == s2:
        ball = ball + 1

    if strike == 0 and ball == 0:
        print("  ❌ 아웃! (하나도 없어요)")
    else:
        print(f"  {strike} 스트라이크 {ball} 볼")

    if strike == 3:
        win = True
        break

print("")
if win:
    print(f"🎉 정답! {tries}번 만에 맞혔어요.")
    if tries <= 4:
        print("등급: 🏆 천재 타자")
    elif tries <= 7:
        print("등급: ⚾ 주전 타자")
    else:
        print("등급: 🧢 신인 타자")
else:
    print(f"😢 기회를 모두 썼어요. 정답은 {s1}{s2}{s3}였어요.")
