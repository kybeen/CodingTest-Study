#소수 구하기

import sys
import math

def Prime(i):
    if i == 1:
        pass
    elif i == 2:
        return i
    else:
        flag = 0
        for j in range(2,int(math.sqrt(i))+1):
            if i%j == 0:
                flag = 1
                break
        if flag == 0:
            return i

M, N = map(int, sys.stdin.readline().split())

for i in range(M,N+1):
    if Prime(i):
        print(Prime(i))