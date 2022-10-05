# 2476

T = int(input())

answers = []

for _ in range(T):
    answer = 0
    nums = list(map(int, input().split(" ")))
    
    for i in range(3):
        numCount = nums.count(nums[i])

        if numCount == 2:
            answer = 1000 + nums[i] * 100
        if numCount == 3:
            answer = 10000 + nums[i] * 1000
    
    if answer == 0:
        answers.append(max(nums) * 100)
    else:
        answers.append(answer)

print(max(answers))

# IDEA
# 1. numCount를 세는 방식이 아닌 if elif 문을 통한 세 개의 변수 비교도 가능할 것 같다.

## if a ==b==c: result = 10000+a*1000
### elif a!=b==c or a==b!=c: result = 1000+b*100
## elif a==c!=b or a!=c==b:
### result = 1000+c*100
## elif a!=b!=c:
### result = max([a,b,c])*100