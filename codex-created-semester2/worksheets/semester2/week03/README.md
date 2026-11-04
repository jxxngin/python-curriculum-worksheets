# 2학기 3주차 · 롤리팝 가게

> Codex 별도 제작본. lesson.html을 열어 활동하거나 인쇄해요.

## 🎯 오늘의 미션
막대사탕 가게에 크기가 다른 사탕을 진열해요. 반복 속 숫자를 이용해 위치와 크기를 바꾸고 무늬도 넣어요.

완성 모습:
```
크기가 다른 분홍 사탕 세 개, 막대와 흰 장식 세 개씩
```

## 🔧 워밍업
warmup.py에서 오류 세 개를 찾아 고쳐요. 줄 번호, 오류 이름, 고친 방법을 적어요.

## 🪜 단계 1 · 사탕 세 개 놓기
mini_starter.py의 해당 단계 아래에 이어 써요. 실행하고 달라진 모습을 적어요.

🧰 반복할 때 바뀌는 숫자: range(3)의 숫자는 0, 1, 2가 돼요. 위치 계산에 써요.
```python
for number in range(3):
    print(number * 10)
```
0, 10, 20이 차례로 나와요.

```python
import turtle as t
t.penup()
for number in range(3):
    t.goto(-150 + number * 150, 40)
    t.dot(60, "pink")
```
✅ 가로로 사탕 세 개가 나왔어요.


## 🪜 단계 2 · 막대와 다른 크기 더하기
mini_starter.py의 해당 단계 아래에 이어 써요. 실행하고 달라진 모습을 적어요.

🧰 반복 속에서 크기 바꾸기: 반복 숫자에 20씩 곱해서 차이를 만들어요.
```python
for number in range(3):
    print(40 + number * 20)
```
40, 60, 80이 나와요.

```python
# 단계 1 코드 아래에 이어서 써요.
for number in range(3):
    t.goto(-150 + number * 150, 40)
    t.dot(60 + number * 20, "hotpink")
    t.pendown()
    t.goto(-150 + number * 150, -100)
    t.penup()
```
✅ 세 사탕의 크기가 다르고 아래로 막대가 생겼어요.


## 🪜 단계 3 · 사탕마다 작은 장식 세 개 찍기
mini_starter.py의 해당 단계 아래에 이어 써요. 실행하고 달라진 모습을 적어요.

🧰 반복 안에 반복: 사탕 하나마다 장식을 세 번 찍어요. 안쪽은 8칸 들여써요.
```python
for row in range(2):
    for col in range(3):
        print("*", end="")
    print()
```
별 3개짜리 줄이 2줄 나와요. end=""는 줄바꿈을 미뤄요.

```python
# 단계 2 코드 아래에 이어서 써요.
for number in range(3):
    for spot in range(3):
        t.goto(-165 + number * 150 + spot * 15, 40)
        t.dot(8, "white")
```
✅ 사탕마다 흰 장식이 세 개씩 나왔어요.


매번 맨 아래에 t.done()을 한 번 써요. 다음 단계 코드는 그 줄 위에 써요. 이전 그림 창은 닫고 다시 실행해요.

🔍 따라가기: 단계 3에서 number=1인 사탕만 따라가요.
spot 차례 / x 좌표 차례 / 이 사탕의 점 개수

## ⭐ 내 것으로 바꾸기
단계 1·2의 분홍색 이름을 모두 내 색으로 바꿔요. 같은 자리에서 더 큰 점을 덮는 방식이에요. 60 + number * 20의 숫자와 단계 3의 장식 반복을 바꿔요.
바꿀 부분과 계획을 적고 실행해요.

- [ ] 사탕 색을 내 가게 색으로 바꿨어요.
- [ ] 사탕 크기가 반복 숫자에 따라 달라져요.
- [ ] 중첩 반복으로 사탕마다 장식을 두 개 이상 넣었어요.

더 해 보기:
- 사탕 수와 간격을 함께 바꿔요.
- 장식을 다른 높이에도 찍어요.

친구에게 보여 주고 한마디를 받아요.

## 💡 새로 만들기
- 초콜릿 가게
- 두 줄 사탕 진열대

## 🚀 도전 · 제너러티브 아트 배경화면
줄과 칸은 규칙적으로 놓고, 원의 크기는 무작위로 정해요. 질서와 우연이 섞인 배경을 만들어요.
extension_starter.py를 실행하고 바꿔요.
- [ ] 줄 수나 칸 수를 바꿨어요.
- [ ] 좌표 간격을 바꿨어요.
- [ ] 무작위 크기 범위를 바꾸고 여러 번 실행했어요.
더 해 보기: random.choice()로 색도 골라요.

## 🃏 힌트
<details>
<summary>단계 1 ●○○</summary>

<p>number가 0, 1, 2일 때 -150 + number * 150을 계산해요. 세 x는 -150, 0, 150이에요.</p>

</details>

<details>
<summary>단계 2 ●○○</summary>

<p>크기는 60 + number * 20, 막대 끝의 y는 -100이에요. 다음 사탕으로 가기 전에 penup()을 써요.</p>

</details>

<details>
<summary>단계 3 ●○○</summary>

<p>안쪽 for와 그 안의 goto·dot 들여쓰기를 비교해요. 사탕 하나마다 spot이 다시 0부터 시작해요.</p>

</details>

<details>
<summary>바꾸기·새로 만들기 1 ●○○</summary>

<p>바꿀 위치나 값을 먼저 찾아요. 한 번에 하나만 바꿔 실행해요.</p>

</details>

<details>
<summary>바꾸기·새로 만들기 2 ●●○</summary>

<p>바깥 number는 사탕 위치, 안쪽 spot은 장식 위치에 써요.</p>

</details>

<details>
<summary>바꾸기·새로 만들기 3 ●●●</summary>

<p>단계 3 아래, t.done() 바로 위에 넣어요.</p><pre class="code nonum"><span class="l">for number in range(3):</span><span class="l">    for spot in range(3):</span><span class="l">        t.goto(-165 + number * 150 + spot * 15, 55)</span><span class="l">        t.dot(8, "white")</span></pre>

</details>

<details>
<summary>도전 1 ●○○</summary>

<p>시작 코드를 실행하고 어떤 숫자를 바꿀지 골라요.</p>

</details>

<details>
<summary>도전 2 ●●○</summary>

<p>row는 y 좌표에, col은 x 좌표에 써요. 크기는 size라는 상자에 뽑아 담아요.</p>

</details>

<details>
<summary>도전 3 ●●●</summary>

<p>도전 반복문 안의 size와 dot 두 줄을 아래로 바꿔요. 들여쓰기는 원래처럼 8칸으로 맞춰요.</p><pre class="code nonum"><span class="l">size = random.randint(12, 45)</span><span class="l">t.dot(size, "coral")</span></pre>

</details>

## ✅ 오늘의 마무리
- [ ] 오류 세 개를 고쳤어요.
- [ ] 단계를 실행하며 만들었어요.
- [ ] 꼭 하기 세 가지를 완성했어요.
내가 자랑하고 싶은 부분을 적어요.
