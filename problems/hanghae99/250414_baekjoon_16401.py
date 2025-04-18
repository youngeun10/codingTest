# Level: 
# Title: 

import sys
input = sys.stdin.readline

M, N = map(int, input().split())
snack = list(map(int, input().split()))

start = 1
end = max(snack)

answer=0
while start <= end:
    mid = (start + end) // 2

    cnt=0
    for x in snack:
        if x < mid:
            continue
        else:
            cnt += x // mid

    if cnt >= M:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)
