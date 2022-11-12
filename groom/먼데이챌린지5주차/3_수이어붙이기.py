from itertools import permutations
import sys


input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))
A.sort()

ans = 1e18

# 파이썬은 내장 라이브러리에서 순열을 지원
for order in permutations(A, N):
    cur = order[0]

    for i in range(1, N):
        if cur % 10 == order[i] // 10:
            cur = cur * 10 + order[i] % 10
        else:
            cur = cur * 100 + order[i]

    # 최소값을 찾아나감
    ans = min(ans, cur)

print(ans)

# IDEA
# 주어진 모든 수를 사용하여 가장 작은 수를 만들어야 한다.
# <앞의 숫자 일의 자리 수 === 뒤의 숫자 십의 자리 수> 라면 숫자를 겹쳐서 이어붙일 수 있다는 규칙이 있다.
# 순열로 가능한 조합을 구한 후, 완전 탐색을 통해 최소 값을 찾아나간다.