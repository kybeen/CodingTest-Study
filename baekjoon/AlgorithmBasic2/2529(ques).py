# 부등호 ==> 구글링함.

import sys

def check():
    if len(case) == k+1:
        possible.append(case[:])   # 끝까지 검사를 마친 경우(가능한 경우)면 possible에 추가, case[:]로 append 안하면 얕은복사 됨 자꾸
        return

    for i in range(10):
        if i in case:
            continue
        case.append(i)
        # 숫자 배치가 부등호와 안맞는 경우가 있으면 리턴해서 넘어간다.
        if len(case) >= 2:
            if comp[case.index(case[-2])] == '<' and case[-2] > case[-1]:
                case.pop()
                continue
            elif comp[case.index(case[-2])] == '>' and case[-2] < case[-1]:
                case.pop()
                continue
        check()
        case.pop()

k = int(sys.stdin.readline())   # 부등호 개수 k
comp = list(sys.stdin.readline().split())   # 부등호 입력받은 리스트
possible = [] # 가능한 경우를 모두 담을 리스트
case = []

check()
print(*possible[-1],sep='')
print(*possible[0],sep='')



#----------------------------> 시간초과,PyPy3도 안됨. 알고리즘은 맞는것 같은데 부등호 조건이 안맞는게 생기면 바로 자르도록 재귀함수로 코드 짜기
# import sys
# import itertools

# k = int(sys.stdin.readline())   # 부등호 개수 k
# comp = list(sys.stdin.readline().split())   # 부등호 입력받은 리스트
# result = [] # 가능한 값들을 모두 담을 리스트
# combination = list(itertools.permutations([i for i in range(10)], k+1))   # k+1개의 수로 구성된 가능한 모든 조합들

# for i in range(len(combination)):
#     cbn = combination[i]
#     possible = 0    # 부등호에 만족되는 조합인지 체크하기 위한 변수
#     for i in range(k):
#         # 부등호에 알맞게 숫자가 배치돼있으면 possible을 1씩 카운트
#         if comp[i] == '<' and cbn[i] < cbn[i+1]:
#             possible += 1
#         elif comp[i] == '>' and cbn[i] > cbn[i+1]:
#             possible += 1
#         else:
#             continue
#     # combination은 가능한 조합들을 오름차순으로 반환하므로 첫번째로 나오는 조합이 가장 작은 수고, 마지막으로 나오는 조합이 가장 큰 수잇 것이다.
#     if possible == k:   # 가능한 조합이면 result에 저장
#         result.append(list(cbn))

# print(*result[-1],sep='')
# print(*result[0],sep='')