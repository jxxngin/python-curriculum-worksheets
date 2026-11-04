# 2학기 4주차 · 세계의 산 높이 정렬

> Codex 별도 제작본. lesson.html을 열어 활동하거나 인쇄해요.

## 🎯 오늘의 미션
산 높이 탐험대의 기록이 뒤섞였어요. 낮은 산부터 줄을 세우고 가장 높은 값과 평균도 찾아요. 이번 주 미니는 글자 기록표, 도전은 터틀 그래프예요.

완성 모습:
```
산 높이(m)
8849
8516
8586
낮은 산부터
8516
8586
8849
산 개수: 3
가장 높은 산: 8849m
가장 낮은 산: 8516m
높이 합계: 25951m
평균 높이: 8650m (정수 몫)
```

## 🔧 워밍업
warmup.py에서 오류 세 개를 찾아 고쳐요. 줄 번호, 오류 이름, 고친 방법을 적어요.

## 🪜 단계 1 · 산 높이를 하나씩 보여 주기
mini_starter.py의 해당 단계 아래에 이어 써요. 실행하고 달라진 모습을 적어요.

🧰 목록의 값을 하나씩: for 뒤에 목록을 쓰면 안의 값을 차례로 꺼내요.
```python
scores = [3, 7]
for score in scores:
    print(score)
```
3과 7이 차례로 나와요.

```python
heights = [8849, 8516, 8586]
print("산 높이(m)")
for height in heights:
    print(height)
```
✅ 입력한 순서대로 높이 세 개가 나왔어요.


## 🪜 단계 2 · 낮은 순서로 정렬하기
mini_starter.py의 해당 단계 아래에 이어 써요. 실행하고 달라진 모습을 적어요.

🧰 작은 값부터 정리하기: sort()는 원래 목록의 순서를 바꿔요.
```python
scores = [8, 2, 5]
scores.sort()
print(scores)
```
[2, 5, 8]. sort() 결과를 다른 변수에 담지 않아요.

```python
# 단계 1 코드 아래에 이어서 써요.
heights.sort()
print("낮은 산부터")
for height in heights:
    print(height)
```
✅ 8516, 8586, 8849 순서로 나왔어요.


## 🪜 단계 3 · 탐험대 요약표 만들기
mini_starter.py의 해당 단계 아래에 이어 써요. 실행하고 달라진 모습을 적어요.

🧰 개수와 대표 값: 빈 목록에서는 max(), min(), 평균을 구할 수 없어요.
```python
scores = [2, 4, 6]
print(len(scores), sum(scores))
print(max(scores), min(scores))
```
개수 3, 합계 12 / 가장 큰 값 6, 가장 작은 값 2예요.

```python
# 단계 2 코드 아래에 이어서 써요.
print(f"산 개수: {len(heights)}")
print(f"가장 높은 산: {max(heights)}m")
print(f"가장 낮은 산: {min(heights)}m")
total = sum(heights)
print(f"높이 합계: {total}m")
print(f"평균 높이: {total // len(heights)}m (정수 몫)")
```
✅ 개수, 최댓값, 최솟값, 합계와 평균이 나왔어요.



## ⭐ 내 것으로 바꾸기
처음 세 높이에서 시작해요. remove → sort → pop은 한 번씩만 추가하고, 남은 목록으로 통계를 다시 계산해요.
🧰 값 빼기와 마지막 값 꺼내기: remove(값)는 같은 값을 하나 지워요. pop()은 마지막 값을 꺼내 돌려줘요. 둘 다 원래 목록을 바꿔요.
```python
numbers = [10, 20, 30]
numbers.remove(20)
last = numbers.pop()
```
numbers는 [10], last는 30이에요.
🔍 따라가기: 위 도구 카드의 remove()와 pop()을 살펴본 뒤 예상해요. 단계 2 직후 heights=[8516, 8586, 8849]에서 remove(8586) → pop()을 차례로 실행해요.
remove 뒤 목록 / pop이 꺼낸 값 / 마지막 목록
바꿀 부분과 계획을 적고 실행해요.

- [ ] remove(8586)으로 산 하나를 뺀 뒤 다시 sort() 했어요.
- [ ] pop()으로 마지막 높이를 꺼내 별도 변수에 담아 보여 줬어요.
- [ ] 남은 목록의 개수와 최댓값·최솟값·합계·평균을 다시 보여 줬어요.

더 해 보기:
- 목록에 실제 산 높이를 더해요.
- 높은 순서로 보여 주는 방법을 찾아요.

친구에게 보여 주고 한마디를 받아요.

## 💡 새로 만들기
- [높이, 이름]을 함께 정렬하기
- 우리 가족 키 정렬하기

[높이, 이름] 기본 코드:
```python
mountains = [[8849, "에베레스트"], [8516, "로체"], [8586, "칸첸중가"]]
mountains.sort()
for mountain in mountains:
    print(mountain[0], mountain[1])
```

## 🚀 도전 · 우리 반 설문 막대그래프
시작 파일은 가상 학생 네 명의 하루 폰 사용 시간(분)이에요. 내 설문으로 바꾸고 번호별 값을 콘솔 기록표와 막대로 비교해요. 막대 길이는 가장 큰 값에 맞춰 자동으로 조절돼요. 음악 취향은 항목별 인원수로 바꿀 수 있어요.
extension_starter.py를 실행하고 바꿔요.
- [ ] 설문 주제와 단위를 정하고 기록표에서 각 막대의 번호를 확인했어요.
- [ ] 응답 수만큼 막대 또는 0을 나타내는 시작점이 생겼어요.
- [ ] 최댓값과 최솟값, 평균을 글자로 보여 줬어요.
더 해 보기: 자료 수에 맞춰 세로 간격을 조절해요.

## 🃏 힌트
<details>
<summary>단계 1 ●○○</summary>

<p>for height in heights: 아래 print(height)를 4칸 들여써요.</p>

</details>

<details>
<summary>단계 2 ●○○</summary>

<p>heights.sort()를 따로 실행한 뒤 for로 정리된 목록을 보여 줘요.</p>

</details>

<details>
<summary>단계 3 ●○○</summary>

<p>len은 개수, max·min은 양 끝 값, sum은 합계예요. 평균은 합계 ÷ 개수이며 여기서는 //로 소수 부분을 버려요.</p>

</details>

<details>
<summary>바꾸기·새로 만들기 1 ●○○</summary>

<p>바꿀 위치나 값을 먼저 찾아요. 한 번에 하나만 바꿔 실행해요.</p>

</details>

<details>
<summary>바꾸기·새로 만들기 2 ●●○</summary>

<p>remove(값)는 같은 값을 하나 지워요. pop()은 마지막 값을 꺼내 돌려줘요. 둘 다 원래 목록을 바꿔요.</p>

</details>

<details>
<summary>바꾸기·새로 만들기 3 ●●●</summary>

<p>단계 3 아래에 이어 써요. remove와 pop은 각각 한 번만 실행해요.</p><pre class="code nonum"><span class="l">heights.remove(8586)</span><span class="l">heights.sort()</span><span class="l">removed = heights.pop()</span><span class="l">print(removed)</span><span class="l">print(heights)</span></pre>

</details>

<details>
<summary>도전 1 ●○○</summary>

<p>시작 코드를 실행하고 어떤 숫자를 바꿀지 골라요.</p>

</details>

<details>
<summary>도전 2 ●●○</summary>

<p>value는 분 단위 자료, scale은 가장 긴 막대를 300으로 맞추는 배율이에요. gap은 막대 사이 간격이에요. 번호는 number에 담아요. 자료는 0 이상의 수를 한 개 이상 넣어요.</p>

</details>

<details>
<summary>도전 3 ●●●</summary>

<p>도전 코드의 else 안, t.done() 앞에 4칸 들여쓰기로 넣어요.</p><pre class="code nonum"><span class="l">print(f"응답 수: {len(minutes)}")</span><span class="l">print(f"평균: {sum(minutes) // len(minutes)}분 (정수 몫)")</span></pre>

</details>

## ✅ 오늘의 마무리
- [ ] 오류 세 개를 고쳤어요.
- [ ] 단계를 실행하며 만들었어요.
- [ ] 꼭 하기 세 가지를 완성했어요.
내가 자랑하고 싶은 부분을 적어요.
