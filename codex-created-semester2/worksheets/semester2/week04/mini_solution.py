# 단계 1: 산 높이를 하나씩 보여 주기
heights = [8849, 8516, 8586]
print("산 높이(m)")
for height in heights:
    print(height)

# 단계 2: 낮은 순서로 정렬하기
# 단계 1 코드 아래에 이어서 써요.
heights.sort()
print("낮은 산부터")
for height in heights:
    print(height)

# 단계 3: 탐험대 요약표 만들기
# 단계 2 코드 아래에 이어서 써요.
print(f"산 개수: {len(heights)}")
print(f"가장 높은 산: {max(heights)}m")
print(f"가장 낮은 산: {min(heights)}m")
total = sum(heights)
print(f"높이 합계: {total}m")
print(f"평균 높이: {total // len(heights)}m (정수 몫)")

# 꼭 하기 세 가지를 모두 바꾼 예시는 mini_change_solution.py에 있다.
