# 1922
# 크루스칼 => union find 함수를 통해 해결할 수 있다!

import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기 (간선 연결한다고 생각!)
def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB


node = int(input()) # 노드 수 (컴퓨터 수)
edge = int(input()) # 간선 수 (컴퓨터 연결 짓는 수)

answer = 0
parent = {}
edges = []

for i in range(1, node+1):
    parent[i] = i

for _ in range(edge):
    a, b, value = map(int, input().split())
    edges.append((value, a, b )) # 비용에 따른 오름차순 정렬을 위해 value를 0번째 값으로

edges.sort()

for edge in edges:
    value, a, b = edge
    if find(parent,a) != find(parent,b):
        union(parent,a,b)
        answer += value

print(answer)

# IDEA
# 1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
# 2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
# ㄴ 사이클이 발생하지 않는 경우, 최소 신장 트리에 포함시킨다.
# ㄴ 사이클이 발생하는 경우, 최소 신장 트리에 포함시키지 않는다.
# 3. 모든 간선에 대하여 2번의 과정을 반복한다.