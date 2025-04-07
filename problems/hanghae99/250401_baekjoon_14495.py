# Level: Silver 4
# Title: 피보나치 비스무리한 수열

import sys
input = sys.stdin.readline

n = int(input())
arr = [0, 1, 1, 1]

if n > 3:
    for i in range(4, n+1):
        arr.append(arr[i-1] + arr[i-3])
print(arr[n])
