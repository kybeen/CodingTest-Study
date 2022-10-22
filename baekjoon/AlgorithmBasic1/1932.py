# 정수 삼각형

import sys

n = int(sys.stdin.readline())
triangle = [0] * n
for i in range(n):
    triangle[i] = list(map(int, sys.stdin.readline().split()))

dp = [item[:] for item in triangle]    # 깊은복사 안되는 이유??
for i in range(1,n):
    for j in range(0,i+1):
        if j == 0:  # 삼각형 층에서 0번 인덱스의 수는 같은 인덱스의 윗층 수만 더할 수 있음.
            dp[i][j] += dp[i-1][0]
        elif j == i:   # 삼각형 층에서 맨 오른쪽 인덱스(i)의 수는 윗층에서  i-1 인덱스의 수만 더할 수 있음
            dp[i][j] += dp[i-1][j-1]
        else:   # 나머지 경우는 윗층의 j-1, j번째 인덱스의 값을 비교한 후, 더 큰 값을 더해준다.
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
print(max(dp[n-1]))


# -----------------------------> 런타임 에러
# import sys

# n = int(sys.stdin.readline())
# triangle = [0] * 500
# for i in range(n):
#     triangle[i] = list(map(int, sys.stdin.readline().split()))

# dp = triangle
# if n >= 1:
#     dp[1][0] += triangle[0][0]  # 삼각형의 두번째 줄은 무조건 맨 꼭대기의 원소와 더한다.
#     dp[1][1] += triangle[0][0]
# if n >= 2:
#     for i in range(2,n):
#         dp[i][0] += dp[i-1][0]
#         for j in range(1,i):
#             dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
#         j += 1
#         dp[i][j] += dp[i-1][j-1]

# print(max(dp[n-1]))