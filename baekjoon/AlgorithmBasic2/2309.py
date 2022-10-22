# 일곱 난쟁이

import sys

height = [0] * 9
for i in range(9):
    height[i] = int(sys.stdin.readline())

summary = sum(height)
comp = summary - 100
out = 0
#  원소 2개의 합이 comp가 되는 경우를 찾으면 나머지 난쟁이들의 키의 합이 100임.
for i in range(8):
    for j in range(i+1,9):
        if height[i] + height[j] == comp:   # 원소 2개의 합이 comp가 되는 경우 찾으면
            fake1 = height[i]
            fake2 = height[j]
            height.remove(fake1)    #   height 리스트에서 제거
            height.remove(fake2)
            out = 1
            break   # 답을 찾았으므로 j for문 빠져나옴
    if out == 1:
        break   # 답을 찾았으므로 i for문도 빠져나옴

height.sort()   # 일곱 난쟁이 정렬 후 출력
for i in height:
    print(i)