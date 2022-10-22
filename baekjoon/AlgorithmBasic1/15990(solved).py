# 1, 2, 3 더하기5 ==> 1,000,000,009로 나누는 이유? ==> 수 표현 범위를 넘어가서

import sys

dp = [[0,0,0,0] for i in range(100001)]
dp[1] = [0,1,0,0]
dp[2] = [0,0,1,0]
dp[3] = [0,1,1,1]
for i in range(4, 100001):
    dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % 1000000009
    dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % 1000000009
    dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % 1000000009

T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    print(sum(dp[n]) % 1000000009)  # 여기 안 나눠주면 틀렸다고 뜸 (메모리 초과인듯)