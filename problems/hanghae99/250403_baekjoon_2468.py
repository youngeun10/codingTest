# Level: Silver 1
# Title: 안전 영역

import sys
from collections import deque

input = sys.stdin.readline

def bfs(i, j, c):
    queue = deque([(i, j)])
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    size = 1

    while queue:
        y, x = queue.popleft()
        for dy, dx in d:
            Y, X = y + dy, x + dx
            if (0 <= Y < n) and (0 <= X < n) and graph[Y][X] >= c and chk[Y][X] == False:
                chk[Y][X] = True
                queue.append((Y, X))
                size += 1
    result.append(size)

n = int(input())
result = []
graph = []
chk = [[False] * n for _ in range(n)]
cArr = set()
resultValue = 0
for _ in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    for i in tmp:
        cArr.add(i)

for c in cArr:
    chk = [[False] * n for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= c and chk[i][j] == False:
                chk[i][j] = True
                bfs(i, j, c)
    resultValue = max(resultValue, len(result))
print(resultValue)
