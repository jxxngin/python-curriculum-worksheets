# 4주차: 비밀의 문 게임 만들기

> 교안 요약이에요. 활동은 `lesson.html`을 열어서 해요(인쇄하면 학습지).

## 🎯 오늘의 미션

보물이 숨은 문은 몇 번일까? 🚪 실행할 때마다 보물 위치와 비밀번호가 바뀌는 모험 게임을 만들어 봐요. 친구가 해도, 내가 다시 해도 매번 새로워요!

완성하면 이렇게 돼요:

```
탐험가 이름: 하린
[1관문] 몇 번 문을 열까요? (1~3): 2
💎 보물을 찾았어요! +10점
[2관문] 1~20 중 비밀번호는? 10
비밀번호와 2만큼 차이 나요!
비밀번호는 12이었어요.
🏆 하린님의 점수: 15점
```

## 🔧 워밍업

`warmup.py`를 실행하고 오류 3개를 고쳐요. (고장 난 주사위 고치기)

## 🪜 단계 1: 보물 문을 무작위로 정하기

> 🧰 **도구 상자 꺼내기: import**: 파이썬에 들어 있는 도구 상자를 꺼내 써요. 맨 위에 한 번만!

> 🧰 **무작위 뽑기: random.randint(a, b)**: a부터 b까지 중 하나를 뽑아요. b도 나와요!

`mini_starter.py`의 `# 단계 1` 아래에 이어 써요.

```python
import random
name = input("탐험가 이름: ")
score = 0
treasure_door = random.randint(1, 3)
print(f"(쉿! 테스트용) 보물은 {treasure_door}번 문")
```

✅ 실행할 때마다 보물 문 번호가 바뀌었어요.

## 🪜 단계 2: 1관문: 문을 골라 보물 찾기

`mini_starter.py`의 `# 단계 2` 아래에 이어 써요.

```python
pick = int(input("[1관문] 몇 번 문을 열까요? (1~3): "))
if pick == treasure_door:
    print("💎 보물을 찾았어요! +10점")
    score = score + 10
else:
    print(f"꽝! 보물은 {treasure_door}번 문에 있었어요.")
```

✅ 맞히면 "보물을 찾았어요", 틀리면 "꽝!"이 나왔어요.

## 🪜 단계 3: 2관문: 비밀번호가 얼마나 가까운지 알려 주기

> 🧰 **거리 재기: abs()**: 두 수가 얼마나 떨어져 있는지 알려 줘요. 누가 더 커도 0 이상이 나와요.

`mini_starter.py`의 `# 단계 3` 아래에 이어 써요.

```python
secret = random.randint(1, 20)
guess = int(input("[2관문] 1~20 중 비밀번호는? "))
gap = abs(guess - secret)
print(f"비밀번호와 {gap}만큼 차이 나요!")
```

✅ 비밀번호와의 차이가 화면에 나왔어요. (음수가 아니에요!)

## 🪜 단계 4: 점수를 주고 게임 끝내기

`mini_starter.py`의 `# 단계 4` 아래에 이어 써요.

```python
if gap == 0:
    score = score + 20
elif gap <= 3:
    score = score + 5
print(f"비밀번호는 {secret}이었어요.")
print(f"🏆 {name}님의 점수: {score}점")
```

✅ 마지막에 내 점수가 나왔어요. / 테스트용 줄을 #으로 숨겼어요.

## ⭐ 내 것으로 바꾸기 (오늘의 완성 기준)

**★ 꼭 하기**

- [ ] 관문 이름과 이야기를 나만의 모험으로 바꿨어요.
- [ ] random.randint()를 쓰는 새 관문을 1개 더 만들었어요.
- [ ] 마지막에 점수에 따라 칭호가 나와요. (예: 30점 이상 "전설의 탐험가")

**➕ 더 해 보기**

- [ ] 문 개수나 비밀번호 범위를 바꿔 난이도를 조절했어요.
- [ ] abs()로 차이에 따라 "뜨거워요 / 따뜻해요 / 차가워요"를 알려 줘요.

## 💡 새로 만들기 (하고 싶은 사람)

- 함정 문 (꽝이 하나뿐인 문, 걸리면 -5점)
- 행운의 주사위 (보너스 점수가 무작위)

## 🚀 도전 프로젝트: 피자 가성비 계산기

크기도 가격도 다른 두 피자, 어느 쪽이 더 이득일까요? 🍕 넓이 1cm²당 가격으로 비교해요. 실행하기 전에 어느 쪽이 이득일지 먼저 예상해 봐요.

`extension_starter.py`를 실행해 보고 바꿔요.

- [ ] 피자 이름도 물어봐서 결과에 이름이 나와요.
- [ ] max()로 더 큰 피자를 알려 줘요.
- [ ] 실제 메뉴(지름, 가격)를 넣어 확인했어요.

## 🃏 힌트

<details>
<summary>단계 1 ●○○</summary>

import random은 맨 위에 써요. 뽑는 도구는 random.randint(처음, 끝)이에요.

</details>

<details>
<summary>단계 2 ●○○</summary>

입력은 글자라서 int()로 숫자로 바꿔야 비교할 수 있어요. 비교는 ==, 줄 끝에 :!

</details>

<details>
<summary>단계 3 ●○○</summary>

차이는 abs(guess - secret). 순서를 바꿔 써도 결과가 같아요.

</details>

<details>
<summary>단계 4 ●○○</summary>

if → elif 순서로 써요. "3 이하"는 &lt;= 3이에요.

</details>

<details>
<summary>새로 만들기 · 거의 코드 ●●●</summary>

trap = random.randint(1, 3)pick3 = int(input("문 번호: "))if pick3 == trap:    print("🕳️ 함정! -5점")    score = score - 5

</details>

<details>
<summary>도전 · 쿠폰 거의 코드 ●●●</summary>

coupon = random.randint(1, 3) * 10cut = price_a * coupon // 100price_a = price_a - cutprint(f"{coupon}% 할인! {price_a}원")

</details>
