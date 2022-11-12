import sys
input = sys.stdin.readline

# TIP
# 파이썬의 기본 재귀 한도는 1000이라고 한다.
# 반드시 재귀 한도를 높여줘야 문제를 해결할 수 있다.

sys.setrecursionlimit(12345)

def DFS(cur, prev):
    cy, cx = cur
    for k in range(4):
        ny, nx = cy + dy[k], cx + dx[k]
        if ny < 0 or nx < 0 or ny >= n or nx >= m:
            continue
        if visit[ny][nx] or not sand[ny][nx]:
            continue
        visit[ny][nx] = 1
        DFS([ny, nx], cur)

n, m = map(int, input().split())

sand = []
for i in range(n):
    sand.append(list(map(int, input().split())))
        
# DFS 탐색시 방문 여부
visit = [[0 for _ in range(m)] for _ in range(n)]

# 
upd = [[0 for _ in range(m)] for _ in range(n)]

# 방향정의
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

t = 0

while 1:
    island = 0

    for i in range(n):
        for j in range(m):
            if visit[i][j] or not sand[i][j]:
                continue
            visit[i][j] = 1
            island += 1
            DFS([i, j], [i, j])
    
    # 섬이 2개 이상
    if island >= 2 :
        print(t)
        exit(0)

    # 모든 칸이 물
    if island == 0:
        print(-1)
        exit(0)
  
    for i in range(n):
        for j in range(m):
            for k in range(4):
                ni, nj = i + dy[k], j + dx[k]
                if ni < 0 or nj < 0 or ni >= n or nj >= m: continue
                if not sand[ni][nj]:
                    upd[i][j] = 1
                    
    for i in range(n):
        for j in range(m):
            if upd[i][j]:
                sand[i][j] = 0
    
    for i in range(n):
        for j in range(m):
            upd[i][j] = visit[i][j] = 0
    t += 1

# IDEA
# 0은 물로 가라 앉은 영역, 1은 모래 영역이다.
# 모래 영역 1 의 상하좌우에 0이 존재하면 해당 영역은 0으로 변한다.
# 1. 모래섬이 두 개의 영역으로 나뉘어지는지 체크하는 로직,
# 그리고 2. 상하좌우 탐색하며 0으로 바꾸는 로직 을 작성하면 해결할 수 있다.