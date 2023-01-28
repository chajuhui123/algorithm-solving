# 1890

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

graph = [list(map(int, input().split())) for i in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

# n * n graph 를 탐색하며 점프를 진행하는 칸 count를 dp에 누적하는 방식 

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:  # 오른쪽 맨 아래 지점에 도달했을 때 (도착)
            print(dp[i][j])
            break
        d_cnt = graph[i][j] # 진행해야하는 칸 수
        # 오른쪽으로 진행
        if j + d_cnt <= n - 1 :
            dp[i][j + d_cnt] += dp[i][j]
        # 아래쪽으로 진행
        if i + d_cnt <= n - 1:
            dp[i + d_cnt][j] += dp[i][j]

# 오답코드

# while len(queue):
#     x, y = queue.pop(0)
#     dp[x][y] += 1

#     if x == n-1 and y == n-1:
#         continue

#     d_cnt = graph[x][y]

#     new_x = x + d_cnt # 아래로 진행하는 경우
#     new_y = y + d_cnt # 오른쪽으로 진행하는 경우

#     if new_x <= n - 1 and y <= n - 1:
#         queue.append((new_x, y))
#     if x <= n - 1 and new_y <= n - 1:
#         queue.append((x, new_y))


# print(dp[n-1][n-1])

# 점프하는 칸마다 앞으로 진행할 아래쪽, 왼쪽 칸을 stack에 쌓아서, 
# 점프 횟수 count를 누적해나갔는데, 시간초과가 떴다.. ㅠㅠㅠ