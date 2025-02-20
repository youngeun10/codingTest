# Level: Silver 3
# Title: 파일 정리

import sys
input = sys.stdin.readline

resultExp = []
result = {}

for i in range(int(input())):
    a, b = map(str, input().rstrip().split('.'))
    if b in result:
        result[b] += 1
    else:
        resultExp.append(b)
        result[b] = 1
resultExp.sort()
for i in resultExp:
    print(i, result[i])


