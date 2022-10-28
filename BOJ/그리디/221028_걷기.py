# 1459

# 도착해야하는 좌표 x,y
# 한 블록 가는데 걸리는 시간 w
# 대각선으로 가로지르는데 걸리는 시간 s
x, y, w, s = map(int, input().split())

answer = 0

if w <= s:
    answer = (x + y) * w
else:
    answer = min(x, y) * s
    answer += min(abs(x-y) * w, (abs(x - y)-1) * s if abs(x - y) % 2 == 1 else abs(x - y) * s);

print(answer)

# IDEA
# 1. w < s 인 경우 => (x + y) * w
# 2. w > s 인 경우 => min(x, y)*s + abs(x-y)
# 2-1. abs(x - y)가 짝수인 경우 : 똑같이 대각선으로 이동할 수 있으므로 abs(x-y)*s만큼 이동
# 2-2. abs(x - y)가 홀수인 경우 : 아래 두 경우중 최소로 이동
# # 일자 거리 abs(x-y) * w 만큼 이동
# # 짝수 abs(x - y - 1)*s 만큼 이동 후 w만큼 이동