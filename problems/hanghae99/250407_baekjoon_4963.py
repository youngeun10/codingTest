# Level: Silver 2
# Title: 섬의 개수

import sys
from collections import deque

input = sys.stdin.readline
result = []

def dfs(i, j):
    queue = deque([(i, j)])
    d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    while queue:
        x, y = queue.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append((nx, ny))

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    chk = [[False] * w for _ in range(h)]
    result = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                graph[i][j] = 0
                result += 1
                dfs(i, j)
    print(result)

