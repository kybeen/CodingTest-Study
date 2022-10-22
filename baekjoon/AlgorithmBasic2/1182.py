# 부분수열의 합

import sys

def sol(start):
    global result
    if len(sub) >= 1 and sum(sub) == S:
        result += 1
    
    for i in range(start,len(arr)):
        if check[i] == 1:
            continue
        sub.append(arr[i])
        check[i] == 1
        sol(i+1)
        sub.pop()
        check[i] == 0

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
result = 0
sub = []
check = [0] * N

sol(0)
print(result)