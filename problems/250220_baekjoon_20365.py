# Level: Silver 3
# Title: 블로그 2

import sys
input = sys.stdin.readline

n = int(input())
str = str(input().rstrip())
strR = str.replace('B', ' ')
strB = str.replace('R', ' ')

print(min(1+len(strR.split()), 1+len(strB.split())))

