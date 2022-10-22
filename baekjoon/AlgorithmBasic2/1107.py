# 리모컨 ------> 구글링함, 어려움

import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
button = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
if M != 0:  # 고장난 버튼이 있다면
    broken = list(sys.stdin.readline().split())
    for i in broken:    # 고장난 버튼 제거
        button.remove(i)

# +,- 버튼만 눌러서 이동하는 경우
result = abs(N - 100)
# 숫자버튼 먼저 누르고 +,-버튼 누르는 경우
for case in range(1000001):
    case = str(case)
    for i in range(0,len(case)):
        if case[i] not in button:   # 남은 리모컨으로 누를 수 없는 숫자면 break
            break
        if i == len(case) - 1:  # case의 끝까지 검사했을 때, case가 남은 리모컨으로 누를 수 있는 숫자면 +,-로 누르는 횟수도 구한다.
            cnt = len(case) + abs(N-int(case))
            result = min(result, cnt)   # 더 작은 값으로 갱신
print(result)