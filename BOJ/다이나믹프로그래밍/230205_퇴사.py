
# 14501

n = int(input())
arr = []

dp = [0] * n

for i in range(n):
    t, p =  map(int, input().split()) # 기간 t, 금액 p
    arr.append((t,p))

for i in range(len(arr)-2, -1, -1): # 역순으로 탐색
    if arr[i][0]+i <= n: # 날짜를 초과하지 않을 경우.
        dp[i] = max(arr[i][1] + dp[i + arr[i][0]], dp[i+1])   
    else:
        dp[i] = dp[i+1]

print(dp[0])