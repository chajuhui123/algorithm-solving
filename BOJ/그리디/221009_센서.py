# 2212

# n : 고속도로 위 센서의 갯수
# k : 세워야 할 집중국 갯수
# sensor : 고속도로 위 센서 위치
n = int(input())
k = int(input())
sensors = sorted(list(map(int, input().split( )))) # 중복 제거 및 정렬

# 나눠야할 구간의 갯수가 센서의 갯수보다 크다면
# 센서 간의 거리 차이가 발생할 일이 없으므로 0 리턴
if k >= n:
    print(0)
else:
    dist = [] # 센서들 사이의 거리 저장

    for i in range(1, n):
        dist.append(sensors[i] - sensors[i-1])

    dist.sort(reverse=True) # 거리를 내림차순 정렬

    for _ in range(k - 1):
        dist.pop(0) # 가장 거리 차이가 큰 k-1 개의 연결된 구간을 제거하면 됨 (k개로 구간이 나뉘어짐)

    print(sum(dist))



# IDEA
# k개의 구간으로 sensors를 나누는 문제와 같다고 해석 가능하다
# 구간을 나눴을 때, 집중국 사이의 거리를 구하고
# 거리의 합을 최소화하는 경우를 리턴


# TIP
# python method : sorted(list) VS list.sort() 비교
# sorted는 정렬된 리스트를 리턴한다
# sort는 None을 리턴한다. 이미 정의된 리스트 값을 정렬해 기존에 저장된 값을 덮어씌운다.
