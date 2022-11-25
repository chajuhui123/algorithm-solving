import sys
input = sys.stdin.readline
from collections import defaultdict


n, m = map(int, input().split())

# 딕셔너리 활용
arr = defaultdict(int)
for _ in range(m):
    user = list(map(int, input().split()))
    for i in user[1:]:
        arr[i] += 1

# 딕셔너리의 Value 기준으로 큰 값부터 작은 값부터 정렬, Value가 같다면 Key순으로 정렬
res = sorted(arr.items(), key=lambda x: (x[1], x[0]), reverse=True)
print(res[0][0], end = ' ')

idx = 0
while True:
    if idx == len(res)-1:
        break
    if res[idx][1] == res[idx+1][1]:
        print(res[idx+1][0], end = ' ')
        idx += 1
    else:
        break