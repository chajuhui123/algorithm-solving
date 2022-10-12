# 1715

import heapq

n = int(input())
cards = []

for _ in range(n):
    # 리스트를 힙처럼 다룰 수 있게 해주는 heap Queue 최소 힙을 보장한다.
    # (리스트와 별개 구조인 PriorityQueue 와 다름)
    heapq.heappush(cards, int(input()))
    
answer = 0

for _ in range(n-1):
    # heap에서 가장 작은 두 카드 묶음 가져옴 
    temp_sum = heapq.heappop(cards) + heapq.heappop(cards) 
    heapq.heappush(cards, temp_sum)
    answer += temp_sum

print(answer)

# IDEA
# 이전에 틀렸던 이윤... 이전 연산에 대한 카드 묶음 값을 더해주지 않았어서 인 거 같다! 문제의 요구 사항을 잘 파악하기.