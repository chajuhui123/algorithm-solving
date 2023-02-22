# 1717
# 크루스칼 => union find 함수를 통해 해결할 수 있다!

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 특정 원소가 속한 집합을 찾기 (같은 집합에 속하는지 확인하기 위한 함수)
def find(parent, x):
    if parent[x] != x:
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

n, m = map(int, input().split())

parent = {}

for i in range(n+1):
    parent[i] = i

for _ in range(m):
    prefix, a, b = map(int, input().split())

    if (prefix == 0):
        union(parent,a,b)
    else:
        print( 'YES' if find(parent,a) == find(parent,b) else 'NO' )