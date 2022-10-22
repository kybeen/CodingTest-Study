# 퇴사 ==> 구글링함

import sys

N = int(sys.stdin.readline())
table = [[0,0] for i in range(N)]
for i in range(N):
    # [i][0]은 걸리는 시간 Ti, [i][1]은 받을 수 있는 금액 Pi
    table[i][0], table[i][1] = map(int, sys.stdin.readline().split())

dp = [0] * (N+1)

# 거꾸로 탐색
for i in range(N-1,-1,-1):
    # 퇴사날을 넘어가서 상담할 수 없는 경우
    if i + table[i][0] > N:
        dp[i] = dp[i+1] # 다음 사람에 대한 dp값을 받는다.
    # 상담 가능한 경우
    else:
        # 상담을 안하고 다음 사람으로 넘어갔을때의 값 <==> i번째 사람과 상담한 뒤 가능한 날로 넘어갔을때의 dp값의 합 비교
        dp[i] = max(dp[i+1], table[i][1] + dp[i + table[i][0]])

print(max(dp))