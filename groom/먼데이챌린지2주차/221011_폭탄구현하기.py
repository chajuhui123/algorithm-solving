# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

n, k = map(int, input().split(' '))

graph = [0 for _ in range(n)]
count = 0

dx = [0, 0, -1 ,1]
dy = [1, -1, 0, 0]

for _ in range(k):
	x,y = map(int, input().split(' '))
	
	count += 1
	
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		
		if nx > 0 and ny > 0 and nx <= n and ny <= n:
			count += 1

print(count)