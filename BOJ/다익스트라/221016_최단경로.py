# 1753

import sys
input = sys.stdin.readline

import heapq

# 정점 갯수 v, 간선 갯수 e
v, e = map(int, input().split())

# 시작점 start
start = int(input())

# 비용을 무한으로 초기화 
INF = int(1e9)
distance = [INF] * (v+1)

# 경로 그래프 초기화
graph = [[] for _ in range(v+1)]
for _ in range(e):
    # 시작 정점 u, 도착 정점 v, 가중치 w
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

queue = []

def dijkstra(start):
    # 첫 시작 비용은 0으로 초기화
    distance[start] = 0
    heapq.heappush(queue, [0, start])

    while queue:
        current_weight, current_node = heapq.heappop(queue)
        # 최단 거리가 아니라면 차례 넘김
        if distance[current_node] < current_weight: continue
        # 현재 정점과 이어진 정점들을 탐색함
        for next_node, weight in graph[current_node]:
            # 선택된 노드를 거쳐서 인접 노드로 갈 때의 가중치
            next_weight = weight + current_weight
            if next_weight < distance[next_node]:
                # 기존의 가중치보다 작다면 교체하고, 다음 노드에 다음 가중치를 넣어준다.
                distance[next_node] = next_weight
                heapq.heappush(queue, [next_weight, next_node])
                
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in distance[1:]:
    print(i if i != INF else "INF")


# IDEA
# 백준에 제출할 때 readline 설정 안하면 시간초과 날 수 있는 거 이제 알았다...
# 분명 전형적인 그래프 -> 최단경로 : 다익스트라 문제인데 왜 안되는거지 ㄱ-.. 했는데 input에 대한 시간초과 때문이였어!!
# 로직엔 이상이 없는듯 하다!! 그래프 노드 간의 가중치를 검사하고, 최단으로 가중치를 갱신하며 최단 경로를 찾아가는 문제!