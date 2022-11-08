# 10816

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))
nums.sort()

answer = []

for target in targets:
    left_pointer, right_pointer = 0, n-1
    contain = 0 

    while left_pointer <= right_pointer:
        mid = (left_pointer + right_pointer) // 2
        if target == nums[mid]:	
            contain = nums[left_pointer:right_pointer+1].count(target)
            break
        elif target > nums[mid]: # nums[mid]가 target보다 작다면
            left_pointer = mid + 1
        else: # nums[mid]가 target보다 크다면
            right_pointer = mid - 1

    answer.append(contain)

print(" ".join(str(item) for item in answer))