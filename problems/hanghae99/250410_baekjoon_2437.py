# Level: Gold 2
# Title: 저울

import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
weight = list(map(int, input().split()))
weight.sort()

cnt = 1

for w in weight:
    if cnt < w:
        break
    cnt += w
print(cnt)


