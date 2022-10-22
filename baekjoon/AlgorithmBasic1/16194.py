# 카드 구매하기 2
# ==> 11052에서 max 부분을 min으로 바꿈
# ==> i의 for문이 돌때 처음에 dp[i] = P[i]을 해주지 않으면 최솟값을 찾기 떄문에 처음 값인 0만 나오게 됨

import sys

N = int(sys.stdin.readline())
P = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0]*(N+1)
dp[1] = P[1]
for i in range(1,N+1):
    dp[i] = P[i]
    for j in range(1,i):
        dp[i] = min(dp[i], P[i-j]+dp[j])
print(dp[-1])