# N과 M(12)

import sys

def dfs():
    if len(stk) == M:
        result.append(tuple(stk[:]))
        return
    for i in range(0,len(num)):
        if len(stk) >= 1 and num[i] < stk[-1]:   # 기존 문제에서 check리스트 빼고, 같은 수 여러번 가능 & 비내림차순 조건 추가
            continue
        stk.append(num[i])
        dfs()
        stk.pop()

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
stk = []
result = []

num.sort()
dfs()
result = sorted(list(set(result)))
for i in result:
    for j in i:
        print(j, end=' ')
    print()