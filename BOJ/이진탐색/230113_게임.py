# 1072

import sys
input = sys.stdin.readline

def get_victory_percent(x, y):
    return int(y/x * 100)

# 1. 게임 횟수 x, 이긴 게임 수 y, 승률 z
x, y = map(int, input().split())
z = get_victory_percent(x, y)

# 2. 승률이 이미 100인 경우는 오르지 않음
if z >= 99:
    print(-1)
    exit(0)

answer = 0
start = 1
end = 1000000000 # 최대 10억이 들어올 수 있어서 end 값을 10억으로 초기화

while start <= end:
        # 3. 범위 좁혀가며 이진 탐색 
        mid = (start + end) // 2

        # x, y 는 함께 증가
        if get_victory_percent(x+mid, y+mid) <= z:
            start = mid + 1
        else:
            answer = mid
            end = mid - 1

            print(answer)

# IDEA
# 해당 문제는 왜 이진 탐색으로 풀어야 할까? "1 ≤ X ≤ 1,000,000,000"
# 값이 최대 10억이 나올 수 있음 => O(N)으로 풀어도 시간 초과가 날 것이기 때문에, 연산을 줄일 수 있는 로직을 생각해나야함
# 다량의 데이터 검색을 하는 문제는 이진 탐색을 적용해볼 수 있음