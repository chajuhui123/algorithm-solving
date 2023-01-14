from collections import deque

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

matrix = []
for _ in range(n):
    line = list(map(int, input().split()))
    matrix.append(line)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx <= -1:
            # n으로 초기화
        if nx >= n:
            # 0으로 초기화
        if ny <= -1
            # m 으로 초기화
        if ny >= m:
            # 0으로 초기화
        dfs(nx, ny)

        if matrix[nx][ny] == 0:



answer = 0
for idx_x in range(n):
    for idx_y in range(m):
        if matrix[idx_x][idx_y] == 0 :
            # matrix[x][y] = 1
            dfs(idx_x, idx_y)
            answer += 1

print(answer)


# 5 6
# 1 1 1 1 1 1
# 1 0 0 0 1 1
# 1 1 1 1 0 0
# 1 1 1 1 0 0
# 1 1 1 1 1 1
