# 1309

n = int(input())

# dp 초기화. 첫 줄은 3가지 선택지 중, 1가지 선택을 할 수 있는 것으로 시작
dp = [[0, 0, 0] for _ in range(n+1)]
dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1

# 2번째 줄부터 시작
# 새로운 타일로 넘어왔을 때 3가지 선택이 가능하다.
# 1. 아무것도 선택 안하기 dp[i][0] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2] (모든 경우의 수 가능)
# 2. 왼쪽 타일 선택하기  dp[i][1] = dp[i-1][0] + dp[i-1][2] (오른쪽 타일, 안칠하기 경우 가능)
# 3. 오른쪽 타일 선택하기  dp[i][2] = dp[i-1][0] + dp[i-1][1] (왼쪽 타일, 안칠하기 경우 가능)
for i in range(2, n + 1):
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % 9901
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % 9901

# 사자를 배치하는 경우의 수를 9901로 나눈 나머지 print
print(sum(dp[n]) % 9901)


