# 11279

import heapq
import sys
input = sys.stdin.readline

n = int(input())

heap = []

for _ in range(n):
    num = int(input())
    if num == 0:
        if not heap:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -num)


'''
13
0 => [], print(0)
1 => [1]
2 => [1,2]
0 => [1], print(2)
0 => [], print(1)
3 => [3]
2 => [3,2]
1 => [3,2,1]
0 => [2,1] print(3)
0 => [1] print(2)
0 => [] print(1)
0 => [], print(0)
0 => [], print(0)
따라서, 0 2 1 3 2 1 0 0 

0이면 최대힙 출력
-> 만약 배열이 비어 있는 경우인데 가장 큰 값을 출력하라고 한 경우에는 0을 출력
자연수이면 힙에 값 넣음 
'''