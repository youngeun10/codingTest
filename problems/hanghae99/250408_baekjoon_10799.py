# Level: Silver 2
# Title: 쇠 막대기

import sys

s = sys.stdin.readline().rstrip()

stack = []
cnt = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1] == '(':
            cnt += len(stack)
        else:
            cnt += 1
print(cnt)