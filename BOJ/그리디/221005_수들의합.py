# 1789

s = int(input())

count = 0
sum = 0

while sum <= s:
    sum += count
    count += 1

if sum >= s:
    count -= 2

print(count)