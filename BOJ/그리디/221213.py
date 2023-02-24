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


# '그리디 문제'로 분류해보았다.
# 예를 들어 aaaabbcc 문자들이 중복되지 않도록하는데 적은 비용으로 제거해야한다면 
# 중복되는 문자를 하나의 그룹으로 나눠서 본다 aaaa/bb/cc 이때 각 그룹에서 하나씩만 남기고 제거를 해야하는데,
# 그렇다면 가장 큰 비용을 남기고 그 외 비용들을 더한다.