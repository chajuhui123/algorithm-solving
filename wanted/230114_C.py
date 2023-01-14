import sys
input = sys.stdin.readline

N, M, C = map(int,input().split())

sati_arr = []
for _ in range(C):
    new_sati = list(map(int,input().split()))
    sati_arr.append(new_sati)

student_N = list(map(int, input().split()))
student_M = list(map(int, input().split()))

sati_answer = []
for n in student_N:
    temp = []
    for m in student_M:
        sati = sati_arr[n-1][m-1]
        temp.append(sati)
    sati_answer.append(max(temp))

# print(sati_answer)

sati_answer.sort(reverse=True)
cnt = min(N, M)

print(sum(sati_answer[0:cnt]))
    
    

# 2 3 2
# 1 10
# 10 10
# 1 2
# 1 2 2