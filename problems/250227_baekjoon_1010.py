# Level: Silver 5
# Title: 다리 놓기

import sys
input = sys.stdin.readline

import math

result = []

for _ in range(int(input())):
    a, b = map(int, input().split())
    result.append(math.comb(b, a))

print('\n'.join(map(str, result)))
