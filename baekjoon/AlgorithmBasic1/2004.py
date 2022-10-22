#조합 0의 개수 -> 팩토리얼을 소인수분해 했을때 2와 5의 개수 중 더 작은걸 구한다
#푸는데도 오래걸리고, 이해하는데도 오래걸림;;

import sys

def count_two(n):
    two = 0
    while n != 0:
        n = n // 2
        two += n
    return two

def count_five(n):
    five = 0
    while n != 0:
        n = n // 5
        five += n
    return five

n, m = map(int, sys.stdin.readline().split())
print(min(count_two(n)-count_two(m)-count_two(n-m), count_five(n)-count_five(m)-count_five(n-m)))




# @@답은 나오는데 시간초과
# import sys
# import math

# n, m = map(int, sys.stdin.readline().split())

# bio = int(math.factorial(n) / (math.factorial(n-m)*math.factorial(m)))
# sum = 0
# result = str(bio)
# if result[-1] == '0':
#     sum += 1
#     i = -2
#     while result[i] == '0':
#         sum += 1
#         i -= 1
# print(sum)