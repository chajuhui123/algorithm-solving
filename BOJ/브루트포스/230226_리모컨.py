from itertools import permutations, combinations

n = int(input()) # 이동하고자 하는 채널
m = int(input()) # 고장난 버튼의 갯수
buttons = list(map(int, input().split())) # 고장난 버튼

# 누를 수 있는 버튼 리스트 (사용가능한 버튼)
able_buttons = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for button in buttons:
    able_buttons.remove(button)

# +/- 버튼만 눌러서 움직일 경우 (최대)
cnt = abs(100 - n)

for channel in range(1000001):
    for i in str(channel):
        # 고장난 버튼이 있으면
        # 입력을 하지못하므로 통과
        if i not in able_buttons:
            break
        # 버튼이 고장나지 않았다면
        # 채널 움직인 후 +/-를 통해 움직이는게 더 최소이므로 갱신
        else:
            cnt = min(cnt, len(str(channel)) + abs(channel - n))

print(cnt)

# IDEA
# 0 ~ 1000000 까지 for문을 반복하며 해당 숫자가 모두 누를수 있는 버튼들로 이루어져 있다면,
# 해당 숫자로 가능한 최소횟수 VS (입력으로 받은 숫자 n - 100) 의 절대값과 비교하여 작은 숫자 출력