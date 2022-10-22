# RGB거리

import sys

N = int(sys.stdin.readline())
color = [[0]*3 for i in range(N)]
for i in range(0, N):
    color[i] = list(map(int, sys.stdin.readline().split()))

dp = [[0]*3 for i in range(N)]
dp[0] = color[0]
for i in range(1,N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + color[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + color[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + color[i][2]

print(min(dp[N-1]))