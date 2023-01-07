# 7562

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

for _ in range(t):
    n = int(input())
    now_x, now_y = map(int, input().split())
    to_x, to_y = map(int, input().split())

    q = deque()
    visited = [[0 for _ in range(n)] for __ in range(n)]
    q.append((now_x, now_y))

    while q:
        x, y = q.popleft()
        if x == to_x and y == to_y:
            print(visited[to_x][to_y])
            break
        for i in range(8):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < n and visited[next_x][next_y] == 0:
                q.append((next_x, next_y))
                visited[next_x][next_y] = visited[x][y] + 1