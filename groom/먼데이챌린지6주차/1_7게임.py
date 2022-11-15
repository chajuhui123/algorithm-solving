import sys
input = sys.stdin.readline

# 5개의 케이스가 주어진다
for _ in range(5):
	nums = list(map(int, input().rstrip()))
	
	a = 0
	
	for i in range(7):
    # 홀수의 경우 (index가 짝수)
		if i % 2 == 0:
			a += nums[i]
			
	for i in range(7):
		# 짝수의 경우 (index가 홀수)
		if i % 2 == 1 and nums[i] != 0:
			a *= nums[i]
	
	print(a % 10)
			
	