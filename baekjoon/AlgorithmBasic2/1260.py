# DFS와 BFS --> 구글링함

# import sys
# import collections

# # 깊이 우선 탐색
# def dfs(start):
#     print(start, end = ' ')
#     check[start] = 1    # 출력된 노드는 check리스트에 표시한다.
#     for i in line[start]:
#         if check[i] == 1:   # 방문하지 않은 노드라면 해당 노드를 인자로 받아 dfs로 재귀
#             continue
#         dfs(i)

# # 너비 우선 탐색
# def bfs(start):
#     dq = collections.deque()    # 양방향 큐 (데크deque) --> 리스트보다 연산 속도가 빠름
#     dq.append(start)    # 하위 노드들을 탐색해야 하는 노드를 데크에 저장
#     check[start] = 1
#     while dq:
#         start = dq.popleft()    # 데크의 왼쪽 끝 원소를 pop하고 start에 저장
#         print(start, end = ' ')
#         for i in line[start]:   # 데크에서 pop한 원소의 하위 노드들을 탐색한다. 출력 안한 노드가 있다면 출력.
#             if check[i] == 0:
#                 dq.append(i)
#                 check[i] = 1

# # N : 정점의 개수, M : 간선의 개수, V : 탐색을 시작할 정점의 번호
# N, M, V = map(int, sys.stdin.readline().split())
# line = [[] for i in range(N+1)]
# # 서로 연결된 노드들을 line리스트에 저장
# for i in range(M):
#     a, b = map(int, sys.stdin.readline().split())
#     line[a].append(b)
#     line[b].append(a)
# for i in line:
#     i.sort()    # 작은 수부터 탐색하기 위해 노드들의 연결관계를 나타내는 이차원 리스트 line의 원소들을 정렬한다.
    
# check = [0] * (N+1)
# stk = []
# dfs(V)
# print()
# check = [0] * (N+1)
# bfs(V)





# 2022.06.22
import sys
import collections

def dfs(node):
    visited[node] = 1   # 노드 방문 표시
    print(node, end=' ')
    for i in lines[node]:   # 현재 노드와 연결된 노드들 불러오기 (작은 수부터 탐색해야 하기 때문에 정렬 필요)
        if visited[i] == 0: # 아직 방문하지 않은 노드라면 재귀함수 호출
            dfs(i)  # 재귀함수호출
        else:
            continue
    return

def bfs(node):
    dq = collections.deque()
    dq.append(node)
    visited[node] = 1
    while dq:
        done = dq.popleft()
        print(done, end=' ')
        for i in lines[done]:
            if visited[i] == 0:
                dq.append(i)
                visited[i] = 1
    return


N, M, V = map(int, sys.stdin.readline().split())
lines = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    lines[a].append(b)
    lines[b].append(a)
for row in lines:
    row = row.sort()    # 작은 수부터 탐색하기 위해 정렬해줌

visited = [0 for i in range(N+1)]   # 인덱스 맞추기 위해 의미 없는 칸 1개 있음 (0번 인덱스)
dfs(V)
print()
visited = [0 for i in range(N+1)]
bfs(V)