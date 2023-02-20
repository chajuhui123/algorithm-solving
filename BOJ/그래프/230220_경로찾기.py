# 11403

import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
    
# 플로이드-워셜
for k in range(n):
    for i in range(n):
        for j in range(n): 
            # [i][j] 에 경로가 존재하는지 혹은
            # k 를 경로로 삼았을 때 [i][k], [k][j] 를 잇는 연결 노드가 존재하는지 검사
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1

for line in graph:
    temp_str_line = list(map(str, line))
    print(" ".join(temp_str_line))
    