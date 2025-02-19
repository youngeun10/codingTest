# Level: Bronze 2
# Title: 피보나치 수 5

import sys
input = sys.stdin.readline

n = int(input())
arr = [0, 1]
for i in range(2, n + 1):
    arr.append(arr[i-2] + arr[i-1])
print(arr[n])