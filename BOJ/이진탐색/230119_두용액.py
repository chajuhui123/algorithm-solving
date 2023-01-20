# 2470

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr.sort() # arr[start] 와 arr[end] 값을 활용해 sum 값을 탐색할 것이므로 정렬 필요

start = 0
end = N - 1

answer = float('inf')
answer_start = 0
answer_end = 0

while start < end:
    sum = arr[start] + arr[end];

    # 두 용액의 합 (절대적 차이) 가 가장 작은 값을 구해야 함
    if abs(sum) < answer:
        answer = abs(sum)
        answer_start = arr[start]
        answer_end = arr[end]

    if sum == 0: # sum == 0
        break
    elif sum > 0: # sum == 양수. 0과 가깝게 하기 위해 sum 을 줄여야 하므로 end 를 -1 줄여서 다시 탐색함
        end -= 1
    else : # sum == 음수. 0과 가깝게 하기 위해 sum 을 늘려야 하므로 end 를 +1 늘려 다시 탐색함
        start += 1


print("{} {}".format(answer_start, answer_end))