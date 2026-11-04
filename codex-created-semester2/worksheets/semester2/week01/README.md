# 2학기 1주차 · 기분 이모지

> Codex 별도 제작본. lesson.html을 열어 활동하거나 인쇄해요.

## 🎯 오늘의 미션
오늘 내 마음은 어떤 얼굴인가요? 둥근 얼굴에 눈과 입을 더해 나만의 기분 이모지를 만들어요.

완성 모습:
```
노란 원 얼굴 → 같은 높이의 검은 눈 두 개 → 웃는 입
```

## 🔧 워밍업
warmup.py에서 오류 세 개를 찾아 고쳐요. 줄 번호, 오류 이름, 고친 방법을 적어요.

## 🪜 단계 1 · 얼굴 바탕 그리기
mini_starter.py의 해당 단계 아래에 이어 써요. 실행하고 달라진 모습을 적어요.

🧰 그림 펜과 채우기: 선을 닫으면 그 안을 색으로 채울 수 있어요.
```python
import turtle as t
t.color("skyblue")
t.circle(30)
```
하늘색 원을 그려요. begin_fill()과 end_fill() 사이에 닫힌 도형을 그리면 속도 채워요.

```python
import turtle as t
t.color("gold")
t.begin_fill()
t.circle(80)
t.end_fill()
t.penup()
```
✅ 노란 얼굴 바탕이 나왔어요.

begin_fill() 뒤에 원을 그리고 end_fill()로 채워요. penup()은 펜을 들어 이동선을 남기지 않아요.
## 🪜 단계 2 · 눈 두 개 찍기
mini_starter.py의 해당 단계 아래에 이어 써요. 실행하고 달라진 모습을 적어요.

🧰 좌표로 이동하기: 가운데는 (0, 0), 오른쪽은 x가 커지고 위쪽은 y가 커져요.
```python
t.penup()
t.goto(40, 60)
t.dot(10, "blue")
```
선을 남기지 않고 오른쪽 위에 파란 점을 찍어요.

```python
# 단계 1 코드 아래에 이어서 써요.
t.goto(-30, 100)
t.dot(14, "black")
t.goto(30, 100)
t.dot(14, "black")
```
✅ 같은 높이에 검은 눈이 두 개 나왔어요.

dot(크기, 색)은 현재 위치에 점을 찍어요. 두 눈의 y가 같으면 나란히 놓여요.
## 🪜 단계 3 · 웃는 입 그리기
mini_starter.py의 해당 단계 아래에 이어 써요. 실행하고 달라진 모습을 적어요.

🧰 방향과 둥근 선: 0도는 오른쪽, 90도는 위쪽이에요. circle(반지름, 각도)는 원의 일부를 그려요.
```python
t.setheading(0)
t.forward(25)
t.left(90)
```
오른쪽으로 25 움직인 뒤 위를 봐요. backward()는 뒤로, right()는 오른쪽으로 돌아요.

```python
# 단계 2 코드 아래에 이어서 써요.
t.goto(-35, 65)
t.setheading(-90)
t.pencolor("black")
t.pendown()
t.circle(35, 180)
t.penup()
```
✅ 양 끝이 올라간 웃는 입이 생겼어요.

pencolor()는 선 색, pendown()은 펜 내리기예요. setheading(-90)은 아래쪽을 보게 해요.
매번 맨 아래에 t.done()을 한 번 써요. 다음 단계 코드는 그 줄 위에 써요. 이전 그림 창은 닫고 다시 실행해요.

🔍 따라가기: 단계 2의 두 goto를 순서대로 따라가요.
첫 눈의 x, y / 둘째 눈의 x, y / 눈 사이 거리

## ⭐ 내 것으로 바꾸기
기존 코드의 얼굴 색, 눈의 크기·위치, 입의 각도를 고쳐요. 예를 들어 circle(35, 180)을 circle(35, 120)으로 바꾸면 입 모양이 달라져요. 새 코드를 덧붙이기보다 해당 줄을 바꿔요.
바꿀 부분과 계획을 적고 실행해요.

- [ ] 얼굴 색을 내 기분에 맞게 바꿨어요.
- [ ] 눈의 크기나 위치를 바꿨어요.
- [ ] 입 모양을 바꾸고 어떤 기분인지 친구에게 설명했어요.

더 해 보기:
- 볼에 점을 찍어 꾸며요.
- 눈썹을 더해요.

친구에게 보여 주고 한마디를 받아요.

## 💡 새로 만들기
- 졸린 얼굴
- 깜짝 놀란 얼굴

## 🚀 도전 · 국기 그리기 챌린지
국기를 관찰하고 색과 도형으로 나누어 봐요. 시작 파일의 일본 국기를 바꿔 스위스 국기에 도전해요. 공식 규격 재현보다 도형 배치 연습에 집중해요.
extension_starter.py를 실행하고 바꿔요.
- [ ] 배경과 중심 도형의 색을 구분했어요.
- [ ] 선을 남기지 않고 도형 사이를 이동했어요.
- [ ] 색을 채우는 시작과 끝을 짝지었어요.
더 해 보기: 태극기나 영국 국기는 교사와 도형을 나눠 설계해요.

## 🃏 힌트
<details>
<summary>단계 1 ●○○</summary>

<p>채우기 시작과 끝 사이에 circle(80)이 있는지 확인해요. 얼굴을 다 그린 뒤 펜을 들어요.</p>

</details>

<details>
<summary>단계 2 ●○○</summary>

<p>두 goto의 x는 서로 반대 부호, y는 100으로 같아요. goto 다음 줄에 dot을 써요.</p>

</details>

<details>
<summary>단계 3 ●○○</summary>

<p>입에 선이 없으면 pendown()을 확인해요. 아래쪽을 본 뒤 반지름 35인 반원을 그려요.</p>

</details>

<details>
<summary>바꾸기·새로 만들기 1 ●○○</summary>

<p>바꿀 위치나 값을 먼저 찾아요. 한 번에 하나만 바꿔 실행해요.</p>

</details>

<details>
<summary>바꾸기·새로 만들기 2 ●●○</summary>

<p>얼굴 색은 color(), 눈은 dot(크기, 색), 입 모양은 circle(반지름, 각도)의 숫자를 고쳐요.</p>

</details>

<details>
<summary>바꾸기·새로 만들기 3 ●●●</summary>

<p>기존 단계 3의 여섯 줄을 아래로 바꿔요.</p><pre class="code nonum"><span class="l">t.goto(-35, 65)</span><span class="l">t.setheading(-90)</span><span class="l">t.pencolor("black")</span><span class="l">t.pendown()</span><span class="l">t.circle(35, 120)</span><span class="l">t.penup()</span></pre>

</details>

<details>
<summary>도전 1 ●○○</summary>

<p>시작 코드를 실행하고 어떤 숫자를 바꿀지 골라요.</p>

</details>

<details>
<summary>도전 2 ●●○</summary>

<p>흰 십자가는 굵은 가로선과 세로선으로 나눌 수 있어요.</p>

</details>

<details>
<summary>도전 3 ●●●</summary>

<p>도전 시작 코드의 원 그리기 부분을 지우고 십자가 선으로 바꿔요. 먼저 penup()과 goto(-65, 0), pendown()으로 가로선 시작점으로 가요.</p><pre class="code nonum"><span class="l">t.pencolor("white")</span><span class="l">t.pensize(35)</span><span class="l">t.goto(65, 0)</span></pre>

</details>

## ✅ 오늘의 마무리
- [ ] 오류 세 개를 고쳤어요.
- [ ] 단계를 실행하며 만들었어요.
- [ ] 꼭 하기 세 가지를 완성했어요.
내가 자랑하고 싶은 부분을 적어요.
