#단어 뒤집기

import sys

T = int(sys.stdin.readline())

for i in range(0,T):
    text = sys.stdin.readline().split()
    for j in text:
        print(j[::-1], end = ' ')
    print("")