# Level: Silver 3
# Title: 병든 나이트

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
visited = [[False] * M for _ in range(N)]
root = [False] * 4
def chk():
    dx = [1, 2, 2, 1]
    dy = [-2, -1, 1, 2]
    queue = deque([(0, 0)])
    cnt = 0
    while queue:
        bx, by = queue.popleft()
        print(queue)
        for i in range(4):
            x = bx + dx[i]
            y = by + dy[i]
            print(x, y)
            if 0 <= x < N and 0 <= y < M and not visited[x][y]:
                if cnt > 4:
                    if False in root:
                        continue
                    else:
                        visited[x][y] = True
                        queue.append((x, y))
                        cnt += 1
                else:
                    visited[x][y] = True
                    queue.append((x, y))
                    cnt += 1
                    root[i] = True
    return cnt
print(chk())

