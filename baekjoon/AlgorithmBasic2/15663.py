# N과 M(9)

import sys

def dfs():
    if len(stk) == M:
        result.append(tuple(stk[:]))    # 중복되는 조합은 제거하기 위해 결과를 바로 출력하지 않고 result에 넣는다. (출력될 리스트를 튜블 자료형으로 바꿔서 넣는다.)
        return
    for i in range(0,len(num)):
        if check[i] == 1:   # 이 문제에서는 스택에 들어간 값 자체만 보는게 아니라 어떤 원소가 들어갔는지를 봐야 하기 때문에, 입력받은 num리스트와 같은 크기의 check리스트로 스택에 들어갔는지를 판단한다.
            continue
        stk.append(num[i])
        check[i] = 1    # num리스트에서 해당 인덱스의 원소 값이 스택에 들어가면 check리스트에서 해당 인덱스 값을 1로 바꾼다.
        dfs()
        stk.pop()
        check[i] = 0    # 스택에서 나간 수는 check리스트에서의 값을 다시 0으로 돌린다.

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
stk = []
result = []
check = [0] * len(num)


num.sort()
dfs()
result = sorted(list(set(result)))  # result리스트에서 중복되는 조합들은 집합으로 바꾸면서 없앤 뒤 다시 리스트로 바꾸고 정렬한다.
for i in result:
    for j in i:
        print(j, end=' ')
    print()