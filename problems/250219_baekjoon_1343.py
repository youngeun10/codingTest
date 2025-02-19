# Level: Silver 5
# Title: 폴리오미노

import sys
input = sys.stdin.readline

s = str(input().rstrip())
# arr = s.split('.')
# a = 'AAAA'
# b = 'BB'
# result = ''
#
# for t in arr:
#     if t == '':
#         result += '.'
#     else:
#         if len(t) % 2 == 0:
#             result += a * (len(t) // 4)
#             n = len(t) % 4
#             result += b * (n // 2)
#             result += '.'
#         elif len(t) % 2 == 1:
#             result = -1
#             break
# if result != -1:
#     print(''.join(result[0:len(result)-1]))
# else:
#     print(result)

### 풀이
def solution(str):
    str = str.replace('XXXX', 'AAAA').replace('XX', 'BB')
    if 'X' in str:
        return -1
    else:
        return str
print(solution(s))