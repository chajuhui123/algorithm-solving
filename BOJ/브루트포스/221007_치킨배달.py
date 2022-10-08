# 15686

from itertools import combinations

# n : n 줄의 도시 정보, m : 폐업시킬 치킨 집  갯수
# cityGraph : 도시 지도
n, m = map(int, input().split(' ')) 
cityGraph = list(list(map(int, input().split())) for _ in range(n))

# 1은 집, 2는 치킨집 좌표를 저장
houses = []
stores = []

for x in range(n):
    for y in range(n):
        if cityGraph[x][y] == 1: houses.append([x,y])
        elif cityGraph[x][y] == 2: stores.append([x,y])

# 폐업해야하는 m개의 치킨집 좌표 조합을 구함 (중복 x)
result = 9999999999999

for store in combinations(stores, m):
    temp = 0 # 도시의 치킨 거리
    for house in houses: 
        storeLen = 999   # 각 집에서의 치킨 거리
        for j in range(m):
            storeLen = min(storeLen, abs(house[0] - store[j][0]) + abs(house[1] - store[j][1])) # |r1-r2| + |c1-c2|
        temp += storeLen # 해당 도시의 치킨 거리를 더해준다
    result = min(result, temp) # 치킨 거리가 가장 작은 값으로 저장함

print(result)

# IDEA
# 1. 폐업이 가능한 m개의 치킨집 조합을 구해, 해당 케이스에서의 도시 치킨 거리를 구한다
# 1-1. 이는 파이썬이 제공하는 combinations 를 활용할 수 있다. (중복 X 조합)
# 2. 구해진 도시 치킨 거리 중 가장 작은 값을 result에 갱신시키면서 답을 구해나간다