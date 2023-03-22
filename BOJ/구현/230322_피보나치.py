# 57950557

TC = int(input())

for _ in range(TC):
    n = int(input())
    num_0, num_1 = 1, 0
    
    for i in range(n):
        num_0, num_1 = num_1, num_0 + num_1 # 피보나치 로직
        
    print(num_0, num_1)


# IDEA
# 피보나치 함수의 규칙 <fibonacci(n‐1) + fibonacci(n‐2) (n==1 인 경우 1, n==0인 경우 0)> 을 변수의 덧셈 연산으로 풀이하였다.