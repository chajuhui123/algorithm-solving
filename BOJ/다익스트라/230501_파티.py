# 1238

import sys
import heapq
input = sys.stdin.readline

n, m, x = map(int, input().split())

# 1. 경로 그래프 초기화 (시작점, 끝점 그리고 소요 시간을 graph 에 초기화)
graph = [[] for _ in range(m+1)]
for _ in range(m):
    road_from, road_to, t = map(int, input().split())
    graph[road_from].append((road_to, t))

# 2. 다익스타라 알고리즘 활용해
def dijkstra(start):
    # 첫 시작 비용은 0으로 초기화
    INF = int(1e9)
    distance = [INF] * (n+1)
    distance[start] = 0

    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        current_dist, current_node = heapq.heappop(queue)
        # 최단 경로가 아니라면 넘긴다
        if current_dist > distance[current_node]: continue
        # 현재 정점과 이어진 정점들을 탐색함
        for next_node, dist in graph[current_node]:
            # 선택된 노드를 거쳐서 인접 노드로 갈 때의 거리
            next_dist = dist + current_dist
            
            if next_dist < distance[next_node]:
                # 기존의 dist보다 작다면 교체하고, 다음 노드에 다음 dist를 넣어준다.
                distance[next_node] = next_dist
                heapq.heappush(queue, (next_dist, next_node))

    return distance

# 3. n 명의 학생들의 비용 검사
result = 0
for i in range(1, n + 1):
    # 목적지 x로 가는 최단 경로
    go_to_x = dijkstra(i)
    # 출발지 home으로 가는 최단 경로
    back_to_home = dijkstra(x)
    result = max(result, go_to_x[x] + back_to_home[i])

print(result)