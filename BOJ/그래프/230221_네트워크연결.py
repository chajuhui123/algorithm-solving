# 1922
# 크루스칼

import sys
input = sys.stdin.readline

INF = float('inf')

node = int(input())
edge = int(input())

graph = [[INF for _ in range(node + 1)] for _ in range(node + 1)]
visited = [ False for _ in range(node + 1)]
distance = [ INF for _ in range(node + 1)]

# 연결관계 초기화
for _ in range(edge):
    computer_l, computer_r, value = map(int, input().split())
    graph[computer_l][computer_r] = value;
    graph[computer_r][computer_l] = value;


def get_min_node():
    min_num = INF
    v = 0
    for idx in range(1, node + 1):
        if visited[idx] == False and distance[idx] < min_num:
            minNum = distance[idx];
            v = idx
    return v

def get_prim(start):
  distance[start] = 0;

  for i in range(1, node + 1):
    min_node = get_min_node()
    visited[min_node] = True
    for j in range(1, node + 1):
        if graph[min_node][j] != INF and visited[j] == False and (graph[min_node][j] < distance[j]):
            distance[j] = graph[min_node][j]

get_prim(1)

print(distance)