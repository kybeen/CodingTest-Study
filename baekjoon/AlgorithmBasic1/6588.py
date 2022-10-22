#골드바흐의 추측 ---> 크기에 맞게 에라토스테네스 체 함수 돌려서 찾는것보다 백만짜리 배열 한번에 만들어놓고 찾는게 더 빠른듯

import sys
import math

#에라토스테네스의 체(소수 구하기)
prime_num_list = [True] * 1000001
for i in range(2, 1001):
    if prime_num_list[i] == True:
        for j in range(i+i, 1000001, i):
            prime_num_list[j] = False

while True:
    wrong_flag = 1
    n = int(sys.stdin.readline())
    if n == 0:
        break

    for i in range(3,n):
        if prime_num_list[i] == True and prime_num_list[n-i] == True:
            wrong_flag = 0  #조합이 존재하면 0
            print(f'{n} = {i} + {n-i}')
            break
    if wrong_flag == 1:
        print("Goldbach's conjecture is wrong.")



# def prime_list(n):  #에라토스테네스의 체(소수 구하는 함수)
#     prime = [True] * n
#     for i in range(2, int(math.sqrt(n))+1):
#         if prime[i] == True:
#             for j in range(i+i, n, i):
#                 prime[j] = False
#     return [i for i in range(3, n) if prime[i] == True]

# while True:
#     n = int(sys.stdin.readline())
#     if n == 0:
#         break

#     prime_num_list = prime_list(n)
#     wrong_flag = 1
#     for i in prime_num_list:
#         temp = n - i
#         for j in prime_num_list[::-1]:
#             if j == temp:
#                 wrong_flag = 0
#                 print(f'{n} = {i} + {j}')
#                 break
#         if wrong_flag == 0:
#             break

#     if wrong_flag == 1:
#         print("Goldbach's conjecture is wrong.")