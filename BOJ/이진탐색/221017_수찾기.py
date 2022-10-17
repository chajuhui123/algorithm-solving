# 1920

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))
nums.sort()

for target in targets:
    left_pointer, right_pointer = 0, n-1
    is_contain = False # target이 nums에 있는지 체크

    while left_pointer <= right_pointer:
        mid = (left_pointer + right_pointer) // 2

        if target == nums[mid]:	
            is_contain = True
            break
        elif target > nums[mid]: # nums[mid]가 target보다 작다면
            left_pointer = mid + 1
        else: # nums[mid]가 target보다 크다면
            right_pointer = mid - 1

    print(1 if is_contain else 0)