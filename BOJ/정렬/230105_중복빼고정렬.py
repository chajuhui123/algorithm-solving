# 10867

import sys
input = sys.stdin.readline

n = int(input())
arr = list(set(map(int, input().split())))

arr.sort()

# ' '.join(arr) 작성시, str 타입만 허용하기 때문에 아래처럼 쓰는 편이 낫다.
print(*arr, sep=' ')