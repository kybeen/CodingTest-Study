# 차이를 최대로
# ==> 결과를 구하는데에 있어서 특정한 규칙이 없고, N의 크기가 작으므로 브루트포스 방법 사용
# ==> permutation 사용하면 바로 순열 구해주지만 그냥 풀어보기

import sys

# 10974 코드 사용하여 가능한 모든 순열을 저장
def dfs():
    if len(stk) == N:
        permutations.append(stk[:])
        return
    for i in range(0,N):
        if check[i] == 1:   # 배열에 같은 숫자가 들어있을 경우도 생각해야 함. So, 원소를 사용했는지 확인하는 check배열 사용
            continue
        stk.append(arr[i])
        check[i] = 1
        dfs()
        stk.pop()
        check[i] = 0

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stk = []
check = [0] * N
permutations = []
result2 = 0

dfs()
for case in permutations:   # 구해진 모든 순열의 경우의 수 탐색
    result1 = 0
    for i in range(0, N-1):
        result1 += abs(case[i] - case[i+1]) # 탐색하는 순열에서의 해당 식에 의한 결과 result1에 저장
    result2 = max(result2, result1) # 해당 순열 탐색이 끝나면 result1과 result2(최종결과) 비교 후 더 큰 값을 result2에 저장
print(result2)