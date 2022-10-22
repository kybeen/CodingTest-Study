# 이분 그래프 ==> 구글링함

import sys
import collections

# 너비 우선 탐색
def bfs(start):
    global possible
    dq = collections.deque()    # 데크 사용
    dq.append(start)
    visit[start] = 1    # 시작 노드는 데크에 넣어주고 색을 1로 칠해준다.
    while dq:
        upper = dq.popleft()    # 데크에서 가장 오래된 원소를 pop한 뒤 upper로 저장
        for i in line[upper]:   # upper의 인접 노드들을 탐색
            if visit[i] == 0:   # 방문하지 않은 노드라면 데크에 추가하고 upper 노드의 색과 반대 색을 칠해준다.
                dq.append(i)
                visit[i] = -visit[upper]
            else:   # 이미 방문한 노드이면서 upper노드와 색이 같으면 안된다. 이 경우가 보이면 possible 변수 1로 바꾼 뒤 바로 리턴
                if visit[i] == visit[upper]:
                    possible = 1
                    return

K = int(sys.stdin.readline())   # 테스트케이스 개수
for i in range(K):
    possible = 0    # YES,NO 판단하는 변수
    V, E = map(int, sys.stdin.readline().split())   # V : 정점의 개수, E : 간선의 개수
    line = [[] for i in range(V+1)]
    visit = [0 for i in range(V+1)] # visit ==> 0 : 방문하지 않은 노드 / 1 : 빨강 / -1 : 파랑
    for i in range(E):  # 간선리스트 입력
        a, b = map(int, sys.stdin.readline().split())
        line[a].append(b)
        line[b].append(a)

    # 그래프가 두개로 나뉘어져 있는 경우도 있을 수 있으므로 모든 노드에 대해서 탐색해 봐야한다.
    for i in range(1,V+1):
        if visit[i] == 0:
            bfs(i)
    
    # 모든 탐색이 끝난 뒤 possible 값에 따라 결과 출력
    if possible == 1:
        print('NO')
    else:
        print('YES')