# p.180

n = int(input())
array = []

for _ in range(n):
    name, score = input().split()
    array.append((name, int(score)))

# 점수 기준 정렬
array = sorted(array, key=lambda student : student[1])

print(" ".join(student[0] for student in array))

# IDEA
# Tuple 자료형 활용해 (점수, 이름)을 묶은 후, 점수를 기준으로 정렬

