# Level: Silver 3
# Title: 한국이 그리울 땐 서버에 접속하지

import sys
input = sys.stdin.readline

N = int(input())
pattern = input().rstrip().split('*')
arr = [input().rstrip() for _ in range(N)]
result = []

for i in range(N):
    if arr[i].startswith(pattern[0]) and arr[i].endswith(pattern[1]):
        if len(arr[i]) < len(pattern[0]) + len(pattern[1]):
            result.append("NE")
        else:
            result.append("DA")
    else:
        result.append("NE")
print(*result, sep="\n")