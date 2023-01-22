# 2839

import sys
input = sys.stdin.readline

# 3kg과 5kg 의 봉지를 최소한의 갯수를 활용해 담기
n = int(input())
cnt = 0 # 필요한 봉지 수

# 1. 5kg 봉지만 사용
# 2. 5kg + 3kg 봉지 사용 (단, 가능한 5kg 봉지를 많이 써야함)
# 3. 3kg 봉지만 사용
# 4. 그렇다면 5kg 연산이 가능한 많이하고, 이 외를 3kg 연산으로 채우기 
# => 주어진 수를 5의 배수로 만들기

while n >= 0 : #설탕이 남아있다면
    if n % 5 == 0: # n이 5의 배수일 때와 0일때 실행
        cnt += n // 5 # 5kg 봉지로 진행
        n = 0
        break
    n -= 3 # 5의 배수가 될 때까지 3킬로그램짜리 봉지에 담음 (3kg 최소로 사용)
    cnt += 1

if n == 0:
    print(cnt)
else:
    print(-1) # 설탕이 0아니라면 3, 5로 딱 맞게 나눌 수 없음