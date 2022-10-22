# 쉬운 계단 수   ==>   dp[i][j] -> i번째 자릿수로 j가 올 수 있는 경우의 수

import sys

N = int(sys.stdin.readline())
dp = [[0,0,0,0,0,0,0,0,0,0,] for i in range(101)]
dp[1] = [0,1,1,1,1,1,1,1,1,1]
for i in range(2,101):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]
    for j in range(1,9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[N])%1000000000)