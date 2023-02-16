# 18352

# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4

import sys
import heapq
input = sys.stdin.readline

# 도시의 개수 (정점 갯수) N, 도로의 개수 (간선 갯수) M, 거리 정보 K, 출발 도시의 번호 X
n, m, k, x = map(int, input().split())

# 비용을 무한으로 초기화 
INF = int(1e9)
distance = [INF] * (n+1)

# 경로 그래프 초기화
graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append((end, 1)) # 경로 연결 관계 graph에 저장


def dijkstra(start):
    queue = []
    # 첫 시작 비용은 0으로 초기화
    distance[start] = 0
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
                

dijkstra(x)

answer = []
for idx in range(1, n+1):
    if distance[idx] == k:
        answer.append(idx)

answer.sort()

if len(answer):
    print("\n".join(map(str, answer)))
else:
    print(-1)
