# 2학기 2주차 · 바람개비

> Codex 별도 제작본. lesson.html을 열어 활동하거나 인쇄해요.

## 🎯 오늘의 미션
바람이 없어도 멋진 바람개비를 그릴 수 있어요. 삼각 날개를 그리고 방향을 바꾸어 네 날개를 완성해요.

완성 모습:
```
한 중심에서 네 방향으로 펼쳐진 청록색 삼각 날개
```

## 🔧 워밍업
warmup.py에서 오류 세 개를 찾아 고쳐요. 줄 번호, 오류 이름, 고친 방법을 적어요.

## 🪜 단계 1 · 첫 삼각 날개 그리기
mini_starter.py의 해당 단계 아래에 이어 써요. 실행하고 달라진 모습을 적어요.

🧰 같은 일을 여러 번: for 아래 들여쓴 줄을 range()에 적은 횟수만큼 반복해요.
```python
for turn in range(2):
    print("빙글")
```
빙글이 두 번 나와요. 정삼각형은 한 바퀴 360도를 3으로 나눈 120도씩 돌아요.

```python
import turtle as t
t.color("teal")
for side in range(3):
    t.forward(90)
    t.left(120)
```
✅ 삼각형 하나를 그렸어요.


## 🪜 단계 2 · 두 번째 날개 더하기
mini_starter.py의 해당 단계 아래에 이어 써요. 실행하고 달라진 모습을 적어요.

🧰 날개 사이의 각도: 네 방향으로 벌어지려면 360 ÷ 4만큼 돌아요.
```python
t.left(45)
t.forward(20)
```
보던 방향에서 왼쪽으로 45도 돌아 20 움직여요.

```python
# 단계 1 코드 아래에 이어서 써요.
t.left(90)
for side in range(3):
    t.forward(90)
    t.left(120)
```
✅ 첫 날개에서 90도 돌아 두 번째 날개가 생겼어요.


## 🪜 단계 3 · 세 번째 날개 더하기
mini_starter.py의 해당 단계 아래에 이어 써요. 실행하고 달라진 모습을 적어요.

```python
# 단계 2 코드 아래에 이어서 써요.
t.left(90)
for side in range(3):
    t.forward(90)
    t.left(120)
```
✅ 세 번째 방향에 날개가 생겼어요.


## 🪜 단계 4 · 네 번째 날개 완성하기
mini_starter.py의 해당 단계 아래에 이어 써요. 실행하고 달라진 모습을 적어요.

```python
# 단계 3 코드 아래에 이어서 써요.
t.left(90)
for side in range(3):
    t.forward(90)
    t.left(120)
```
✅ 네 방향으로 날개가 펼쳐졌어요.


매번 맨 아래에 t.done()을 한 번 써요. 다음 단계 코드는 그 줄 위에 써요. 이전 그림 창은 닫고 다시 실행해요.

🔍 따라가기: 단계 1의 range(3)을 따라가요. side는 0부터 시작해요.
side 차례 / forward 횟수 / left로 돈 각도 합

## ⭐ 내 것으로 바꾸기
네 곳의 forward(90)을 같은 길이로 바꿔요. 각 날개의 for 바로 위에서 pencolor()로 다른 색을 정해요. 삼각형 안의 회전은 120도, 날개 사이는 90도예요.
바꿀 부분과 계획을 적고 실행해요.

- [ ] 날개 길이를 바꿨어요.
- [ ] 날개마다 색을 다르게 바꿨어요.
- [ ] 네 날개 사이에서 90도씩 도는 이유를 설명하고 완성했어요.

더 해 보기:
- 막대를 더해요.
- 360 ÷ 날개 수로 각도를 계산해 여섯 날개로 바꿔요.

친구에게 보여 주고 한마디를 받아요.

## 💡 새로 만들기
- 세 날개 바람개비
- 네모 날개 바람개비

## 🚀 도전 · 스피로그래프 만다라
원을 조금씩 돌려 겹치면 꽃 같은 무늬가 생겨요. 원의 수와 회전 각도를 함께 바꿔 나만의 무늬를 만들어요.
extension_starter.py를 실행하고 바꿔요.
- [ ] 원의 수와 회전 각도를 바꿨어요.
- [ ] 반지름을 바꿔 무늬 크기를 조절했어요.
- [ ] 한 바퀴를 채우는 각도를 설명했어요.
더 해 보기: 같은 반복을 한 번 더 써서 안쪽 무늬를 더해요.

## 🃏 힌트
<details>
<summary>단계 1 ●○○</summary>

<p>for 줄 끝의 :와 아래 두 줄의 4칸 들여쓰기를 확인해요. range(3)은 변 세 개예요.</p>

</details>

<details>
<summary>단계 2 ●○○</summary>

<p>삼각형을 그린 뒤 left(90)을 한 번 쓰고 같은 삼각형 반복을 이어 써요.</p>

</details>

<details>
<summary>단계 3 ●○○</summary>

<p>세 번째 날개도 새 삼각형을 그리기 전에 left(90)으로 방향을 바꿔요.</p>

</details>

<details>
<summary>단계 4 ●○○</summary>

<p>네 번째 날개는 앞의 삼각형 반복을 다시 써요. 삼각형 안의 120도는 그대로 둬요.</p>

</details>

<details>
<summary>바꾸기·새로 만들기 1 ●○○</summary>

<p>바꿀 위치나 값을 먼저 찾아요. 한 번에 하나만 바꿔 실행해요.</p>

</details>

<details>
<summary>바꾸기·새로 만들기 2 ●●○</summary>

<p>삼각형 안에서는 left(120), 날개 사이에서는 left(90)을 써요.</p>

</details>

<details>
<summary>바꾸기·새로 만들기 3 ●●●</summary>

<p>기존 첫 번째 날개 부분을 아래처럼 바꿔요. 다른 날개도 길이와 색을 각각 고쳐요.</p><pre class="code nonum"><span class="l">t.pencolor("orange")</span><span class="l">for side in range(3):</span><span class="l">    t.forward(70)</span><span class="l">    t.left(120)</span></pre>

</details>

<details>
<summary>도전 1 ●○○</summary>

<p>시작 코드를 실행하고 어떤 숫자를 바꿀지 골라요.</p>

</details>

<details>
<summary>도전 2 ●●○</summary>

<p>원의 수 × 돌리는 각도가 360이 되도록 골라요.</p>

</details>

<details>
<summary>도전 3 ●●●</summary>

<p>기존 도전 반복문 세 줄을 아래로 바꿔요.</p><pre class="code nonum"><span class="l">for turn in range(18):</span><span class="l">    t.circle(55)</span><span class="l">    t.left(20)</span></pre>

</details>

## ✅ 오늘의 마무리
- [ ] 오류 세 개를 고쳤어요.
- [ ] 단계를 실행하며 만들었어요.
- [ ] 꼭 하기 세 가지를 완성했어요.
내가 자랑하고 싶은 부분을 적어요.
