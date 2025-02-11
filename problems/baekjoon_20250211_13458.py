### Bronze 2
### 시험 감독

import sys
room = int(sys.stdin.readline())
students = list(map(int, sys.stdin.readline().split()))
main, sub = map(int, sys.stdin.readline().split())

result = 0

for n in students:
    result += 1
    n = n - main

    if n > 0:
        if n // sub == 0:
            if n > 0:
                if n - sub < 0:
                    result += 1
        else:
            if n % sub == 0:
                result += (n // sub)
            else:
                result += (n // sub) + 1

print(result)

'''
n = int(input())
arr = map(int,input().split())
b,c = map(int,input().split())

sol = 0
for i in arr:
    sol +=1
    i = i-b
    if i>0: 
        sol+=i//c
        if i%c !=0 : sol+=1
print(sol)
'''
