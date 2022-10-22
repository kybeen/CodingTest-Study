#골드바흐 파티션

import sys
import math

#에라토스테네스의 체(소수 구하기) -------------> 100만크기의 배열을 한번에 미리 만들어 두고, 수를 입력받았을 때는 찾기만 하는 방식
prime_num_list = [True] * 1000001
for i in range(2, 1001):
    if prime_num_list[i] == True:
        for j in range(i+i, 1000001, i):
            prime_num_list[j] = False

T = int(sys.stdin.readline())
for i in range(0,T):
    N = int(sys.stdin.readline())
    cnt = 0
    for i in range(2,N//2+1):
        if prime_num_list[i] == True and prime_num_list[N-i] ==True:
            cnt += 1
    print(cnt)


#--------------------------------> 되는데 시간초과 (수를 입력받을 떄마다 입력받은 수의 크기만큼 에라토스테네스의 체 함수 실행함)
# import sys
# import math

# def Eratos(n):
#     lst = [True]*n
#     lst[1] = False
#     cnt = 0
#     for i in range(2 , int(math.sqrt(n))+1):
#         if lst[i] == True:
#             for j in range(i+i, n, i):
#                 lst[j] = False
#     for i in range(3,N//2+1):
#         if lst[i] == True and lst[n-i] == True:
#             cnt += 1
#     print(cnt)

# T = int(sys.stdin.readline())
# for i in range(0,T):
#     N = int(sys.stdin.readline())
#     result = Eratos(N)