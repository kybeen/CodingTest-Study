# 이친수 ==> 10844 계단수 문제랑 비슷하게 풀면 됨

import sys

N = int(sys.stdin.readline())
dp = [[0,0] for i in range(N+1)]
dp[1] = [0,1]
for i in range(2,N+1):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]
print(sum(dp[N]))