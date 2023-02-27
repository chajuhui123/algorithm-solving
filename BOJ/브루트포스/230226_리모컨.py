from itertools import permutations, combinations

n = int(input()) # 이동하고자 하는 채널
m = int(input()) # 고장난 버튼의 갯수
buttons = list(map(int, input().split())) # 고장난 버튼

# 누를 수 있는 버튼 리스트 (사용가능한 버튼)
able_buttons = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for button in buttons:
    able_buttons.remove(button)


# 5457
# 3 
# 6 7 8 

# 우리가 사용할 수 있는 버튼 1, 2, 3, 4, 5, 9

# 사용할 수 있는 버튼의 수 >= n의 자리수
# 1, 2, 3, 4, 5, 9 라는 숫자로 만들 수 있는 4자리 수

# items = [1,2,3,4]

able_len = list(permutations(able_buttons, len(str(n))))
abel_small_len = list(permutations(able_buttons, len(str(n)) - 1 ))
able_big_len = list(permutations(able_buttons, len(str(n)) + 1 ))

# 사용 가능한 버튼들로 만들 수 있는 모든 번호 (n개의 자리 동일)
able = []
for item in able_len:
    able.append(''.join(map(str, item)))

diff = []
for able_num in able:
    print(able_num)
    diff.append(abs(int(n) - int(able_num)))
    
print(diff)




    
    
