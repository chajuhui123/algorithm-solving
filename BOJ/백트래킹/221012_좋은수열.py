# 2661

n = int(input())

def checkIsGoodSequence(num):
    length = len(num)
    # 인접한 두 개의 부분 수열 중
    # 가장 긴 경우는 현재 수열의 길이의 N/2이기 때문에
    # 해당 길이까지 인접한 두 수열이 일치하는지 파악한다.

    # 만약 일치한다면 좋은 수열이 아님을 return 한다.(False)
    # N/2 길이까지 인접한 두 수열이 일치하지 않으면 좋은 수열임을 return 한다.(True)
    for idx in range(1, length//2 + 1):
        if num[-idx:] == num[-(idx*2):-idx]: return False
    else:
        return True

def backtracking(num):
    global n
    # 길이가 n인 좋은 수열 중 가장 작은 수 print
    # 1, 2, 3 순서대로 수열을 만들어나가기 때문에,
    # 처음 만들어지는 길이를 만족하는 수열 = 가장 작은 수열 보장됨
    if len(num) == n:
        print(num)
        exit()
    
    # 1, 2, 3 으로 순열을 만들어나감
    for i in range(1, 4):
        temp = num + str(i)
        if (checkIsGoodSequence(temp)): backtracking(temp) # 좋은 수열임이 확인되면 길이 붙여나감

backtracking('1')

# IDEA
# 좋은 수열인지 체크하는 부분과 (checkIsGoodSequence)
# 재귀적으로 백트래킹하여 수열을 만드는 함수가 필요하다 (backtracking)