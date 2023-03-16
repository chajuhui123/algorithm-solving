# 8979

import sys
input = sys.stdin.readline
 
# 입력받는 국가의 갯수 n, 등수를 알고자하는 국가 k
n, k = map(int, input().split()) 
s = []

for i in range(n):
    s.append(list(map(int, input().split())))
s.sort(key=lambda x : (x[1], x[2], x[3]), reverse=True) # 금메달이 많은 순으로 정렬

# 금메달이 같다면 은메달, 은메달이 같다면 동메달이 많은순
for i in range(n):
    if s[i][0] == k:
        index = i

for i in range(n):
    if s[index][1:] == s[i][1:]:
        print(i + 1)
        break


# 금메달 수가 더 많은 나라 
# 금메달 수가 같으면, 은메달 수가 더 많은 나라
# 금, 은메달 수가 모두 같으면, 동메달 수가 더 많은 나라 