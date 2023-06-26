# 13904

import sys
input = sys.stdin.readline

n = int(input()) # n: 과제 갯수

result = 0 # 얻을 수 있는 점수의 최댓값
assignment_clear = [False] * 1001 #  i일차 과제 수행 여부 저장 list 
# 런타임 에러 (IndexError) : 처음에 입력받은 n이 최대값으로 들어올 줄 알았는데, 과제 수행 일수에 대한 n 값은 관계가 없음.. 따라서 문제 조건에 주어진 (1 ≤ d ≤ 1,000) 참고하여 초기화해줌

homeworks = []

for _ in range(n):
    d, w = map(int, input().split()) # d: 과제 마감일까지 남은 일수, w: 과제 점수
    homeworks.append([d, w])

homeworks.sort(key=lambda x:-x[1]) # 과제 점수 기준 내림차순 정렬

for d, w in homeworks:
    max_day = d 
    while (max_day > 0) and assignment_clear[max_day]:
        max_day -= 1 # 과제할 날짜를 최대한 미룰 수 있을 때까지 미루기
    if max_day > 0:
        assignment_clear[max_day] = True
        result += w
    
print(result)

# IDEA
# Greedy + 정렬 문제
# 우선 <얻을 수 있는 점수의 최댓값> 을 구하는 문제인 것을 인지하고, Greedy 유형의 문제라는 것을 파악할 수 있었음
# 단, 해당 문제에서는 <과제 수행 가능 일수> 라는 제한이 있어, 이에 대한 연산이 필요하다는 것을 깨달음
# 우선 과제 점수를 기준으로 내림차순 정렬하여, 높은 점수에 대해 우선적으로 수행해야 함. 
# 또한 해당 과제를 최대한 늦게 수행하는 방안으로 진행해야함.
# <높은 점수의 과제를 우선 진행하나, 가능한 늦게 과제를 수행해야함>
# 예시에 나온 예제처럼 가장 점수가 높은 60점은 4일이 소요되는데, 4번째로 수행할 때, 이전 1, 2, 3일차엔 다른 과제를 진행할 수 있기에 수행할 수 있는 과제가 늘어남 = 점수도 늘어남
# 따라서 위 코드에서는 <assignment_clear> 라는 리스트를 선언하여, 과제할 날짜를 최대한 미룰 수 있을 때까지 미루는 로직을 완성함. 0 이전까지 인덱스를 줄여가며, 가능한 인덱스 중 가장 최대 일수에 해당하는 인덱스에서 과제를 수행하도록 저장

