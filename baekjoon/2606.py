# 바이러스
import sys
import collections

N = int(sys.stdin.readline())   # 컴퓨터의 수
M = int(sys.stdin.readline())   # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
linked = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    linked[a].append(b)
    linked[b].append(a)

result = 0
visited = [0 for i in range(N+1)]
dq = collections.deque()
dq.append(1)
visited[1] = 1
while dq:
    now = dq.popleft()
    for i in linked[now]:
        if visited[i] == 0:
            dq.append(i)
            visited[i] = 1
            result += 1 # 1번 컴퓨터를 통해 웜 바이러스에 감염되는 컴퓨터의 수를 구해야 하므로 while문 시작 전 dq에 1을 넣어주는 것은 카운트하지 X
print(result)