# 2559

import sys
input = sys.stdin.readline


n, k = map(int, input().split())
nums = list(map(int, input().split()))

# for i in range(n - k + 1):
#     # i부터 i+k 구간까지 합(연속 k개의 합)이 answer의 후보가 될 수 있음
#     result.append(sum(a[i : i+k]))
        
# # 그 중 가장 큰 값 리턴
# print(max(result))
# 하지만 해당 방법은 시간 초과. (2 <= N <= 100,000)

result = [sum(nums[:k])]

for i in range(n - k):
    # 기존에 저장한 결과 값에서 이전 값을 제외하고 이후값을 더해 값들을 구하는 방식
    # 이전 수열의 합산 값 - 현재 값 (i, 현재 수열 첫 번째 위치하는 값) + 다음 값 (k+i, 현재 수열 마지막에 위치하는 값) 
    result.append(result[i] - nums[i] + nums[k+i])
        
print(max(result))