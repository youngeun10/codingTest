#   Silver 4
#   Project Teams

## input
###  n
###  [2n]개의 코딩 역량 (' ' 로 구분 되어있음)
## output
### 팀별 코딩 역량의 min

import sys
n = int(sys.stdin.readline())
capabilityArr = list(map(int, sys.stdin.readline().split()))
capabilityArr.sort()

for i in range(n):
    capabilityArr[i] = capabilityArr[i] + capabilityArr[(len(capabilityArr)-1)-i]

print(min(capabilityArr[0:n]))


