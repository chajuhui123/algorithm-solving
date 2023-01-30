# 49743919

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split(' ')))
dp = [1] * n

for i in range(1, n):
    cnt = 0
    for j in range(0, i):
        # arr[i] 값과 arr[0] ~ arr[i] 이전 값들 비교해 
        # 더 작은 값인지 (수열을 만들 수 있는지) 검사
        if arr[i] > arr[j]:
            # 가장 긴 수열 값으로 cnt 를 갱신해 나감
            cnt = max(cnt, dp[j]);
    dp[i] += cnt

print(max(dp)) # 가장 긴 부분수열

# IDEA
# 이전에 Node.js 로 풀이했던 문제이다. 
# LIS(Longest Increasing Subsequence)를 구하는 문제 중 가장 기본적인 문제!
