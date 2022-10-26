# bfs/dfs, 그래프

import sys
from collections import deque
from collections import defaultdict

input = sys.stdin.readline

n, m, k = map(int, input().split())

# 양방향 그래프
dict = defaultdict(list)
for i in range(m):
    s, e = map(int, input().split())
    dict[s].append(e)
    dict[e].append(s)

q = deque()

visited = [-1 for _ in range(n+1)]
visited[1] = 0

q.append(1)

while q:
    cur = q.popleft()
    for next in dict[cur]:
        if visited[next] != -1:
            continue
        q.append(next)
        visited[next] = visited[cur] + 1
        
if 1 <= visited[n] <= k:
    print("YES")
else:
    print("NO")


# 양방향 그래프가 주어지며, 1번 노드에서 이동 시작하고, k번 이하의 이동으로 n번 노드에 도달할 수 있는지 판단