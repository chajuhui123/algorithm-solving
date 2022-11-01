# 20044

n = int(input())
nums = list(map(int, input().split()))
nums.sort() # 오름차순 정렬

left = 0
right = len(nums) - 1

# min_value 갱신하며 답 찾아나감 
min_value = 1e9

while left < right :
  temp = nums[left] + nums[right]
  min_value = min(min_value, temp)
  left += 1
  right -= 1

print(min_value)


# IDEA
# 1. 주어진 값 오름차순 정렬
# 2. left index 값과 right rindex 값을 더해, 갱신되는 min_value 보다 작은 값을 갱신해나감
# 3. left는 +1 right -1 하며 최종 min_value 찾음