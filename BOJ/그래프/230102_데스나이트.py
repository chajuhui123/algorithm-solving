# 16948
# 데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수 
# => 최단 경로 문제는 가까운 노드부터 방문하는 BFS 풀이가 유리

import sys
input = sys.stdin.readline

from collections import deque

n = int(input()) # 체스판 크기 n
r1, c1, r2, c2 = map(int, input().split()) # 시작점 r1, c1 도착점 r2, c2
graph = [[-1] * n for _ in range(n)] # -1 이라면 방문하지 않은 노드로 
directions = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)] # 문제에서 주어진 4개의 방향

def bfs(r, c):
    # queue 자료구조 활용. 시작점 초기화
    q = deque() 
    q.append((r, c)) 
    graph[r][c] = 0
    # bfs 를 선택한 이유는 => 최단 경로 문제는 '가까운 노드'부터 방문하는 BFS 풀이가 유리
    while q:
        r, c = q.popleft()
        for direction_r, direction_c in directions:
            R = r + direction_r
            C = c + direction_c
            # 이동가능한 4 방향 검사 후, 체스판 안에 포함되며, 방문하지 않은 곳이면
            if (0 <= R < n) and (0 <= C < n) and graph[R][C] == -1: 
                # queue에 추가하고 이동거리 +1 을 해준다.
                q.append((R, C))
                graph[R][C] = graph[r][c] + 1

bfs(r1, c1)
print(graph[r2][c2]) # 그래프에 누적된 최종 이동거리 출력

# 7
# 6 6 0 1

# 6
# 5 1 0 5

# 7
# 0 3 4 3