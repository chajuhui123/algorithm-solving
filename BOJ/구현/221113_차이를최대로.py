# 10819

import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# 순열을 활용해, 가능한 모든 순서를 구함
all_cases = list(permutations(A))

# 최대값을 갱신해나감
answer = 0

for case in all_cases:
    # 문제에서 주어진 | a - b | 값을 더하는 변수 
    mid_sum = 0
    for i in range(N - 1):
        mid_sum += abs(case[i] - case[i + 1])
    answer = max(mid_sum, answer)

print(answer)

# IDEA
# 문제의 분류는 백트래킹으로 분류되어있었으나,
# 순열(순서 고려)을 활용하여, 모든 순열에서의 합을 구한 후 최대 값을 갱신하는 로직으로 진행해도 된다고 생각하였다.