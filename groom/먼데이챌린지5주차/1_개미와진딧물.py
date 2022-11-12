import sys
input = sys.stdin.readline

def search(y, x, k):
    #윗 부분 탐색
    for i in range(k, -1, -1):
        for j in range(-i , i+1):
            if 0 <= y-  k + i < n and 0 <= x + j < n:
                # 2는 진딧물이므로 살아남음
                if ant_matrix[y -  k + i][x + j] == 2:
                    return True
    #아랫부분 탐색
    for i in range(1, k+1):
        for j in range(-k + i , +k - i + 1 ):
            if 0 <= y + i < n and 0 <= x + j < n:
                # 2는 진딧물이므로 살아남음
                if ant_matrix[y + i][x + j] == 2:
                    return True
    return False

n, k = map(int, input().split())
ant_matrix = list()
for i in range(n):
    ant_matrix.append(list(map(int, input().split())))

ant_count = 0

# 완전 탐색
for i in range(n):
    for j in range(n): # 개미가 위치한 값이 1 이므로
        if ant_matrix[i][j] == 1:
            #탐색해서 진딧물이 있으면 살아남은 개미로 생각한다.
            if search(i, j, k):
                ant_count += 1

print(ant_count)

# IDEA
# 완전탐색, 맨해튼 거리 활용하여 해결할 수 있다.
# 1은 개미가 존재하고, 2 는 진딧물인데, 개미와 진딧물의 맨헤튼 거리가 문제 조건에서 주어진 거리 안에 있다면 개미는 살아남는다.
# 조건을 통과해 살아남은 개미의 마리 수를 구한다.
