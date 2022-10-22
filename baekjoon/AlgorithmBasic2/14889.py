# 스타트와 링크 ==> Python3로 하면 시간초과 뜨는데, PyPy3로 하면 맞음. 알고리즘은 맞음.

import sys
import itertools

N = int(sys.stdin.readline())
stat = [[0 * N] for i in range(N)]  # 능력치 표
for i in range(N):
    stat[i] = list(map(int, sys.stdin.readline().split()))
result = sys.maxsize    # 비교를 위해 result의 초기값은 가장 큰 수

start = list(itertools.combinations( [i for i in range(N)], N//2 )) # 인원수의 절반만큼 가능한 모든 조합을 start에 저장
for i in start:
    start2 = list(i)
    start_sum = 0
    link_sum = 0
    link = [i for i in range(N)]
    for j in range(0,len(i)):
        link.remove(i[j])   # start에 있는 사람을 빼서 link 구성
    
    # start팀 능력치 총합
    for i in range(len(start2)):
        for j in range(len(start2)):
            start_sum += stat[start2[i]][start2[j]]

    # link팀 능력치 총합
    for i in range(len(link)):
        for j in range(len(link)):
            link_sum += stat[link[i]][link[j]]

    result = min(result ,abs(start_sum - link_sum)) # 차이가 더 작은 값으로 갱신

print(result)




# # --------------------------> 속도 개선한 코드, Python3로 채점해도 맞음
# import sys
# import itertools

# N = int(sys.stdin.readline())
# stat = [[0 * N] for i in range(N)]  # 능력치 표
# for i in range(N):
#     stat[i] = list(map(int, sys.stdin.readline().split()))
# result = sys.maxsize    # 비교를 위해 result의 초기값은 가장 큰 수

# team = list(itertools.combinations( [i for i in range(N)], N//2 )) # 인원수의 절반만큼 가능한 모든 조합을 team에 저장
# for i in range(len(team)//2):
#     # team에 들어있는 조합들은 순서대로 돼있기 때문에 [i]조합은 [-1-i]조합과 완전히 반대임
#     start = team[i]
#     link = team[-1-i]
#     start_sum = 0
#     link_sum = 0

#     # start팀 능력치 총합
#     for j in range(N//2):
#         for k in range(N//2):
#             start_sum += stat[start[j]][start[k]]

#     # link팀 능력치 총합
#     for j in range(N//2):
#         for k in range(N//2):
#             link_sum += stat[link[j]][link[k]]

#     result = min(result ,abs(start_sum - link_sum)) # 차이가 더 작은 값으로 갱신

# print(result)