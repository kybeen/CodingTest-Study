# RGB거리2 ----------> 어려움;;

import sys

N = int(sys.stdin.readline())
cost = [[0]*3 for i in range(N)]
for i in range(0, N):
    cost[i] = list(map(int, sys.stdin.readline().split()))

dp = [[0, 0, 0] for i in range(N)]
BIG = sys.maxsize   # 임의의 큰 정수 BIG
result2 = BIG

for select in range(3):
    for i in range(3):
        if select == i: # 첫번째 집을 칠할 때 R,G,B 중 한가지 색만 사용하는 경우 설정 (select : 0,1,2 -> R,G,B)
            dp[0][i] = cost[0][i]
        else:
            dp[0][i] = BIG  # 임의의 큰 정수 BIG을 넣게 되면서 두번째 집부터는 작은 비용을 찾기 위해 무조건 첫번째 집에 칠한 색만 고려하게 된다.

    for j in range(1,N):
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + cost[j][0]
        dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + cost[j][1]
        dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + cost[j][2]
    # N번째 집은 첫번째 집에 칠한 색은 제외한 dp만 구한다.
    temp1 = (select + 4) % 3
    temp2 = (select + 5) % 3
    result = min(dp[N-1][temp1], dp[N-1][temp2])
    # 첫번째 집에 칠하는 색을 달리 할때마다 최종적으로 N번째 집까지 칠했을때의 최소 비용을 비교하며 결과값을 갱신한다.
    result2 = min(result, result2)
print(result2)