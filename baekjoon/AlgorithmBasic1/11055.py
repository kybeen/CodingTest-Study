# 가장 큰 증가 부분 수열
# --> 증가가 아닌 경우에는 dp테이블에 값이 0으로 남기 때문에 이 경우도 고려해서 dp테이블에 값이 안 들어가면 해당 인덱스의 수열의 값을 넣어줘야함

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [0] * N
dp[0] = A[0]
for i in range(1,N):
    for j in range(0,i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+A[i])
    if dp[i] == 0:  # 추가한 코드
        dp[i] = A[i]
print(max(dp))


#-------------------> 틀린 코드
# import sys

# N = int(sys.stdin.readline())
# A = list(map(int, sys.stdin.readline().split()))

# dp = [0] * N
# dp[0] = A[0]
# for i in range(1,N):
#     for j in range(0,i):
#         if A[i] > A[j]:
#             dp[i] = max(dp[i], dp[j]+A[i])
# print(max(dp))