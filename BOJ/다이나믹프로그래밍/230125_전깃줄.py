# 2565

import sys
input = sys.stdin.readline

n = int(input())

right_arr = []
left_arr = []
same_arr = []

compare = 0

for _ in range(n):
  # 왼쪽 전봇대, 오른쪽 전봇대 대소 관계 비교   
  left, right = map(int, input().split())
  
  if left < right:
    right_arr.append((left, right))
  elif left > right:
    left_arr.append((left, right))
  else:
    same_arr.append((left, right))

target = right_arr if len(left_arr) < len(right_arr) else left_arr
answer = len(target)

exclude_same_item = []
for item in target:
    for same_item in same_arr:
        if item[0] > same_item[0] or item[1] > same_item[0]:
            exclude_same_item.append(same_item[0])

answer = answer - len(list(set(exclude_same_item)))
print(answer)



