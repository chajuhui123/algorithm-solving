# 3568

import sys
input = sys.stdin.readline

# 1. 기본 변수형과 배열([]), 참조(&), 포인터(*)를 제공
# 2. 공통된 변수형을 제일 먼저 쓰고, 그 다음에 각 변수의 이름과 추가적인 변수형태 작성
# 3. 변수의 오른편에 있는 변수형은 순서를 뒤집어서 왼편에 붙일 수 있다

variables = input().split()

default = variables.pop(0) # 공통 변수명

# 세 번째 시도
for item in variables:
    item = item.strip()[0:len(item)-1] # 공백 제거 후, 뒤에 붙은 ',' 혹은 ';' 제거

    # 추가적인 변수형태는 뒤에서부터 탐색
    add_type = ''
    for type_idx in range(len(item) - 1, 0, -1):
        if not item[type_idx].isalpha():
            if item[type_idx] == ']':
                add_type += '['
            elif item[type_idx] == '[':
                add_type += ']'
            else:
                add_type += item[type_idx]

    # 기본 변수명(알파벳)
    default_var = ''
    for var_idx in range(len(item)):
        if item[var_idx].isalpha():
            default_var += item[var_idx]

    print(default + add_type + ' ' + default_var + ';')
            


# 놓쳤던 부분들
# 1. 변수명은 1자 이상일수도 있음 (제한 없음)
# 2. [] 은 거꾸로 출력되면 ][ 가 되므로 replace를 해서 추가해줘야 함

# 첫 번째 시도
# for item in variables:
#     item = item.strip()[0:len(item)-1] # 공백 제거 후, 뒤에 붙은 ',' 혹은 ';' 제거

#     variable_name = item[0] # 변수명

#     more_type = ''
#     if len(item) > 1: # 추가 변수형태 있는 경우
#         more_type = item[1::]
#     answer = (default + more_type[::-1] + ' ' + variable_name + ';').replace('][', '[]')
#     print(answer)

# 두 번째 시도
# for item in variables:
#     answer = default

#     item = item.strip()[0:len(item)-1] # 공백 제거 후, 뒤에 붙은 ',' 혹은 ';' 제거
#     item = item[::-1] # 거꾸로 정렬
    
#     start_idx = 0

#     for idx in range(0, len(item)):
#         if item[idx] in ["[", "]", "&", "*"]:
#             answer += item[idx]
#         else :
#             start_idx = idx
#             break

#     answer += ' ' + item[start_idx:len(item)][::-1] + ';' 
#     answer = answer.replace('][', '[]')

#     print(answer)

# int& a*[]&, b, c*;
# int& a*[][][]&, b, c*;
# int& abc*[]&, baaa, cddd*[];