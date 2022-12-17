#  11501

import sys
input = sys.stdin.readline

TC = int(input().strip()) # Test Case 갯수
answer = [] # TC 별 답을 저장할 answer

for _ in range(TC):
    stocks_count = int(input().strip()) # 날의 수
    stocks = list(map(int, input().strip().split(" "))) # 날 별 주가

    tc_answer = 0
    max = 0 # 고가 (갱신)

    # 거꾸로(미래부터) 탐색
    # 뒤에서부터 큰 수를 찾아 앞에 값을 빼주는 방법
    for i in range(stocks_count-1, -1, -1):
        if stocks[i] > max:
            max = stocks[i]
        else:
            tc_answer += max - stocks[i] # 가장 고가에 가격에서 현재 주식을 판 값을 TC별 answer에 더해줌

    answer.append(tc_answer)

print(*answer, sep = "\n")


# IDEA
# 과거에 NodeJS 로 풀었지만, 스터디에서 추천받은 문제여서 Py 로 다시 풀이를 진행해보았다.