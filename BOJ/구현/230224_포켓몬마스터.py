# 1620

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}

for i in range(1, n + 1):
    a = input().rstrip()
    dict[i] = a
    dict[a] = i

for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(dict[int(quest)])
    else:
        print(dict[quest])
    

# IDEA
# 처음에는 백과사전 정보를 Array 형태로 관리하려고 했는데,
# 배열에 속한 문자열의 index 값을 구하는 Array.index(value) 메서드는 항상 배열 길이 N 만큼의 복잡도를 가진다. O(n)
# 따라서 해당 문제에는 Dictionary 형태로 포켓몬 명과 백과사전 번호를 관리하는 것이 적절하다. O(1)