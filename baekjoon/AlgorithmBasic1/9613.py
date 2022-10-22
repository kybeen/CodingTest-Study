#GCD 합

import sys
import math
import itertools

t = int(sys.stdin.readline())
for i in range(t):
    lst = list(map(int,sys.stdin.readline().split()))
    pair = list(itertools.combinations(lst[1:], 2)) #itertools.combinations(리스트,숫자) -> 인자로 받은 숫자의 리스트의 원소들의 모든 조합을 리턴
    sum = 0
    for i in range(0,len(pair)):
        sum += math.gcd(pair[i][0],pair[i][1])
    print(sum)