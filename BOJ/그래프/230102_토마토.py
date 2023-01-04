# 7576

from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split()) # 상자의 가로칸 m, 세로칸 n

# 1. 입력받은 토마토 2중 리스트로 초기화 (1, 0, -1 중 하나의 값)
tomato_box = [list(map(int, input().split())) for _ in range(n)] 

# 2. bfs 활용함 (queue)
# ㄴ 인접한 상하좌우가 먼저 익고 (bfs는 인접한 노드 우선 방문)
# ㄴ 토마토가 익는 최소 일수를 구해야하므로 bfs 유리
queue = deque([])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

# 3. 토마토가 존재하는 칸을 queue에 저장
for r in range(n):
    for c in range(m):
        if tomato_box[r][c] == 1:
            queue.append([r, c])

def bfs():
    while queue:
        x, y = queue.popleft()
        # 상하좌우 인접한 노드 방문
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            # tomato_box 범위 안에 들고, 아직 익지 않은 토마토라면 queue에 넣고
            # 해당 칸까지 토마토가 익는데 걸리는 일수를 기존의 tomato_box에 누적하여 저장해줌
            if 0 <= nx < n and 0 <= ny < m and tomato_box[nx][ny] == 0:
                tomato_box[nx][ny] = tomato_box[x][y] + 1
                queue.append([nx, ny])

bfs()

# 4.익지 않은 토마토 있는지 검사 및 토마토가 익는데 걸린 일수 (answer) 저장
# Q. Python 2중 배열에서 가장 큰 값 찾을 수 있나 ? 일단 for 문으로 작업해둠
for r in tomato_box:
    for c in r:
        if c == 0:
            print(-1) # 익지 않은 토마토가 있다면
            exit(0) # 프로그램 종료 
    answer = max(answer, max(r)) # 가장 큰 값이 토마토가 익는데 걸린 값!

# 처음에 시작한 1값은 => 토마토가 익은 위치를 표현한 1이었기 때문에, answer - 1 을 해줌!
print(answer - 1)