# Level: Silver 4
# Title: 별 찍기 - 19

# 4n-3 * 4n-3 만큼의 박스가 필요

import sys
input = sys.stdin.readline

# d 시작점
def fillBoxes(d, size, box):

    # 가로
    for i in range(size-(2*d)):
        box[d][d+i] = '*'
        box[size-d-1][d+i] = '*'

    # 세로
    if size-(2*d) > 1:
        for i in range(1, size-(2*d)):
            box[d+i][d] = '*'
            box[d+i][size-d-1] = '*'

    return box

n = int(input())
size = (4 * n) - 3
box = [[' ']*size for _ in range(size)]

for d in range(0, n):
    box = fillBoxes(d*2, size, box)

for b in box:
    print(''.join(b))