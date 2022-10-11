n = input()
nums = list(map(int, input().split(' ')))

answer = 1

for num in nums:
	answer *= num
	
print(answer)

# IDEA

# 경로의 수를 파악하는 경우의 수 문제이다.
# n개의 다리를 모두 이용하여, 다시 1번 섬으로 돌아올 때의 가능한 경로 갯수를 구하므로, 곱의 법칙을 이용하는 문제이다.