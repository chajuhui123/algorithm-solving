# 1449

# 물이 새는 곳 갯수 n, 테이프의 길이 l
n, l = map(int, input().split())
# 물 새는 곳 위치 s
s = list(map(int, input().split()))
s.sort()


# 테이프 붙이기 시작하는 지점
start = s[0]
# 필요한 테이프의 갯수 (answer)
cnt = 1

# 시작하는 시점 제외하고, 물이 새는 지점 검사
for now_location in s[1:]:
    # 테이프를 붙이는 범위 내에 현재 물이 새는 곳 위치가 포함되어 있다면, 기존 테이프 유지하고
    if now_location in range(start, start + l):
        continue
    # 기존의 테이프로 가릴 수 없다면, 시작점을 갱신한다. 
    # 테이프의 갯수를 세는 cnt도 증가시킨다.
    else:
        start = now_location
        cnt += 1

print(cnt)

# IDEA
# 1. 매 순간 최선의 선택을 하는 그리디 알고리즘이라고 볼 수 있다.
# 2. 테이프로 가릴 수 있는 경우 / 테이프로 가릴 수 없는 경우로 판단하여, 총 소모된 테이프의 갯수를 count 한다.
