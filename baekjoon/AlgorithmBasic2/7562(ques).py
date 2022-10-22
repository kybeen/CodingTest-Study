# 나이트의 이동 ==> 구글링함(짧은 코드로 푸는법), 근데 같은 위치 두번 가면 안된다는 말 없는데 최소 횟수라 당연히 고려해야하는건지 모르겠음

import sys
import collections

def bfs(y,x):
    global after_a, after_b
    
    # x축과 y축으로 진행 가능한 방향들(dy와 dx의 같은 인덱스의 원소들이 한 쌍임)
    dy = [1, 2, 2, 1, -1, -2, -2, -1] # y축
    dx = [2, 1, -1, -2, -2, -1, 1, 2]   # x축
    dq = collections.deque()
    dq.append((y,x))

    while dq:
        a, b = dq.popleft()
        if a == after_a and b == after_b:
            print(visit[a][b])
            break
        for i in range(8):  # dy와 dx로 진행 가능한 방향들 중 진행 가능한 곳으로 간다.
            y = a + dy[i]
            x = b + dx[i]
            if 0 <= y < l and 0 <= x < l and visit[y][x] == 0:
                dq.append((y,x))
                visit[y][x] = visit[a][b] + 1

testcase = int(sys.stdin.readline())
for i in range(testcase):
    l = int(sys.stdin.readline())   # 체스판의 한 변의 길이
    current_a, current_b = map(int, sys.stdin.readline().split()) # 나이트가 현재 있는 칸
    after_a, after_b = map(int, sys.stdin.readline().split())   # 나이트가 이동하려고 하는 칸
    board = [[0 for i in range(l)] for i in range(l)]   # 체스판
    visit = [item[:] for item in board]

    bfs(current_a,current_b)