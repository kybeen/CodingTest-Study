# N과 M(11)
# ==> 15663 문제에서 해당 원소가 쓰였는지 확인하는 check를 없애고, 중복도 포함한 모든 조합을 그냥 다 result에 넣은 뒤 집합으로 변환하여 중복만 제거해준다.

import sys

def dfs():
    if len(stk) == M:
        result.append(tuple(stk[:]))
        return
    for i in range(0,len(num)):
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