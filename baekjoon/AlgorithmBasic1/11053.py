# 가장 긴 증가하는 부분 수열

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
dp = [1 for i in range(N)]
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i],dp[j]+1)  # j의 인덱스를 1부터 i 전까지 증가시켜가면서 i가 j보다 작을때만 dp[i]의 값을 더 큰 값으로 갱신한다.
print(max(dp))