# 1260

import sys
input = sys.stdin.readline

from collections import deque

n, m, v = map(int, input().split()) # 정점 개수 n, 간선 개수 m, 탐색 시작 정점 v

# 1. 그래프 초기화를 위한 2중배열 선언, dfs, bfs 정점 방문 여부를 위한 리스트 선언
graph = [[0] * (n + 1) for _ in range(n + 1)] 
dfs_visit_list = [0] * (n + 1)
bfs_visit_list = [0] * (n + 1)

# 2. 그래프 연결 관계 초기화
for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = graph[b][a] = 1

# 3. 재귀 방식의 dfs 그래프 탐색
def dfs(v):
  # 시작 정점 v 방문
  dfs_visit_list[v] = 1     
  print(v, end = " ")
  # 연결된 정점 중 방문하지 않은 정점이 있다면 탐색 => 깊은 정점으로 탐색됨
  for i in range(1, n + 1):
    if dfs_visit_list[i] == 0 and graph[v][i] == 1:
      dfs(i)

# 2. Queue 활용한 bfs 그래프 탐색
def bfs(v):
  q = deque()
  q.append(v)
  bfs_visit_list[v] = 1  
  # queue가 비기 전까지    
  while q:
    # 먼저 탐색된 순서대로 노드 방문=> 특정 정점과 연결되어있는 모든 정점을 우선 탐색하면서 넓게 탐색됨
    v = q.popleft()
    print(v, end = " ")
    # 연결된 정점 중 방문하지 않은 정점이 있다면, queue에 넣어줌
    for i in range(1, n + 1):
      if bfs_visit_list[i] == 0 and graph[v][i] == 1:
        q.append(i)
        bfs_visit_list[i] = 1

dfs(v)
print('')
bfs(v)

# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4