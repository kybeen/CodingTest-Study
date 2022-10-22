# 모든 순열

import sys

# 15663 코드를 활용하여 사전순으로 정렬되도록 스택에 숫자를 추가한 후 result로 순열들을 넣어준다.
def dfs():
    if len(stk) == N:
        result.append(stk[:])   # 순열을 result에 추가
        return
    for i in range(1,N+1):
        if i in stk:
            continue
        stk.append(i)
        dfs()
        stk.pop()

N = int(sys.stdin.readline())
stk = []
result = []

dfs()
for i in result:    # result에 저장된 순열들 출력
    print(*i)