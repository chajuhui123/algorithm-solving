# 1461

# n : 책의 개수
# m : 세준이가 한 번에 들 수 있는 책의 개수
# books : 책의 제자리 위치가 저장된 리스트
n,m = map(int, input().split(" "))
books = sorted(list(map(int, input().split(" "))))

#  각 책의 위치를 저장

negative = [] # 음수 위치 저장
positive = [] # 양수 위치 저장
last_walk = 0 # 마지막 방문 위치 (왕복 하지 않아도 되는 위치)

for book in books:
    if (book > 0): positive.append(book)
    else : negative.append(book)
    if abs(book) > abs(last_walk): last_walk = book

# 양수는 내림차순
# 음수는 오름차순으로 정렬
positive.sort(reverse= True)
negative.sort()

# m권의 책을 들 수 있을 때, 그 중 멀리 있는 거리로 방문한다. (왕복)

walk = 0

for positive_walk in range(0, len(positive), m):
    if positive[positive_walk] != last_walk: # 마지막으로 방문해야하는 곳이라면 제외
        walk += positive[positive_walk]

for negative_walk in range(0, len(negative), m):
    if negative[negative_walk] != last_walk: # 마지막으로 방문해야하는 곳이라면 제외
        walk += abs(negative[negative_walk])

print(walk * 2 + abs(last_walk))