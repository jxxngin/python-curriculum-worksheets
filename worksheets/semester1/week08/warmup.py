# 8주 워밍업: 우리 반 간식 뽑기
# 간식 후보 명단(리스트)에 새 간식을 넣고, 오늘의 간식을 뽑아요.
# 오류가 3개 있어요. 고쳐 보세요.

import random

snacks = ["젤리", "과자", "초콜릿"]
print(f"첫 번째 후보: {snacks[1]}")

snacks.add("아이스크림")
print(f"새 명단: {snacks}")
print(f"마지막 후보: {snacks[4]}")

today = random.choice(snacks)
print(f"🍬 오늘의 간식: {today}")
