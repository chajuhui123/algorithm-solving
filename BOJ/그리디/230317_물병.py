# 1052

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

count = 0;

while bin(n).count('1') > k:
    n = n+1
    count = count +1

print(count)

# IDEA
# 물병을 같은 무게끼리만 합칠 수 있다는 말은 <2의 제곱승인 숫자들의 합>으로 이루어져 있다는 것
# n을 2의 제곱승인 숫자들로 표현하는 방법은 이진수(bin 메서드 활용)로 바꿔 이진수에 있는 1의 개수를 세면 된다