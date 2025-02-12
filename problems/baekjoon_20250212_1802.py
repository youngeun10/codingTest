#   Silver 1
#   종이 접기

## input
###  T: 테스트 케이스 (T < 1000)
###  n (* T 개수 만큼) : 1 - out, 0 - in
## output
### 종이 접기가 가능한지 결과 (YES / NO)
# 가운데 0을 기점으로 양쪽은 0과1로 이루어져야한다?!

import sys
input = sys.stdin.readline

def isAvailableStr(s):
    todo = list(s)

    while len(todo) >= 3:
        for i in range(2, len(todo), 2):
            print('=', i-2, todo[i-2], i, todo[i])
            if todo[i-2] == todo[i]:
                return False

        nextTodo = []
        for i in range(1, len(todo), 2):
            nextTodo.append(todo[i])
        print(nextTodo)

        todo = nextTodo
    return True

T = int(input())
for _ in range(T):
    curInput = str(input().rstrip())

    if isAvailableStr(curInput):
        print("YES")
    else:
        print("NO")