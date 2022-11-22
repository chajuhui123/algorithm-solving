# 11724
import sys
input = sys.stdin.readline

def dfs(start):
    visited[start] = True # 해당 노드 방문체크

    # 해당 시작점을 기준으로 dfs 탐색 (연결되어 있는 노드들 탐색)
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

# n 정점의 갯수, m 간선의 갯수
n, m = map(int, input().split())
# 점들의 연결관계가 저장된 graph
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    # 양 끝 점 u, v가 m개 주어진다.
    u, v = map(int, input().split())
    # 두 점이 연결되게끔 graph 초기화
    graph[u].append(v)
    graph[v].append(u)
    
visited = [False] * (1 + n)
count = 0  

for i in range(1, n+1):
    if not visited[i]:  # 만약 i번째 노드를 방문하지 않았다면
        if not graph[i]:  # 만약 해당 정점이 연결된 그래프가 없다면
            count += 1  # 개수를 + 1
            visited[i] = True  # 방문 처리
        else:  # 연결된 그래프가 있다면
            dfs(i)  # dfs탐색을 돈다. (이 과정에서 연결된 노드는 visited 체크됨)
            count += 1  # 개수를 +1

print(count)

# IDEA
# 방향 없는 그래프가 주어졌을 때, 연결되어 있는 점들의 묶음을 구하는 문제!
# 해당 문제는 DFS(혹은 BFS)로 해결할 수 있으며, 노드들의 연결 관계를 graph 자료 구조에 저장해 하나씩 탐색한다. 
# 이때 visited 배열을 선언하여, 방문했는지 체크하면서 몇 개의 연결(=덩어리, 묶음)이 존재하는지 확인할 수 있다.