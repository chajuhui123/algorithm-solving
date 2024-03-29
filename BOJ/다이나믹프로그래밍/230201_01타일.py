# 1904

import sys
input = sys.stdin.readline

n = int(input())
dp = [0, 1, 2]

# 1 ≤ N ≤ 1,000,000
for idx in range(3, 1000001):
    dp.append((dp[idx-1] + dp[idx-2]) % 15746) # 문제에서 메모리 초과 이슈 때문에 15746로 나눴을 때의 나머지를 return 하게 함

print(dp[n])

# IDEA
# n = 0 인 경우, 없음
# n = 1 인 경우, 1 => 1개
# n = 2 인 경우, 00, 11 => 2개
# n = 3 인 경우, 001, 111, 100 => 3개 
# n = 4 인 경우, 0000, 1111, 0011, 1100, 1001 => 5개
# n = 5 인 경우, 00001, 10000, 00100, 11100, 00111, 10011, 11001, 11111 => 8개
# 01 타일의 갯수는 점화식으로 표현할 수 있으며, dp를 활용할 수 있다.
# dp[n] = dp[n-1] + dp[n-2] (n>=2) 가 성립한다.
