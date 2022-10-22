#네 수

import sys
A, B, C, D = sys.stdin.readline().split()

left = A + B
right = C + D
result = int(left) + int(right)

print(result)