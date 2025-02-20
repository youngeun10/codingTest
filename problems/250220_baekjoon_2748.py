# Level: Bronze 1
# Title: 피보나치 수 2

import sys
input = sys.stdin.readline

arr = [0, 1]
for i in range(2, int(input())+1):
    arr.append(arr[i-1] + arr[i-2])
print(arr[-1])
