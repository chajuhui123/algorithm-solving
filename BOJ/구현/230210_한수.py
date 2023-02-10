def is_hansu(num) :
    cnt = 0
    for i in range(1, num + 1):
        nums = list(map(int, str(i))) # 각 자리를 list 로 만들기
        if i < 100: # 100보다 작으면 모두 한수 (각 자리의 차이를 구할 필요가 없기 때문)
            cnt += 1  
        elif nums[0] - nums[1] == nums[1] - nums[2]: # 1000 이하의 수만 주어지기 때문에 [0]과[1], [1],[2]만 비교
            cnt += 1  

    return cnt

num = int(input())
print(is_hansu(num))