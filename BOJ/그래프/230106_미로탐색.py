# 2178

# 1,1 에서 n,m 의 위치로 이동할 때 지나야하는 최소 칸 수

import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000) 

n, m = map(int,input().split())
maze = [list(map(int,list(input().rstrip()))) for i in range(n)]

queue = deque()
visited = [[False for i in range(m)] for i in range(n)]
visited[0][0] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    while queue:
        x, y = queue.popleft()
        # 상하좌우 인접한 노드 방문
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] and visited[nx][ny] == False:
                queue.append([nx, ny])
                visited[nx][ny] = True
                maze[nx][ny] += maze[x][y]
bfs()


print(maze[n][m])
