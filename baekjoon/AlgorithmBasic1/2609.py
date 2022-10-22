#최대공약수와 최소공배수

import math
import sys

A, B = map(int, sys.stdin.readline().split())

ans1 = math.gcd(A,B)
ans2 = math.lcm(A,B)
print(f'{ans1}\n{ans2}')