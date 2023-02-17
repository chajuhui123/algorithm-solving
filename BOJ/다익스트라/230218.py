import sys; input = sys.stdin.readline
from heapq import heappush, heappop

def dijkstra(start, end):
    dis = [0xffffff] * (N + 1)
    dis[start] = 0
    q = [[0, start]]
    while q:
        k, u = heappop(q)
        if k > dis[u]: continue
        for w, v in G[u]:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                heappush(q, [dis[v], v])

    return dis[end]

N, E = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append([w, v])
    G[v].append([w, u])

a, b = map(int, input().split())
