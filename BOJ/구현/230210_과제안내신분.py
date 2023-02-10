# 5597

import sys
input = sys.stdin.readline


nums = [i for i in range(1, 31)]

for _ in range(28):
    num = int(input())
    nums.remove(num)

nums.sort()

print(nums[0])
print(nums[1])