# 1,2,3 더하기3

import sys

T = int(sys.stdin.readline())
dp = [0]*1000001
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4,1000001):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009  # 여기도 나눠주지 않으면 오래걸리는듯

for i in range(T):
    n = int(sys.stdin.readline())
    print(dp[n]%1000000009)