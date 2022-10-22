# 로또 ==> 구글링해서 되긴 되는데 combination 구현이 이해가 잘 안감

import sys

def dfs(start):
    if len(combi) == 6: # 만들어진 조합의 길이가 6이 되면 조합 출력
        print(*combi)
        return
    for i in range(start, k):   # 재귀호출 할 때마다 i의 시작 인덱스를 1씩 증가
        combi.append(testcase[i])
        dfs(i + 1)
        combi.pop() # start가 7이 되면 반복문 실행 안되야 되는거같은데( for i in range(7,6) ) 이 줄(combi.pop())만 실행됨
    
combi = []
while True:
    testcase = list(map(int, sys.stdin.readline().split()))
    if testcase[0] == 0:
        break
    k = testcase[0]
    testcase = testcase[1:]
    dfs(0)
    print()


# import sys

# def dfs(start, depth):
#     if depth == 6:
#         print(*stk)
#         return
#     for i in range(start,len(testcase)):
#         stk[depth] = testcase[i]
#         dfs(start+1, depth+1)

# stk = [0] * 6
# start = 0
# depth = 0
# while True:
#     testcase = list(map(int, sys.stdin.readline().split()))
#     if testcase[0] == 0:
#         break
#     k = testcase[0]
#     testcase = testcase[1:]
#     dfs(start, depth)
#     print()