# 1072

import sys
import decimal
input = sys.stdin.readline

def get_victory_percent(x, y):
    # return int(y/x * 100) 
    return y * 100 // x 
    # 부동소수점 오차로 인해 해당 return 문에 대해서만 정답 처리가 됨. 
    # int( / ) 와 // 의 차이를 이해해야 할듯 하다.
    # python float 다룰 때 주의!

# 1. 게임 횟수 x, 이긴 게임 수 y, 승률 z
x, y = map(int, input().split())
z = get_victory_percent(x, y)

answer = float('inf')

start = 1
end = 1000000000 # 최대 10억이 들어올 수 있어서 end 값을 10억으로 초기화

# 2. 범위 좁혀가며 이진 탐색 
while start <= end:
        mid = (start + end) // 2

        # x, y 는 함께 증가 => 게임 진행 판수
        
        # mid번 더 진행했을 때 원래의 승률이 더 크다면 
        # start를 mid 이상으로 두고 다시 탐색한다.
        if get_victory_percent(x+mid, y+mid) <= z:
            start = mid + 1
        else:
            # mid번 더 진행했을 때 처음 승률보다 크다면, answer은 현재 mid가 되고
            # end를 mid 이하로 두고 다시 탐색한다.
            answer = mid
            end = mid - 1

if answer == float('inf'): # 처음 진행했을 때보다 승률이 크게 변경되지 않은 경우
    print(-1) 
else:
    print(answer)

# IDEA
# 해당 문제는 왜 이진 탐색으로 풀어야 할까? "1 ≤ X ≤ 1,000,000,000"
# 값이 최대 10억이 나올 수 있음 => O(N)으로 풀어도 시간 초과가 날 것이기 때문에, 연산을 줄일 수 있는 로직을 생각해나야함
# 다량의 데이터 검색을 하는 문제는 이진 탐색을 적용해볼 수 있음