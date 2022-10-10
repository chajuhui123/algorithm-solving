# 2293

n, k = map(int, input().split())
coins = [int(input()) for i in range(n)]
dp = [0 for _ in range(k+1)]
dp[0] = 1 # 동전을 하나만 쓰는 경우 1로 초기화 # dp[1] = dp[1] + dp[0] (dp[1] = 0 + 1) 만족 (dp[j] = dp[j] - dp[j-i] 성립가능함)

for coin in coins:
    for now in range(coin, k+1):
        if now - coin >= 0:
            dp[now] += dp[now - coin]

print(dp[k])
