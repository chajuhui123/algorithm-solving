# 12904

import sys
input = sys.stdin.readline

s = list(input().strip())
t = list(input().strip())

while len(s) != len(t):
    last = t.pop()

    # A 라면 그냥 제거
    if last == "A":
        continue

    # B 라면 뒤집고 제거
    elif last == "B":
        t = list(map(lambda x: 'A' if x == "B" else 'B', t))

    if len(t) == len(s):
        break

print(1 if s == t else 0)


    

# 문자열 뒤에 A 추가
# 문자열 뒤집고 B 추가


# B 라면 뒤집고 제거


# 길이 같으면 -> 뒤집어서 비교 같지 않다면 0 리턴

# A B B A (A 그냥 제거)
# A B B B (B 제거 후 뒤집기)
# B A A (A 그냥 제거)
# B A (A 그냥 제거)
# B (일치~!)

# A B B (B 제거 후 뒤집기)
# B A (일치하지 않아용)


