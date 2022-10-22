# N과 M(1) ------> 구글링함, 백트래킹 사용
# ==>파이썬에서 리스트 자료형은 mutable(변경 가능)하기 때문에 함수 안에서 global로 전역변수 선언을 따로 하지 않아도 된다.
# ==> 하지만 int 자료형 같은 변수는 immutable(변경 불가)하기 때문에 함수 안에서 전역변수로 사용하려면 global 선언을 따로 해줘야 한다.

import sys

N, M = map(int, sys.stdin.readline().split())
stk = []

def dfs():
    if len(stk) == M:   # 스택의 길이가 M이랑 같아지면 스택의 원소들을 출력하고 리턴
        print(' '.join(map(str,stk)))
        return
    for i in range(1,N+1):
        if i in stk:    # 중복되는 숫자는 무시하기 위해 스택에 있는 숫자일 경우 continue로 넘긴다.
            continue
        stk.append(i)
        dfs()   # 호출된 dfs에서 수열이 출력되고 리턴되면 다음 숫자로 바꿔주기 위해 스택의 마지막 원소를 pop해준다.
        stk.pop()

dfs()