# 10431
p = int(input())  
arr = [list(map(int, input().split())) for _ in range(p)]

# 키 순 정렬 리스트
height = [[] for _ in range(p)]
# TC 번호, 걸음 수 리스트
result = [[] for _ in range(p)]  
cnt = 0  #걸음수

for i in range(p):
    cnt=0

    height[i].append(arr[i][0])
    height[i].append(arr[i][1])
    # 20개가 주어짐
    for j in range(2, 21):  
        for k in range(1, len(height[i])):  
            # 현재 넣으려는 학생을(arr) 정렬되어 있는 학생들(height)과 한명씩 비교하기
            if (arr[i][j] < height[i][k]): 
                height[i].insert(k, arr[i][j]) 
                # height 전체 길이에서 현재 인덱스, 테스트 케이스를 빼주면 학생들이 움직인 걸음 수
                cnt += len(height[i]) - 1 - k
                break
            if k == len(height[i]) - 1: 
                height[i].append(arr[i][j]) 
                
    result[i].append(arr[i][0]) 
    result[i].append(cnt)   

for i in range(p):
    print(result[i][0], result[i][1])


# IDEA
# 1. 자기 앞에 자기보다 키가 큰 학생이 없다면 그냥 그 자리에 서고 차례가 끝난다.
# 2. 자기 앞에 자기보다 키가 큰 학생이 한 명 이상 있다면 그중 가장 앞에 있는 학생(A)의 바로 앞에 선다. 이때, A부터 그 뒤의 모든 학생들은 공간을 만들기 위해 한 발씩 뒤로 물러서게 된다.
# 위 조건을 만족하는 줄세우기 알고리즘을 구현하였을 때, 기존 위치에서 뒤로 이동하는 걸음 수를 cnt한다.