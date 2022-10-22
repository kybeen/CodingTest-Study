# 타일 채우기 -------> 어려움 이해 ㅈㄴ안됐음
# ==> 3 x 홀수 크기인 경우는 채우는 경우가 0임, N이 짝수일때만 고려한다.

import sys

N = int(sys.stdin.readline())
dp = [0 for i in range(31)]
dp[0] = 1   # 계산을 위해 설정한 1 (3 x 0은 없기 때문에 실제 경우의 수는 아님)
dp[2] = 3   # (3 x 2의 크기일 때는 경우의 수가 3가지)
for i in range(4,N+1,2): # N이 4일때부터 dp테이블 for문으로 채워나감 (가로 4칸부터는 새로 채우는 타일 모양이 2개씩 추가됨)
    dp[i] = dp[i-2]*3   # 마지막 부분의 3 x 2칸을 3가지 방법으로 채우는 경우의 수
    for j in range(0,i-2,2):
        dp[i] += dp[j] * 2  # 마지막 부분의 3 x 4칸부터 3x6 3x8 ... 3xi 칸만큼 채울 때마다 추가되는 2가지 방법을 곱한 경우의 수를 더해준다.
print(dp[N])



#---------------------------> 틀림
# import sys

# N = int(sys.stdin.readline())
# dp = [0] * (N+1)
# dp[2] = 3
# if N >= 3:
#     dp[4] = 11
#     for i in range(6,N+1,2):
#         dp[i] = (dp[i-2]*3) + (dp[i-4]*2)
# print(dp[N])