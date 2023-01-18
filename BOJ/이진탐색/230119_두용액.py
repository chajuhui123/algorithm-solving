# 2470

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

start = 0
end = N - 1

answer = 0
answer_start = 0
answer_end = 0

while start <= end:
    sum = arr[start] + arr[end];

    if abs(sum) < answer:
        answer = abs(sum)
        answer_start = arr[start]
        answer_end = arr[end]

    if sum == 0: # sum == 0
        break
    elif sum > 0: # sum == 양수
        end -= 1
    else : # sum == 음수
        start += 1


print("{} {}".format(answer_start, answer_end))