# 1707

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def check_bipartite_graph(start, group):
    global check_group
    if check_group: return

    visited[start] = group

    for i in temp_graph[start]:
        if visited[i] == 0 :
            # 인접한 두 노드는 그룹을 바꿔서 저장 (편의상 1, -1로 표현)
            check_bipartite_graph(i, -group) 
        # 두 인접한 노드가 1, 1 혹은 -1, -1 로 같은 경우 == 같은 그룹에 존재하는 경우, 이분 그래프가 아님
        elif visited[start] == visited[i]:
            check_group = True
            return

TC = int(input())

for _ in range(TC):
    V, E = map(int, input().split()) # 정점 V, 간선 E

    temp_graph = [[] for i in range(V+1)]
    visited = [0] * (V + 1)

    for _ in range(E):
        # 인접한 두 정점 u, v 의 연결 관계 초기화
        u, v = map(int, input().split())
        temp_graph[u].append(v)
        temp_graph[v].append(u)

    check_group = False
    for i in range(1, V+1): # 1~V 정점 탐색
        if visited[i] == 0 :
            check_bipartite_graph(i, 1)

    print("NO") if check_group else print("YES")


# IDEA
# 1. 서로 인접한 노드가 같은 그룹에 속하면 '이분 그래프가 아님'
# 2. 모든 노드 방문시에 같은 그룹에 속하는 인접한 노드가 없다면 '이분 그래프가 맞음'
# => DFS (깊이 우선 탐색)을 활용하여, 모든 노드에 대해 인접한 노드가 서로 같은 그룹으로 연결되어있는지 파악하면서 이분 그래프 여부를 판단할 수 있음

# 0. 이분 그래프는 1 혹은 -1 이라는 그룹으로 나뉘어지는 것으로 정의함. 탐색하지 않은 노드는 기본적으로 0
# 1. DFS 알고리즘으로 그래프에 대한 노드를 탐색할 때, 두 인접한 노드는 1, -1 각각 다른 그룹에 속하게 초기화함 (visited 에 저장)
# 2. 탐색 진행시, 인접한 노드의 그룹이 현재 탐색 중인 노드와 동일한 그룹이면, 이분그래프가 아님 (1==1 혹은 -1==-1)
# 3. 모든 노드 탐색 종료에도, 위 케이스가 없다면 이분그래프

# 2
# 3 2
# 1 3
# 2 3
# 4 4
# 1 2
# 2 3
# 3 4
# 4 2