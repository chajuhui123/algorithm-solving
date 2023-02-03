# 9251

import sys 
input = sys.stdin.readline

# 두 개의 수열이 주어짐
# ACAYKP
# CAPCAK

arr1 = list(input().strip())
arr2 = list(input().strip())

# 둘 중에 긴 수열이 arr1
if len(arr1) < len(arr2):
    temp = arr1
    arr1 = arr2
    arr2 = temp

dp = [0] * len(arr1)

for i in range(len(arr1)):
    cnt = 0
    for j in range(len(arr2)):
        if cnt < dp[j]:
            cnt = dp[j] # 현재까지의 최장 공통 부분 수열 갯수
        elif arr1[i] == arr2[j]:
            dp[j] = cnt + 1 # 둘이 겹치는 값이 있어서, 부분 수열이 될 수 있는 경우 count += 1

print(max(dp))
