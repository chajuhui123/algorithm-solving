# 7662

import sys
import heapq
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    n = int(input()) # n 개의 명령어 주어짐
    heap = []

    for __ in range(n):
        command, num = input().split()
        num = int(num)
        
        if command == "I": # 삽입 연산
            heapq.heappush(heap, num)

        elif command == "D": # 제거 연산
            if len(heap) > 0:
                if num == 1:
                    heap = heapq.nlargest(len(heap), heap)[1:] # 가장 큰 n개의 수를 뽑아 정렬 후, 1부터 슬라이싱하면 가장 큰 값이 제거된다.
                    heapq.heapify(heap) # 그 후 다시 힙 정렬을 하여 최소힙으로 변환

                elif num == -1:
                    heapq.heappop(heap) # 힙에서 가장 큰 값 제거

    if len(heap) > 0:
        print(heapq.nlargest(1, heap)[-1], heapq.heappop(heap))
   
    else:
        print("EMPTY")
