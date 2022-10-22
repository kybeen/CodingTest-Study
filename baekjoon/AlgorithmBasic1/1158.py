#요세푸스 문제

import sys

N, K = map(int, sys.stdin.readline().split())
circle = [i for i in range(1,N+1)]
result = []
index = 0

for j in range(N):
    index += K-1
    if index >= len(circle):
        index = index%len(circle)
    else:
        pass
    
    result.append(str(circle.pop(index)))

print(f"<{', '.join(result)}>")