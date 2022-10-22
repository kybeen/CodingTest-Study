# 날짜 계산 -----> 구글링함

import sys

E, S, M = map(int, sys.stdin.readline().split())
result = 0
e, s, m = 0, 0, 0

while(True):
    # e,s,m과 결과로 출력할 값 result를 계속해서 1씩 더해줌
    e += 1
    s += 1
    m += 1
    result += 1
    if e > 15:  # e는 15보다 커지면 1로 돌아감
        e = 1
    if s > 28:  # s는 28보다 커지면 1로 돌아감
        s = 1
    if m > 19:  # m은 19보다 커지면 1로 돌아감
        m = 1
    if e == E and s == S and m == M:    # e,s,m이 모두 같아지면 반복문 빠져나온다.
        break

print(result)