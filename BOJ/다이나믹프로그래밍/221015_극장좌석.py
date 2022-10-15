# 2302

n = int(input())
m = int(input())
vips = [int(input()) for _ in range(m)]

dp =  [0 for _ in range(n + 2)]
dp[0] = 1
dp[1] = 1 # 그대로 자리 착석한 경우 (1)
dp[2] = 2 # 자리를 바꿔앉은 경우, 자리를 안바꿔 앉은 경우. 총 2가지 (1,2 / 2,1)

# 점화식 : dp[n] = dp[n - 1] + dp[n - 2]
if (n > 2):
    for i in range(3, n + 2):
        dp[i] = dp[i - 1] + dp[i - 2]


# vip 좌석 사이에 있는 좌석들 경우의 수를 확인해주기
answer = 1
if m > 0:
    pre_vip = 0
    for vip in vips:
        answer *= dp[vip - 1 - pre_vip] # 현재 vip 위치 - 1 - 이전 vip 위치
        pre_vip = vip # 이전 vip 위치 갱신
    answer *= dp[n - pre_vip]
else:
    answer = dp[n]

print(answer)