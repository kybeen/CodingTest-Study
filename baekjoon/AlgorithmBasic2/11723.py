# 집합

import sys

M = int(sys.stdin.readline())
S = set()   # 빈 집합 생성
for i in range(M):
    command = list(sys.stdin.readline().split())

    # 커맨드 하나짜리일때
    if len(command) == 1:
        if command[0] == 'all': # S를 {1, 2, ..., 20} 으로 바꾼다.
            S = set([i for i in range(1,21)])   # 리스트로 생성 후 자료형 변경
        elif command[0] == 'empty': # S를 공집합으로 바꾼다.
            S = set()
    
    # 커맨드 두개짜리 일때
    else:
        command[1] = int(command[1])

        if command[0] == 'add': # S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
            S.add(command[1])
        elif command[0] == 'remove': # S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
            S.discard(command[1])
        elif command[0] == 'check': # S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
            if command[1] in S:
                print('1')
            else:
                print('0')
        elif command[0] == 'toggle': # S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
            if command[1] in S:
                S.discard(command[1])
            else:
                S.add(command[1])