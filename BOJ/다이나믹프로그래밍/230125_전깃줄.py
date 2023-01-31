# 2565

import sys
input = sys.stdin.readline

n = int(input())

lines = []
dp = [0] * n

for _ in range(n):
  A, B = map(int, input().split())
  lines.append((A, B))

lines.sort()

for i in range(n):
    for j in range(i): # 0 ~ i-1
        if lines[i][1] > lines[j][1] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(n - max(dp))
