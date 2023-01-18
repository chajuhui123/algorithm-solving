import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lesson_arr = list(map(int, input().split())) # 강의 순서가 바뀌면 안됨 (정렬 x)

# Err 원인 : start 유의해서 보기. 항상 1로 초기화 했는데 문제 조건에 따라 다를 수 있음.
start = max(lesson_arr) # list 의 최대 값을 start 로 설정 => 모든 강의를 담아야 하기 때문
end = 100000 * 10000  # 강의의 수 (1 ≤ N ≤ 100,000) * 강의 길이 최대 10000 분

answer = 100000 * 10000

while start <= end:
    mid = (start+end) // 2  # 구하고자 하는 값 => 블루레이의 크기

    cnt = 1 # 몇 번째 블루레이
    video_len_tmp = 0 # 블루레이에 저장하는 강의 길이

    # 블루레이가 주어진 강의가 순차적으로 담겨야 하므로 for 문
    for idx in range(n):
        if video_len_tmp + lesson_arr[idx] <= mid:
            video_len_tmp += lesson_arr[idx] # 현재 강의를 저장하고 있는 블루레이에 강의 저장
        else:
            cnt += 1
            video_len_tmp = lesson_arr[idx] # 새로운 블루레이에 강의 저장
        if cnt > m: # 주어진 블루레이 갯수를 초과하면
            break

    if cnt > m:
        # mid의 블루레이 크기로 강의를 저장할 때, 블루레이 갯수가 m 보다 더 필요한 경우 
        # start 를 mid + 1 로 변경해줌 (블루레이 크기를 높여도 됨)
        start = mid + 1 
    else:
        # mid의 블루레이 크기로 강의를 저장할 때, 블루레이 갯수가 m 과 같거나 부족한 경우
        # end 를 mid - 1 로 변경해줌 (블루레이 크기를 줄여야 함)
        end = mid - 1

        # Err 원인 : mid 가 리스트의 최대값보다 작다면 결과값에 넣지 않도록 조건 (항상 end로 했음)
        if(mid >= max(lesson_arr)):
            answer = min(answer, mid)

print(answer)

'''
EX.
9 3
1 2 3 4 5 6 7 8 9

3개의 블루레이를 쓸 수 있음

1 2 3 4 5 => 15
6 7 3 => 13
8 9 => 17

블루레이의 크기는 17이 됨 => 이보다 더 작을 수 없음
'''