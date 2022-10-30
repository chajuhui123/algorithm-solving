# 12904

import sys
input = sys.stdin.readline

s = list(input().strip())
t = list(input().strip())

answer = False

while t:
    # A 라면 그냥 제거
    if t[-1] == "A":
        t.pop()

    # B 라면 뒤집고 제거
    elif t[-1] == "B":
        t.pop()
        t.reverse()

    if t == s:
        answer = True
        break

print(int(answer))


# IDEA
# 문제의 조건 1. 문자열의 뒤에 A를 추가한다. 2. 문자열을 뒤집고 뒤에 B를 추가한다. 를 파악하면 해결 가능한 그리디 문제
# 처음에 해결하지 못했던 이유는 문자열을 뒤집는다는 문장을 A<->B 교체하는 것으로 이해해서 해결하지 못했다.
# 문제의 요구사항을 정확히 파악하자!