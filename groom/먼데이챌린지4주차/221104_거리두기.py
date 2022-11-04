import sys
input = sys.stdin.readline

n = int(input())

divisor = 100000007

dp = [[0]*5 for i in range(n+1)]

for i in range(5):
    dp[1][i] = 1
		
for i in range(2, n+1):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3] + dp[i-1][4]) % divisor
    dp[i][1] = (dp[i-1][0] + dp[i-1][2] + dp[i-1][3]) % divisor
    dp[i][2] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][3] + dp[i-1][4]) % divisor
    dp[i][3] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % divisor
    dp[i][4] = (dp[i-1][0] + dp[i-1][2]) % divisor
		
# 최종적으로 구하고자하는 값
print((dp[n][0] + dp[n][1] + dp[n][2] + dp[n][3] + dp[n][4]) % divisor)