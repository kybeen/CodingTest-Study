# N과 M(10)

import sys

def dfs():
    if len(stk) == M:
        result.append(tuple(stk[:]))
        return
    for i in range(0,len(num)):
        if check[i] == 1 or (len(stk) >= 1 and num[i] < stk[-1]):   # 15663번 코드에서 이부분 조건만 바꿈
            continue
        stk.append(num[i])
        check[i] = 1
        dfs()
        stk.pop()
        check[i] = 0

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
stk = []
result = []
check = [0] * len(num)


num.sort()
dfs()
result = sorted(list(set(result)))
for i in result:
    for j in i:
        print(j, end=' ')
    print()