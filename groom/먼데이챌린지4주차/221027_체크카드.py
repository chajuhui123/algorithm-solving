# queue
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

from collections import deque

# 계좌에 들어있는 잔액 n
# 거래 횟수 m
n, m = map(int, input().split())

q = deque([])

for _ in range(m):
	command, money = input().split()
	money = int(money)
	
	if command == 'deposit':
		n += money
		
	# 대기 목록 확인
	while True:
		if len(q) != 0 and n >= q[0]:
			delete_money = q.popleft()
			n -= delete_money
		else:
			break
	
	# 주어진 금액 k만큼 계좌에서 돈이 결제된다.
	# 단 계좌의 잔액이 money 보다 적다면 결제되지 않는다. 	
	if command == 'pay' and n >= money:
		n -= money
		
	if command == 'reservation':
		# 주어진 금액 money만큼 결제된다.
		# 잔액이 k보다 적거나, 대기 목록에 다른 거래 결제 대기 중이라면 결제 되지 않고 대기 목록 맨 뒤에 추가한다.
		if n >= money and len(q) == 0:
			n -= money
		else:
			q.append(money)
		
print(n)
	
	
	
	