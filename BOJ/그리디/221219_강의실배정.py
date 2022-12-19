# 11000
# 최소 강의실을 사용하여 강의 끝내기
import heapq

import sys
input = sys.stdin.readline

n = int(input()) # 진행하는 수업의 갯수 n
q = []

# 다시 보기!!!
for _ in range(n):
    start, end = map(int, input().split(' ')) # 강의당 시작 시간 start, 종료 시간 end
    q.append([start, end])

q.sort()

room = []
# 가장 먼저 시작하는 강의의 종료 시간을 heap에 저장
heapq.heappush(room, q[0][1])

for idx in range(1, n):
    # 현재 강의 종료 시간 > 다음 강의 시작 시간
    if room[0] > q[idx][0]: # 현재 강의 끝나는 시간보다, 다음 강의 시작 시간이 빠르면
        heapq.heappush(room, q[idx][1]) # 새로운 회의실 개설
    # 현재 강의 종료 시간 <= 다음 강의 시작 시간
    else: # 현재 회의실에 이어서 회의 개최 가능
        heapq.heappop(room) # 새로운 회의로 시간 변경을 위해 pop 후, 
        heapq.heappush(room, q[idx][1]) # 다음 강의 종료 시간 push

print(len(room))


# 3
# 1 3
# 2 4 
# 3 5

# IDEA CONCEPT
# 현재 회의실의 종료시간과 다음 열릴 회의의 시작시간 과의 관계를 파악해야한다.
# 관계를 파악하여, 하나의 강의실에서 진행 가능한지
# 혹은 강의실을 추가할지 판단한다.

# IDEA1 (Fail)
# start  1 2 3 
# end 3 4 5
# 1. 문제의 핵심은 현재 수업의 end - 그 다음 수업의 start 를 비교하는 것인데 그렇다면 start end 를 따로 관리해서 비교를 해볼까?
# 2. 따로 관리하게 되면 각 강의 start, end 시간이 따로 관리되면 어떤 수업이 한 쌍인지 알기 어려워서 관리 복잡해짐.
# 3. 따라서 start, end 시간은 한 쌍으로 관리되어야 할 것 같음.

# IDEA2 (Success)
# 1. 준형이가 힌트 준 heap을 알아보자 <우선순위 큐를 이용해 큐에 push를 해주면 큐는 정렬상태를 유지한다.> 
# 2. 큐는 정렬된 상태를 만들어줌
# 3. 각 강의의 start end 를 비교했을 때 <이전 강의 end <= 이후 강의의 start> 가 만족되면 하나의 강의실에서 진행하고,
# 4. <이전 강의 end > 이후 강의의 start> 이면 강의실을 추가해야한다.
# 5. 그리고 시간초과 때문에 sys.stdin.readline 셋팅 필수우

# Question
# 1. 이해가 안가는 부분.. 
# 이미 q는 sort를 마친 배열이여서, 수업이 진행되는 순서대로 탐색하며 append or pop 연산을 진행할텐데 
# 왜 heap으로 관리해야만 통과가 될까...????? Queue가 정렬 상태를 유지해주기 때문인지 알겠지만, 이미 순서대로 정렬된 배열을 탐색하는 거 아닌가!?