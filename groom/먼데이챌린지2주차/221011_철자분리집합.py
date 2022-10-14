# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

n = int(input())
s = list(input())

answer = n

for idx in range(1, n):
	if s[idx] == s[idx-1]: answer -= 1

print(answer)

