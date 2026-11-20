# 1주차: 기분 이모지 만들기

> 교안 요약이다. 활동은 `lesson.html`에서 한다(인쇄하면 학습지).

## 🎯 오늘의 미션

거북이를 움직여서 오늘 내 기분을 얼굴 그림(이모지)으로 그리는 프로그램을 만들어요.

**오늘의 목표**

- 거북이를 앞으로 보내고 돌려서 선을 그릴 수 있다.
- 좌표로 거북이를 옮기고, 색을 칠해 그림을 그릴 수 있다.

완성하면 이렇게 돼요:

완성 그림은 `lesson.html`에서 본다.

## 🔧 워밍업

📌 목표: 오류 메시지를 읽고 오류 3개를 고친다. (고장 난 해 그리기 고치기)

`warmup.py`를 실행하고 고친다.

| 오류 이름 | 뜻 | 확인할 곳 |
| --- | --- | --- |
| SyntaxError | 문법이 틀림 | 괄호·따옴표 짝 |
| AttributeError | turtle에 없는 명령을 씀 | 명령 이름의 철자 |
| 메시지 없는 오류 | 그림이 생각과 다름 | 선이 생기면 안 되는 곳 |

## 🪜 단계 1: 노란 얼굴 그리기

📌 목표: 검은 테두리의 노란 원이 그림 창에 나온다.

> 🧰 **원 그리기: circle()**: 괄호 안 숫자(반지름)만큼 원을 그려요. 거북이가 왼쪽으로 돌면서 그려서, 원은 거북이 위쪽에 생겨요.
>
> ```python
> turtle.circle(50)
> ```
> → 반지름 50인 원. 화살표가 거북이예요

> 🧰 **색 칠하기: color()와 begin_fill()·end_fill()**: `color("선 색", "채울 색")`으로 색을 정해요. `begin_fill()`과 `end_fill()` 사이에 그린 모양이 채울 색으로 칠해져요. 색은 영어 이름으로 써요: `"yellow"` 노랑, `"black"` 검정, `"red"` 빨강, `"blue"` 파랑, `"pink"` 분홍
>
> ```python
> turtle.color("blue", "skyblue")
> turtle.begin_fill()
> turtle.circle(30)
> turtle.end_fill()
> ```
> → 파란 테두리, 하늘색으로 칠한 원

① 기능 추가하기: `mini_starter.py`의 `# 단계 1` 아래에 입력

```python
turtle.color("black", "yellow")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
```

② 실행하고 확인: 나온 그림을 칸에 따라 그리기

✅ 검은 테두리의 노란 원이 나왔어요. / 그림 창을 닫으면 프로그램이 끝나요.

## 🪜 단계 2: 눈 찍기

📌 목표: 얼굴 위쪽에 검은 눈 두 개가 나온다.

> 🧰 **좌표로 옮기기: goto()와 penup()**: 그림 창 가운데가 (0, 0)이에요. x는 오른쪽으로, y는 위로 갈수록 커져요. `goto(x, y)`는 그 자리로 가요. 펜이 내려가 있으면 가는 길에 선이 생겨요. 먼저 `penup()`으로 펜을 들면 선 없이 가요.
>
> ```python
> turtle.goto(50, 50)
> turtle.penup()
> turtle.goto(-50, 50)
> ```
> → (50, 50)까지는 선이 생기고, 펜을 든 뒤에는 안 생겨요

> 🧰 **점 찍기: dot()**: 거북이 자리에 동그란 점을 찍어요. 숫자는 점의 크기(지름)예요. 색을 빼면 선 색으로 찍어요.
>
> ```python
> turtle.dot(40, "red")
> ```
> → 크기 40인 빨간 점

① 기능 추가하기: `mini_starter.py`의 `# 단계 2` 아래에 입력

```python
turtle.penup()
turtle.goto(-35, 130)
turtle.dot(25)
turtle.goto(35, 130)
turtle.dot(25)
```

② 실행하고 확인: 나온 그림을 칸에 따라 그리기

✅ 눈 두 개가 나왔어요. / 얼굴에서 눈까지 선이 생기지 않았어요.

## 🪜 단계 3: 웃는 입 그리기

📌 목표: 눈 아래에 V 모양으로 웃는 입이 나온다.

> 🧰 **앞으로 가고 돌기: forward()와 right()·left()**: `forward(거리)`는 거북이가 보는 쪽으로 가요. `right(각도)`는 오른쪽으로, `left(각도)`는 왼쪽으로 그 자리에서 돌아요.
>
> ```python
> turtle.forward(60)
> turtle.left(90)
> turtle.forward(60)
> ```
> → 앞으로 60, 왼쪽으로 90도 돌고, 다시 앞으로 60

> 🧰 **펜 내리기: pendown()**: `penup()`으로 든 펜을 다시 내려요. 내린 뒤에 움직여야 선이 생겨요. 예: `turtle.pendown()`

① 기능 추가하기: `mini_starter.py`의 `# 단계 3` 아래에 입력

```python
turtle.goto(-40, 75)
turtle.pendown()
turtle.right(30)
turtle.forward(46)
turtle.left(60)
turtle.forward(46)
```

② 실행하고 확인: 나온 그림을 칸에 따라 그리기

✅ 눈 아래에 웃는 입이 나왔어요.

③ 따라가기: 단계 3 코드를 한 줄씩 따라가며 펜과 거북이가 보는 쪽(→ ↗ ↘ 중 하나) 적기. 시작: 단계 2가 끝난 뒤라 펜은 올림, 거북이는 → 쪽을 봐요. 끝나면 그림 속 화살표의 방향과 비교해요.

## ⭐ 내 것으로 바꾸기 (오늘의 완성 기준)

📌 목표: 얼굴 색과 입 모양을 바꾸고 하나를 더 그려 오늘 내 기분 이모지로 만든다.

**★ 꼭 하기**

- [ ] 얼굴 색을 내 기분에 맞는 색으로 바꿨어요.
- [ ] 입 모양을 바꿨어요. (돌리는 각도나 가는 거리 바꾸기)
- [ ] 얼굴에 하나를 더 그렸어요. (볼, 코, 눈물 등)

**➕ 더 해 보기**

- [ ] `turtle.pensize(5)`로 선 굵게 하기 (숫자가 클수록 굵어요)
- [ ] `turtle.hideturtle()`로 마지막에 거북이 숨기기
- [ ] 눈 색을 `turtle.dot(25, "blue")`처럼 바꾸기

👀 친구에게 보여 주고 한마디 받기

## 💡 새로 만들기 (하고 싶은 사람)

- 모자 씌우기: 얼굴 위에 색칠한 세모
- 기분 얼굴 하나 더: 옆에 다른 기분 얼굴

**✅ 오늘의 마무리**

- [ ] 워밍업 오류 3개를 고쳤다.
- [ ] 단계마다 실행하며 완성했다.
- [ ] ★ 3개를 완성했다.
- [ ] 친구에게 보여 줬다.

## 🚀 도전 프로젝트: 국기 그리기 챌린지

**왜 만들까?** 국기는 직사각형, 원, 줄무늬 같은 단순한 도형을 정확한 자리에 놓아 만들어요. 미니 프로젝트보다 좌표를 더 많이, 더 정확하게 계산해요.

📌 목표: 시작 파일의 일본 국기 오른쪽에 스위스 국기를 그리고, 내가 고른 국기를 하나 더 그린다.

① 실행해 보기: `extension_starter.py`를 그대로 실행

② 설계하기: 도형마다 색과 꼭짓점 좌표를 표에 먼저 적기. 스위스 십자가는 가운데 (120, 0), 막대 길이 100, 두께 30

완성 예시: 일본(시작 파일) · 스위스 · 프랑스

(그림은 `lesson.html`에서 본다)

| 도형 | 색 | 왼쪽 아래 꼭짓점 | 오른쪽 위 꼭짓점 |
| --- | --- | --- | --- |
| 스위스 바탕 | 빨강 | (40, -80) | (200, 80) |
| 십자가 가로 막대 | 흰색 |   |   |
| 십자가 세로 막대 | 흰색 |   |   |
| 내가 고른 국기: |   |   |   |
|   |   |   |   |

③ 바꾸고 체크하기

- [ ] 스위스 국기의 빨간 정사각형 바탕을 오른쪽에 그렸어요.
- [ ] 흰 십자가를 가로 막대와 세로 막대로 그렸어요.
- [ ] 내가 고른 국기를 아래 줄(y가 -100보다 아래)에 하나 더 그렸어요. (예: 프랑스, 이탈리아 세로 줄무늬)

**➕ 더 해 보기**

- 태극기에 도전: 가운데 태극 무늬를 빨강·파랑 반원으로 (`turtle.circle(반지름, 180)`은 반원)
- 영국 국기에 도전: `turtle.pensize()`로 굵은 대각선과 십자

## 🃏 힌트

<details>
<summary>[워밍업] 선이 하나 더 생길 때 ●○○</summary>

선 없이 옮기려면 `turtle.goto()` 바로 위에 `turtle.penup()`을 넣어요.

</details>

<details>
<summary>[단계 1] 원이 칠해지지 않을 때 ●○○</summary>

`turtle.begin_fill()`은 원 그리기 위, `turtle.end_fill()`은 원 그리기 아래에 있어야 해요. 색은 `color("선 색", "채울 색")` 순서예요.

</details>

<details>
<summary>[단계 2] 얼굴에서 눈까지 선이 생길 때 ●○○</summary>

`turtle.penup()`을 `turtle.goto()`보다 먼저 썼는지 봐요.

</details>

<details>
<summary>[단계 3] 입이 안 나오거나 모양이 이상할 때 ●○○</summary>

`turtle.pendown()`으로 펜을 내렸는지, `right(30)` 다음에 `left(60)`인지 봐요.

</details>

<details>
<summary>[바꾸기] 슬픈 입으로 바꾸고 싶을 때 ●○○</summary>

돌리는 순서를 반대로 해요: `goto(-40, 55)`로 조금 아래에서 시작해서 `left(30)` → `forward(46)` → `right(60)` → `forward(46)`.

</details>

<details>
<summary>[새로 만들기] 모자 씌우기 · 무엇부터 할지 모를 때 ●○○</summary>

얼굴 맨 위는 (0, 200)이에요. 그 근처에 세모를 그리고 색을 칠해요.

</details>

<details>
<summary>[새로 만들기] 모자 씌우기 · 쓸 도구가 떠오르지 않을 때 ●●○</summary>

세모는 `forward(80)`와 `left(120)`을 세 번이에요. 입을 그린 뒤 거북이가 비스듬히 보고 있어서, 먼저 `turtle.setheading(0)`으로 → 쪽을 보게 해요. 칠하기는 `begin_fill()`·`end_fill()`이에요.

</details>

<details>
<summary>[새로 만들기] 모자 씌우기 · 거의 다 됐는데 안 될 때 ●●●</summary>

`turtle.done()` 줄 위에 입력해요.

```python
turtle.penup()
turtle.goto(-40, 195)
turtle.setheading(0)
turtle.pendown()
turtle.color("black", "red")
turtle.begin_fill()
turtle.forward(80)
turtle.left(120)
turtle.forward(80)
turtle.left(120)
turtle.forward(80)
turtle.end_fill()
```

</details>

<details>
<summary>[도전] 스위스 국기 · 무엇부터 할지 모를 때 ●○○</summary>

`extension_starter.py`의 일본 국기 바탕 코드를 봐요. 좌표와 색만 바꾸면 빨간 정사각형이 돼요.

</details>

<details>
<summary>[도전] 스위스 국기 · 쓸 도구가 떠오르지 않을 때 ●●○</summary>

직사각형 하나는 `penup()` → `goto(왼쪽 아래)` → `pendown()` → `begin_fill()` → 꼭짓점을 도는 `goto()` 4번 → `end_fill()`이에요. 십자가는 흰 직사각형 두 개예요.

</details>

<details>
<summary>[도전] 스위스 국기 · 거의 다 됐는데 안 될 때 ●●●</summary>

`# 스위스 국기는 여기부터` 줄 아래에 입력해요. 빨간 바탕이에요.

```python
turtle.penup()
turtle.goto(40, -80)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
turtle.goto(200, -80)
turtle.goto(200, 80)
turtle.goto(40, 80)
turtle.goto(40, -80)
turtle.end_fill()
```

</details>
