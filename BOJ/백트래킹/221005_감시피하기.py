# 18428

def backTracking(cnt):
    global flag
    # 3개의 장애물을 설치했다면
    if cnt == 3:
        # 선생님의 위치에서 감시를 한다.
        if bfs():
            # 장애물 3개를 설치하였을 때, 감시 피하기 성공한 경우
            flag = True # 성공했다면 flag를 true로 초기화 
            return
    else:
        # 모든 빈공간에 장애물을 3개씩 설치해본다.
        for x in range(n):
            for y in range(n):
                if graph[x][y] == "X":
                    graph[x][y] = "O"
                    backTracking(cnt + 1) # backTracking
                    graph[x][y] = "X" # 백트래킹이 끝나면 O를 다시 X로 변경


# bfs를 통해 감시
def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for t in teacher:# 선생님의 위치에서
        for k in range(4): # 상/하/좌/우 탐색
            nx, ny = t

            while 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == "O":
                    break

                # 학생이 보이면 실패
                if graph[nx][ny] == "S":
                    return False

                # 직선 방향으로 계속해서 탐색
                nx += dx[k]
                ny += dy[k]

    # 모두 통과하면 학생이 안보이는 것으로 성공
    return True


n = int(input())
flag = False
graph = []
teacher = []

# 반복문을 통해 복도 정보를 입력 받는다.
for i in range(n):
    data = list(input().strip().split(" "))
    graph.append(data)
    for j in range(n):
        if graph[i][j] == "T": # 선생님이 있는 좌표를 저장
            teacher.append([i, j])

backTracking(0)

if flag:
    print("YES")
else:
    print("NO")

# IDEA
# 1. 백트래킹을 통해 모든 위치를 탐색하는 것을 기본으로 한다.
# 2. 우선 3개의 장애물을 설치하고, 선생님의 위치에서 상하좌우 직진 방향으로 bfs 탐색을 하며 학생이 있는지 확인한다.
## (3개의 장애물 설치 과정)
## 2-1. 모든 빈 공간에 장애물을 3개 설치한다.
## 2-2. 장애물을 설치한 곳에 "X" -> "O"로 초기화
## 2-3. 장애물이 3개 설치한 후 탐색이 끝나면, 백트래킹을 통해 "O"를 "X"로 초기화한 후, 다음 위치에 장애물을 설치한다.