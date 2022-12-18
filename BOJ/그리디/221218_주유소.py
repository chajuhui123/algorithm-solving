n = int(input()) # 도시의 개수를 나타내는 정수 n (2 ≤ N ≤ 100,000)
lengths_road = list(map(int, input().split(' '))) # 인접한 두 도시를 연결하는 도로의 길이 (N-1개)
costs_oil = list(map(int, input().split(' '))) # 다음 줄에는 주유소의 리터당 가격 (N개) 

answer = 0
min_oil = costs_oil[0] # 가장 작은 리터 당 가격

# 맨 마지막 (n-1에 위치한) 리터당 가격은 고려되지 않으므로 n-1 이전까지 탐색한다.
for idx in range(0, n-1):
    # 현재 min_oil에 저장되어 있는 리터당 값보다 작은 리터당 가격이 탐색되면
    if min_oil > costs_oil[idx]:
        # min_oil 값을 변경한다
        min_oil = costs_oil[idx]
    # 탐색 과정에서 저장된 min_oil 값으로 도시까지 이동(lengths_road[idx]) 하는 비용을 answer에 더해준다.
    answer += min_oil * lengths_road[idx]

print(answer)

# 4
# 2 3 1
# 5 2 4 1
# => 18

# 4
# 3 3 4
# 1 1 1 1
# => 10