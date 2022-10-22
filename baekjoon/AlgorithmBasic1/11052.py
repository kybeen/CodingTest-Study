#카드 구매하기 --> 이해하기 어렵;

import sys

N = int(sys.stdin.readline())
P = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0]*(N+1)
dp[1] = P[1]
for i in range(1,N+1):
    for j in range(0,i):
        dp[i] = max(dp[i], P[i-j]+dp[j])
print(dp[-1])