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
    cnt = 1
    for j in range(i): # 0 ~ i-1
        # lines[i][0] > lines[j][0] 일 때, lines[i][1] > lines[j][1] 
        if lines[i][1] > lines[j][1]:
            # 교차하지 않는 수열 조건에 만족하면, 이전 dp에서 길이 1 추가 
            # 최장 부분 수열을 구하기 때문에 max 값으로 갱신
            cnt = max(cnt, dp[j] + 1)
    dp[i] += cnt

print(n - max(dp))

# IDEA
# 증가하는 부분수열 LIS에 대한 응용 문제이다.
# 문제에서 요구하는 답은 교차하지 않기 위해 '제거해야할 최소 개수' 
# 전깃줄의 개수 (n) - 부분수열의 최장 길이 (LIS)
# DP에는 교차하지 않는 수열의 최장 길이를 갱신해나갈 것이다.
# A 전봇대 기준으로 정렬하고 B를 검사하는 방식으로 진행한다.
# B 전봇대가 증가하는 부분 수열 (=> 교차되지 않음) 이라면 DP 갱신해나간다.