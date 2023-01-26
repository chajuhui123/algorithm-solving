import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

matrix = []

n, m = map(int, input().split())

for _ in range(n):
    matrix.append(list(map(int, input().split())))

count = 0

def bfs(sx, sy):
    queue = deque()
    queue.append((sx, sy))
    matrix[sy][sx] = 1

    while queue:
        nx, ny = queue.popleft()

        for i in range(4):
            tx, ty = nx + dx[i], ny + dy[i]

            # 도넛 행성의 특징은 모든 모서리가 하나로 붙어있음. 
            # 따라서 범위 초과시 tx, ty 값을 정리해줘야 함.

            # tx == -1 인 경우는 index length-1 값인 m-1 로 정리
            # tx == m 인 경우는 index 0 으로 정리
            if(tx == -1):
                tx = m - 1
            elif (tx == m):
                tx = 0

            # ty == -1 인 경우는 index length-1 값인 n-1 로 정리
            # tx == m 인 경우는 index 0 으로 정리
            if(ty == -1):
                ty = n - 1
            elif (ty == n):
                ty = 0

            # 비어 있는 칸 (모험이 가능한 칸)
            if(matrix[ty][tx] == 0):
                queue.append((tx,ty)) # 이어서 탐색 (bfs)
                matrix[ty][tx] = 1

for y in range(n):
    for x in range(m):
        if (matrix[y][x] == 0):
            bfs(x,y)
            count += 1

print(count)