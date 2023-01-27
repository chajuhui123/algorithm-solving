# 16395

import sys
input = sys.stdin.readline

pascal = [[1 for _ in range(i)] for i in range(1, 31)] 

# 조건 : 1 <= k <= 30
for i in range(2, 30):
    for j in range(1, i):
        pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j] # 파스칼 삼각형 규칙에 따라 값을 저장해놓음

n, k = map(int, input().split())

print(pascal[n-1][k-1])