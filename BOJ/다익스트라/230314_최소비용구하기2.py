# 11779

import sys, heapq

import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

# 비용을 무한으로 초기화 
INF = int(1e9)
distance = [INF] * (n+1)

# 경로 그래프 초기화
graph = [[] for _ in range(n+1)]
for _ in range(m):
    city_from, city_to, w = map(int, input().split())
    graph[city_from].append((city_to, w))

start, end =map(int, input().split())

def dijkstra(start):
    queue = []
    # 첫 시작 비용은 0으로 초기화
    distance[start] = 0
    heapq.heappush(queue, [0, start])

    while queue:
        current_weight, current_node = heapq.heappop(queue)
      
        if distance[current_node] < current_weight: continue

        for next_node, weight in graph[current_node]:     
            next_weight = weight + current_weight

            if next_weight < distance[next_node]:      
                distance[next_node] = next_weight
                heapq.heappush(queue, [next_weight, next_node])
                
dijkstra(start)


print(distance[end])
print(distance)
