# target : string
# cost : array
def row_cost_non_neighboring(target, cost):
    target = list(target)
    answer = 0
    
    # 첫 번째 아이템
    before = target[0]
    temp_start = 0

    # 두 번째 아이템부터 순차적으로 탐색
    for idx_now, now in enumerate(target[1:len(target)+1]):
        if now != before:
            # 중복되는 숫자들의 비용 중 적은 비용으로 구함
            answer += get_minimum_cost(cost[temp_start:idx_now+1])
            temp_start = idx_now + 1
        before = now
        
    # 마지막 남은 cost 
    answer += get_minimum_cost(cost[temp_start:len(target)+1])

    return answer
            
def get_minimum_cost(arr):
    if len(arr) > 0:
        arr = sorted(arr)
        return sum(arr[0:len(arr) -1])
    else :
        return 0

print(row_cost_non_neighboring('abbcde', [0,1,2,1,1,1]))
print(row_cost_non_neighboring('aabbcc', [0,1,0,1,0,1]))
print(row_cost_non_neighboring('cbbbbde', [0,1,2,3,4,5,6]))

