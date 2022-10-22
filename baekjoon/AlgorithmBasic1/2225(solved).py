# 합분해 -----> (구글링함) 점화식 도출하기 ----> 결과는 나오는데 런타임 에러

import sys

N, K = map(int, sys.stdin.readline().split())
dp = [[1]*(N) for i in range(K)]
if K >= 2:  # n,k가 1인 경우 고려해서 if문 추가해서 해결
    dp[1][0] = 2
for i in range(1,K):
    dp[i][0] = i+1
    for j in range(1,N):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000
print(dp[K-1][N-1]%1000000000)


# n,k가 1,1인 경우 고려 안해서 런타임 에러(인덱스에러) 나왔음
# import sys

# N, K = map(int, sys.stdin.readline().split())
# dp = [[1]*(N) for i in range(K)]
# dp[1][0] = 2
# for i in range(1,K):
#     dp[i][0] = i+1
#     for j in range(1,N):
#         dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000
# print(dp[K-1][N-1]%1000000000)