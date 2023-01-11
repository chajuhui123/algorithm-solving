# 18870

import sys
input = sys.stdin.readline

n = int(input())
origin_xy = list(map(int, input().split()))

sorted_xy = sorted(list(set(origin_xy))) # 중복 제거 후 정렬

# value : index 형태로 dictionary 에 저장한다 (value 들은 오름차순으로 index 를 갖게 된다)
xy_dic = {sorted_xy[i] : i for i in range(len(sorted_xy))} #  : 해당 값의 index

# 처음에 입력받은 좌표들 순서대로 순환하며 value 를 key 값으로해 몇 번째 수인지 index 로 접근한다.
for i in origin_xy:
    print(xy_dic[i], end = ' ')


'''
좌표 압축 == 주어진 좌표에서 가장 작은 값 0 부터 시작하여 알맞는 좌표 값으로 치환

따라서 주어진 좌표 배열을 오름차순 정렬

정렬된 값을 기준으로 몇 번째 수인지  저장하기 위해 dictionary 구조를 활용함 

`value : index` 를 dictionary에 저장

다시 처음에 입력받았던 좌표 배열을 순환하면서 탐색되는 value가 몇 번째 index 인지 print
'''