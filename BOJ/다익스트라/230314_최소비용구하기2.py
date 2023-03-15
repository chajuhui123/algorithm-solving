# 11779

import sys, heapq

import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

# 경로 그래프 초기화
graph = [[] for _ in range(n+1)]
for _ in range(m):
    city_from, city_to, w = map(int, input().split())
    graph[city_from].append((city_to, w))

start, end =map(int, input().split())

INF = int(1e9)
distance = [INF] * (n+1) # 비용 초기화 
node_relations = [start] * (n + 1) # 노드 간의 연결관계를 갱신


def dijkstra(start):
    queue = []
    # 첫 시작 비용은 0으로 초기화
    distance[start] = 0
    heapq.heappush(queue, [0, start])   

    while queue:
        current_weight, current_node = heapq.heappop(queue)

        if distance[current_node] < current_weight:
            continue

        # 연결 되어 있는 노드로 이동한다면
        for next_node, weight in graph[current_node]:     
            next_weight = weight + current_weight
            # 현재 distance에 저장되어 있는 비용보다,
            # 다음 노드를 거쳐 갈 때 비용이 더 적다면 
            if next_weight < distance[next_node]:      
                distance[next_node] = next_weight
                node_relations[next_node] = current_node
                heapq.heappush(queue, [next_weight, next_node])
                

def search_node(end):
    relation = []
    search_node = end

    while search_node != start:
        relation.append(str(search_node))
        search_node = node_relations[search_node]

    relation.append(str(start))
    relation.reverse()
    return relation

dijkstra(start)
result_relation = search_node(end)

print(distance[end]) # 출발 도시에서 도착 도시까지 가는데 드는 최소 비용
print(len(result_relation)) # 최소 비용을 갖는 경로에 포함되어있는 도시의 개수
print(' '.join(result_relation)) # 최소 비용을 갖는 경로를 방문하는 도시 순서대로 출력


# IDEA

# 다익스트라 알고리즘

# (최소 비용을 갖는 경로를 방문하는 도시 순서?) 최단경로 값이 <갱신>될 때, 갱신되는 노드 값을 함께 저장한다.

# 마지막 node인 end의 가장 가까운 노드를 구하고, 
# 그 노드의 가장 가까운 노드를 구하는 과정을
# 시작 노드 start 가 나올 때까지 반복한다.
# 해당 순서를 뒤짚으면 최단 경로 리스트이다.