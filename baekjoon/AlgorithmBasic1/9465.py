# 스티커

import sys

T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    case = [0 for i in range(2)]
    for i in range(2):
        case[i] = list(map(int, sys.stdin.readline().split()))
    
    dp = [[0]*3 for i in range(n)]
    dp[0][1], dp[0][2] = case[0][0], case[1][0]
    for j in range(1,n):
        dp[j][1], dp[j][2] = case[0][j], case[1][j]
        dp[j][0] += max(dp[j-1][0], dp[j-1][1], dp[j-1][2])
        dp[j][1] += max(dp[j-1][0], dp[j-1][2])
        dp[j][2] += max(dp[j-1][0], dp[j-1][1])
    print(max(dp[n-1]))