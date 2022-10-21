# 11659

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

# 누적합 저장할 배열 prefix_sum
prefix_sum = [0]
temp = 0
for num in nums: 
    temp += num
    prefix_sum.append(temp)

# prefix_sum 활용해 합 구하기
for _ in range(m):
    start, end = map(int, input().split())
    print(prefix_sum[end] - prefix_sum[start-1])

# IDEA
# 구간합을 저장하는 배열을 활용해서 풀지 않으면, 시간 복잡도 O(NM)이 되어 시간 내에 해결하지 못한다.
# 배열을 활용하면 전체 구간 합을 구하는 작업도 O(N+M) 시간에 끝낼 수 있어서 통과 가능하다.