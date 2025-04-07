# Level: Silver 3
# Title: 수열

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
result = sum(arr[:K])
for i in range(1, N):
    arr[i] = arr[i] + arr[i-1]
for i in range(K, N):
    result = max(result, arr[i]-arr[i-K])
print(result)