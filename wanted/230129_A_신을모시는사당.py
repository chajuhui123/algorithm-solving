import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

curr, answer = 0, 0 # 지금까지 누적값 / 깨달음의 최댓값
min_sum, max_sum = 0, 0 # 지금까지 누적값의 최솟값, 최댓값

for item in arr:
    if item == 1: # 1: 왼쪽 돌상 
        curr += 1
    elif item == 2: # 2: 오른쪽 돌상
        curr -= 1
	
    # 최대 깨달음 갱신
    answer = max(answer, abs(curr - min_sum))
    answer = max(answer, abs(max_sum - curr))
    
    # 최솟값, 최댓값 갱신
    min_sum = min(min_sum, curr)
    max_sum = max(max_sum, curr)

print(answer)