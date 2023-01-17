import sys
input = sys.stdin.readline

# 가지고 있는 랜선 수 k, 필요한 랜선 수 n
k, n = map(int, input().split())
lan_arr = []

for _ in range(k):
    lan = int(input())
    lan_arr.append(lan)

# 런타임 에러 (Zero Division Error) => 
# k = 1, n = 1, lan_arr = [1] 인 경우 start=0 로 설정시, mid 가 0이 되는 오류가 발생한다..!!! 따라서 start 를 1로 셋팅
start = 1
end = max(lan_arr)

def get_lan_cnt(lan_arr , len):
    lan_cnt = 0
    for lan_item in lan_arr:
        lan_cnt += lan_item // len
    return lan_cnt

while start <= end:
    mid = (start + end) // 2
    lan_cnt = get_lan_cnt(lan_arr, mid)

    # 목표보다 많거나 같은 길이의 랜선이 잘리는 경우는, 더 긴 사이즈로 잘라도 됨
    if lan_cnt >= n:
        start = mid + 1;
    # 목표보다 적거나 랜선이 자르는 경우는, 짧은 사이즈로 잘라야 함
    else:
        end = mid - 1;


print(end)