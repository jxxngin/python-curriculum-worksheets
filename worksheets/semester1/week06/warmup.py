# 6주 워밍업: 우산 챙길까?
# 비가 오거나 하늘이 흐리면 우산을 챙기라고 알려 주는 프로그램이에요.
# 이 코드에는 오류가 3개 숨어 있어요. 실행해서 오류 메시지를 읽고 고쳐 보세요!

rain = input("비가 와요? (네/아니요): ").strip()
cloud = input("하늘이 흐려요? (네/아니요): ").strip()

need_umbrella = false

if rain == "네" or "흐림":
    need_umbrella = True

if cloud == "네":
    need_umbrella = True

if need_umbrella == True:
    print("☂️ 우산을 챙기세요!")
else:
print("😎 우산 없이 가도 괜찮아요!")
