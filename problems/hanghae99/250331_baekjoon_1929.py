# 소수 구하기 -> '에라토스테네스의 체' 를 이용하기
# https://www.acmicpc.net/problem/1929

import sys
from math import sqrt

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [i for i in range(n, m+1)]
sArr = set(arr)
if 1 in sArr: sArr.remove(1)

for i in range(2, int(sqrt(m)+1)):
    tmp = i
    while tmp <= m:
        tmp += i
        if tmp in sArr:
            sArr.remove(tmp)
result = list(sArr)
result.sort()
print(*result, sep='\n')

