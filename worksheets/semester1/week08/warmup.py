# 8주 워밍업: 우리 반 간식 뽑기
# 간식 후보 명단(리스트)을 만들고, 새 간식을 추가한 뒤 오늘의 간식을 뽑아요.
# 이 코드에는 오류가 3개 숨어 있어요. 고쳐 보세요!

import random

snacks = ["젤리", "과자", "초콜릿"
print(f"간식 후보: {snacks}")

snacks.add("아이스크림")
print(f"새 후보를 넣었어요: {snacks}")
print(f"네 번째 후보: {snacks[4]}")

today = random.choice(snacks)
print(f"🍬 오늘의 간식은 {today}!")
