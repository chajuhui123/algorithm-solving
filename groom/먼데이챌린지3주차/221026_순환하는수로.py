import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**8)
from collections import defaultdict

# 현재 그래프의 상태는 양방향 그래프
n = int(input())
graph = defaultdict(list)

for i in range(n):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [0 for _ in range(n+1)]

circle = list()
finded = -1

# dfs
def FindCycle(u, tar):
    global finded

    # 방문기록이 있다면, 순환구조라고 할 수 있다. 
    # 순환되는 고리는 단 1개이기 때문이다.
    if visited[u] == 1:
        finded = u
        if u not in circle:
            circle.append(u)
        return

    # 방문 기록이 없다면, 방문 기록을 남긴다. Visited변수는 방문 기록을 남긴다.
    visited[u] = 1

    # 도착한 물탱크(노드)에서 갈 수 있는 물탱크들로 물을 보낸다.
    for i in graph[u]:
        # 만약에 i값이 이전의 공급한 물탱크는 탐색 정지
        if i == tar:
            continue

        # 방문한 적 없고, 공급한 물탱크가 아니라면 새로운 탐색지점으로 잡는다. (재귀 시작)
        FindCycle(i, u)

        # 이미 발견된 순환 고리 값이라면 탐색 정지
        if finded == -2:
            return

        # u라면 이미 방문 지점이기때문에 탐색 정지
        if finded == u:
            finded = -2
            return

        # 새롭게 발견한 순환 고리 값이라면 순환 고리에 추가하고, 탐색 종료
        if finded >= 0:
            if u not in circle:
                circle.append(u)
            return

FindCycle(1, 1)

#저장된 순환 값 정렬
circle.sort()

print(len(circle))
for i in circle:
    print(i, end = ' ')


# IDEA
# 모든 물탱크에는 물이 없는 상태에서 시작한다.
# 최초의 하나의 물탱크를 선택하여, 물을 채우고 물탱크에 연결된 다른 물탱크에 물을 공급한다.
# 다른 물탱크에 물을 공급하는 물탱크는 물이 모두 비워질 때까지, 다른 물탱크에 공급한다.
# 순환하는 수로의 정의를 다음과 같이 정의하자. => 어떤 물탱크에 있던 물이 특정한 수로들을 거쳐 다시 원래의 물탱크로 돌아올 때, 그 수로들의 집합을 순환하는 수로라 한다.
# 순환하는 수로의 집합의 크기는 최소 '3개 이상'이어야 한다.