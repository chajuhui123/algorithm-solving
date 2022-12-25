# 1213

import sys
input = sys.stdin.readline

# 1. 팰린드롬에 대한 정의
# (짝수 개인 경우) 절반으로 나눴을 때, 마주본 인덱스의 문자끼리 일치하는 경우 
# (홀수 개인 경우) 가운데 하나를 제외한 후, 절반으로 나눴을 때, 마주본 인덱스의 문자끼리 일치하는 경우 
# ㄴ 가운데를 제외하고, 마주본 인덱스끼리 문자가 일치해야하므로, '홀수 개인 알파벳은 1개만 존재'해야 한다.

# 2. 사전순으로 앞서는 것을 출력하는 조건이 있으므로, 정렬 수행
alphabets = sorted(input().strip()) 

# 3. dictionary 로 각 알파벳이 주어진 문자에서 몇 개씩 존재하는지 저장
alphabets_obj = {}
for alphabet in alphabets:
    if alphabet in alphabets_obj:
        alphabets_obj[alphabet] += 1
    else :
        alphabets_obj[alphabet] = 1

# 4. dictionary에 저장된 알파벳 갯수를 검사하여, 홀수 개인 알파벳이 몇 개 존재하는지 검사
odd_cnt = 0
for value in alphabets_obj.values():
    if value % 2 == 1: # 홀수인 경우
        odd_cnt += 1

if odd_cnt > 1: # 홀수 개인 알파벳이 2번 이상 존재하는 경우, 팰린드롬을 만들 수가 없음
    print("I'm Sorry Hansoo")
else :
    middle = '' # 홀수 개인 알파벳인 경우, 가운데 위치
    half = '' # half + middle + reversed_half 로 문자열 관리
    for key in alphabets_obj.keys():
        value = alphabets_obj[key]
        if (value % 2 == 1): middle = key
        half += key * (value // 2) # 알파벳 갯수의 int(1/2)만큼 half 문자열에 더해줌 (사전순으로 이미 정렬되어 있으므로, 이후 정렬 불필요)
    reversed_half = half[::-1]
    print(half + middle + reversed_half)
    
# Ex 
# AABB
# AAABB
# ABACABA
# ABCD
