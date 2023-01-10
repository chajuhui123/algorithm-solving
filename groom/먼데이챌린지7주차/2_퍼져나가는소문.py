import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

G = [[] for _ in range(n + 1)]
V = [0 for _ in range(n + 1)]

# 입력 받을 친구들간의 연결 관계 초기화
for _ in range(m):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
    
def dfs(cur):
    # cur 과 연결되어 있는 
    for next in G[cur]:
        if V[next]: 
            continue
        V[next] = 1
        dfs(next)
        
V[1] = 1
dfs(1)
print(sum(V))

# IDEA
# 구름이는 n명의 친구가 있고, 그 친구들 중에는 m쌍의 친구 관계가 있다.
# 구름이가 만약 어떤 친구에게 소문을 퍼뜨리게 된다면, 그 소문은 친구의 친구, 친구의 친구의 친구... 를 타고 퍼져나갈 것이다.
# 1번 친구에게 소문을 퍼뜨렸을 때, 그 소문을 듣게 될 친구가 몇 명이나 될지를 구해보기.
# 하나의 연결 컴포넌트에 있는 정점의 개수를 세는 그래프 문제