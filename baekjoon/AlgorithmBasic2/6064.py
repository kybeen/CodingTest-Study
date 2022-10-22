# 카잉 달력
# ==> 처음엔 그냥 풀었는데 시간초과뜸. 구글링 해봤더니 수학적으로 접근해서 풀어야함

import sys
import math

T = int(sys.stdin.readline())
for i in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())

    while True: # x에 계속 M을 더해간다.
        if (x-y) % N == 0:  # x(+M)에서 y를 뺸 값이 N으로 나누어 떨어지면 답
            print(x)
            break
        if x > (N * M) // math.gcd(M,N):   # x(+M)가 N과M의 최소공배수를 넘어가면 답이 존재하지 않는 경우이므로 -1 출력
            print('-1')
            break
        x += M

#---------------------------------> 틀림
# import sys
# import math

# T = int(sys.stdin.readline())
# for i in range(T):
#     M, N, x, y = map(int, sys.stdin.readline().split())
#     lcm = (M*N) // math.gcd(M,N)
    
#     for i in range(x, lcm+1, M):
#         if i % N == y:
#             print(i)
#             break
#     i += M
#     if i > lcm:
#         print('-1')


#-----------------------------> 시간초과
# import sys
# import math

# T = int(sys.stdin.readline())
# for i in range(T):
#     x1, y1, year = 1, 1, 1
#     M, N, x, y = map(int, sys.stdin.readline().split())
#     while True:
#         if x1 == x and y1 == y: # 답을 찾으면 출력
#             print(year)
#             break
#         if year > M * N // (math.gcd(M,N)): # year가 M,N의 최소공배수보다 커지는 경우(끝까지 검사했는데 답이 없는 경우)
#             print('-1')
#             break
#         if x1 < M:
#             x1 += 1
#         else:
#             x1 = 1
#         if y1 < N:
#             y1 += 1
#         else:
#             y1 = 1
#         year += 1