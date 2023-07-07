import sys
input = sys.stdin.readline

N, C = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(int(input()))

arr.sort() # 오름차순 정렬

start = 1
end = arr[len(arr) -1] - arr[0] # 첫 집과 마지막 집의 거리 차이 (최대로 나올 수 있는 거리 차이)

answer = 0

while start <= end:
    mid = (start + end) // 2 # 설치 간격 값
    current = arr[0]
    count = 1

    for i in range(1, len(arr)):
        if arr[i] >= current + mid: # i 번째 집에 mid 라는 간격으로 설치 가능한지 (같거나 더 멀어야함) 판단하고
            count += 1 # 가능하다면 count 늘려주기
            current = arr[i] # 해당 집에 설치, 다음 집 탐색을 위해 갱신

    if count >= C: # 설치 가능한 공유기가 C개를 넘어가면 더 넓게 설치 가능하므로 우측으로
        start = mid + 1
        answer = max(answer, mid)

    else: # 설치 가능한 공유기가 C개보다 적은 경우 더 좁게 설치 좌측으로
        end = mid - 1

print(answer)