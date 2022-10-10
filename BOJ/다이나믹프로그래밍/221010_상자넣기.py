n = int(input())
boxes = list(map(int, input().split(' ')))

dp = [1 for _ in range(n)] # dp 초기화 : 박스 하나가 존재하므로 1로 초기화

# 왼쪽에 있는 상자가 오른쪽에 있는 상자보다 크다면 넣을 수 있다.
# 이 때 상자를 가장 많이 담을 수 있는 경우 print
for i in range(1, n):
    for j in range(i):
        if boxes[i] > boxes[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))