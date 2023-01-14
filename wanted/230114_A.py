from itertools import groupby
import sys
input = sys.stdin.readline


s_num = int(input())
s_list = list(map(int,input().split()))
m_list = []


new_arr = [ 1 if item == 1 else -1 for item in s_list ] # 2는 -1로 치환
stone_group = [list(v) for _, v in groupby(new_arr)] 
m_list = [sum(group) for group in stone_group]

max_answer = 0
min_answer = 0

stack = 0

for statue in m_list:
    if(statue > 0):
        current_sum = max_answer + stack + statue

        if(statue >= current_sum):
            max_answer = statue
            stack = 0

        elif (current_sum >= max_answer):
            max_answer = current_sum
            stack = 0

        elif (statue >= max_answer):
            max_answer = statue
            stack = 0
        
        else:
            stack += statue
    else:
        stack += statue

stack = 0

for statue in m_list:
    if(statue < 0):
        current_sum = min_answer + stack + statue

        if(statue <= current_sum):
            min_answer = statue
            stack = 0

        if (current_sum <= min_answer):
            min_answer = current_sum
            stack = 0

        elif (statue <= min_answer):
            min_answer = statue
            stack = 0
        
        else:
            stack += statue
    else:
        stack += statue


print(max(max_answer, abs(min_answer)))
