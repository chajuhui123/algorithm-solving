# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

n, k = map(int, input().split(' '))

people = []

for _ in range(n):
	name, height = list(input().split(' '))
	people.append((name, height))
	
# 첫번째 요소가 같다면, 두 번째 요소 비교하게 됨
answer = " ".join(sorted(people)[k-1])
print(answer)
	