# 2563

import sys
input = sys.stdin.readline

n = int(input())
arr = [[0 for _ in range(101)] for __ in range(101)]

for _ in range(n):
    x, y = map(int, input().split())

    for x_area in range(x, x+10):
        for y_area in range(y, y+10):
            arr[x_area][y_area] = 1

result = 0
for line in arr:
    result += line.count(1)
    
print(result)