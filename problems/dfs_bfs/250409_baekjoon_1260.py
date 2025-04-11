# Level: Silver 2
# Title: DFS와 BFS

import sys
from collections import deque

input = sys.stdin.readline

def bfs(n):
    result = []
    queue = deque([n])
    while queue:
        node = queue.popleft()


    return result

def dfs(n):
    result = []
    queue = deque([n])
    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if chk[n]

    return result


N, M, V = map(int, input().split())
graph = {}
for _ in range(M):
    s, e = map(int, input().split())
    if s not in graph:
        graph[s] = [e]
    else:
        graph[s].append(e)

chk = [False] * N


