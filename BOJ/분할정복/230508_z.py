# 1074

n, r, c = map(int, input().split())

ans = 0

# 1. Z모양으로 1, 2, 3, 4분면을 어떤 규칙을 통해 탐색하는지 파악 
while n != 0:
	n -= 1

    # 1사분면에 해당
	if r < 2 ** n and c < 2 ** n:
		ans += ( 2 ** n ) * ( 2 ** n ) * 0

    # 2사분면에 해당
	elif r < 2 ** n and c >= 2 ** n: 
		ans += ( 2 ** n ) * ( 2 ** n ) * 1
		c -= ( 2 ** n )

    # 3사분면에 해당 
	elif r >= 2 ** n and c < 2 ** n: 
		ans += ( 2 ** n ) * ( 2 ** n ) * 2
		r -= ( 2 ** n )
		
    # 4사분면에 해당    
	else:
		ans += ( 2 ** n ) * ( 2 ** n ) * 3
		r -= ( 2 ** n )
		c -= ( 2 ** n )
    
print(ans)