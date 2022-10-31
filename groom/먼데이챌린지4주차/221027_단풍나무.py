# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# 공원의 크기 n
n = int(input())

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 단풍나무 숲 초기화
graph = []
for _ in range(n):
	line = list(map(int, input().split()))
	graph.append(line)

answer = 0

# 한 바퀴
def checkGraph():
	global answer
	is_more = False
	
	for i in range(n):
		for j in range(n):
			if graph[i][j] != 0:
				is_more = True
				
				for direct in range(4):
					next_x = dx[direct] + i
					next_y = dy[direct] + j

					if next_x >= 0 and next_y >= 0 and next_x < n and next_y < n and graph[next_x][next_y] == 0:
						graph[i][j] -= 1
						# 이전에 단풍 들었던 지역과 구분 
						if graph[i][j] == 0:
							graph[i][j] = -1

	for i in range(n):
		for j in range(n):
			if graph[i][j] <= 0:
				graph[i][j] = 0
	
	if is_more == True:
		checkGraph()
		answer += 1


checkGraph()
print(answer)