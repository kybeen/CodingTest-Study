# 링크와 스타트 ==> PyPy3로 제출해야 맞음. Python3 시간초과.
# ==> 시간초과 줄이는법?

import sys
import itertools

N = int(sys.stdin.readline())
stat = [[0 * N] for i in range(N)]  # 능력치 표
for i in range(N):
    stat[i] = list(map(int, sys.stdin.readline().split()))
result = sys.maxsize    # 비교를 위해 result의 초기값은 가장 큰 수
people = [i for i in range(N)]

for i in range(1,N//2+1):   # 어차피 link팀은 전체 인원과 start팀의 차집합이기 때문에 start팀의 조합은 절반인원까지만 구한다.
    team = list(itertools.combinations( [i for i in range(N)], i )) # 1명일때부터 N-1명일때까지의 가능한 조합을 만든다.
    for j in range(0,len(team)):
        # 거르는거 없어도 되나ㅇ
        start = list(team[j])
        link = [x for x in people if x not in start]    # people과 start의 차집합
        start_sum = 0
        link_sum = 0

        # start팀 능력치 총합
        for m in range(len(start)):
            for n in range(len(start)):
                start_sum += stat[start[m]][start[n]]

        # link팀 능력치 총합
        for m in range(len(link)):
            for n in range(len(link)):
                link_sum += stat[link[m]][link[n]]

        result = min(result ,abs(start_sum - link_sum)) # 차이가 더 작은 값으로 갱신

print(result)