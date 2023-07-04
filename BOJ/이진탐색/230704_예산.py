# 2512

import sys
input = sys.stdin.readline

N = int(input())
requests = list(map(int, input().split())) # requests : 각 지방의 예산 요청
M = int(input()) # M : 목표하는 총 예산

start, end = 0, max(requests)
total_request = 0

# 이진 탐색
while start <= end: # start와 end가 같아지면 (조건 만족하는 상한선 구함!)
    mid = (start+end) // 2 
    total_request = 0

    for request in requests: # 해당 mid 값을 상한가로 한 경우에 대해 예산 연산
        total_request += mid if request > mid else request


    # 연산된 예산이 M 초과하면, 더 작은 범위로
    if total_request > M:
        end = mid - 1
    # 연산된 예산이 M 이하라면, 더 큰 범위로
    else:
        start = mid + 1

print(end)