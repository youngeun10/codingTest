# Level: Sliver 2
# Title: 리그 오브 레전설
import math
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cnt = 0

result = 0
while N >= cnt:
    result += math.comb(N, cnt)
    N -= (M-1)
    cnt += 1
print(result%1000000007)

