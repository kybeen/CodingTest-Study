# 1, 2, 3 더하기

import sys

T = int(sys.stdin.readline())
dp = [0] * 11
dp[1],dp[2],dp[3] = 1,2,4
for i in range(T):
    n = int(sys.stdin.readline())
    if n == 1 or n == 2 or n == 3:
        print(dp[n])
    else:
        for j in range(4,n+1):
            dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
        print(dp[n])
