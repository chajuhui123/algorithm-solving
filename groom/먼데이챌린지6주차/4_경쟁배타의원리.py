# 정확히 개의 종이 공존할 때만 경쟁이 일어난다. 종의 수가 보다 작거나 많다면 경쟁이 일어나지 않고 공생하며 살아간다.
# 경쟁 배타의 원리가 일어나는 영역의 총 넓이 = 정확히 K개의 종이 살고 있는 영역의 넓이

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
L = 1004
ans = 0

S = [[0 for _ in range(L)] for _ in range(L)]
for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    S[y1][x1] += 1
    S[y1][x2] -= 1
    S[y2][x1] -= 1
    S[y2][x2] += 1
    
# 가로로 복원
for i in range(L):
    for j in range(1, L):
        S[i][j] += S[i][j - 1]
        
# 세로로 복원
for j in range(L):
    for i in range(1, L):
        S[i][j] += S[i - 1][j]
    
for i in range(L):
    for j in range(L):
        if S[i][j] == K: ans += 1
        
print(ans)

# 누적합