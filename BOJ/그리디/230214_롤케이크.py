# 16206

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(key = lambda x: (x % 10, x))

print(arr)

cnt = 0
for cake in arr:
    cnt = cake // 10

    if cake % 10 == 0:
        if cnt-1 <= m:
            cnt += cnt
            m -= cnt -1
        else:
            cnt += m
            m -= m
    else:
        if cnt <= m:
            cnt += cnt
            m -= cnt
        else:
            cnt += m
            m -= m
print(cnt)