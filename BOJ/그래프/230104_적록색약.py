# 10026
# 적록 색약은 빨강 === 초록으로 인식, 적록 색약인 사람과 아닌 사람이 보는 구역의 수를 출력

import sys
input = sys.stdin.readline
# 로직에 문제 없는데도 계속 뜨는 RecursionError
# 알고보니 파이썬 자체에서 최대 재귀 한도가 적용되어 무한 루프를 발생하지 않도록 막아뒀기 때문에, 재귀 제한이 있다.
# 아래 셋팅을 추가하여 제한을 푼다.
sys.setrecursionlimit(100000) 

n = int(input())
matrix = [list(map(str, input())) for _ in range(n)]# 입력받은 그림 2차원 배열로 초기화

visited_1 = [[0] * n for _ in range(n)] # 방문 여부 배열
visited_2 = [[0] * n for _ in range(n)] # 방문 여부 배열

# dfs 선정 이유 =>
# 연결된 그래프에서 연관있는 색을 연속적으로 탐색하는 것이므로
# 깊이 있는 노드까지 탐색하는 dfs, 가까이 있는 노드를 우선 탐색하는 bfs 모두 적용 가능하다고 생각한다.
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 적록 색약이 아닌 경우 
def dfs_1(x, y):
    visited_1[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # n*n 범위 안에 들고, 탐색을 시작한 값과 같고, 방문하지 않았다면
        if 0 <= nx < n and 0 <= ny < n and matrix[x][y] == matrix[nx][ny] and visited_1[nx][ny]==0:
            dfs_1(nx, ny)

# 적록 색약인 경우
def dfs_2(x, y):
    visited_2[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # n*n 범위 안에 들고, 탐색을 시작한 값과 같고, 방문하지 않았다면
        if 0 <= nx < n and 0 <= ny < n and visited_2[nx][ny]==0:
            # 탐색을 시작한 값과 같거나
            # R or G 이면
            if (matrix[x][y] == matrix[nx][ny]) or (matrix[x][y] == "R" and matrix[nx][ny] == "G" ) or (matrix[x][y] == "G" and matrix[nx][ny] == "R" ):
                dfs_2(nx, ny)

# 구역의 수
cnt_1 = 0 
cnt_2 = 0

for i in range(n):
    for j in range(n):
        if visited_1[i][j] == 0:
            cnt_1 += 1
            dfs_1(i, j)
        if visited_2[i][j] == 0:
            cnt_2 += 1
            dfs_2(i, j)

print(cnt_1, cnt_2)

# 5
# RRRBB
# GGBBB
# BBBRR
# BBRRR
# RRRRR