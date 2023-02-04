# 11054

# 바이토닉 부분수열? : S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN

n = int(input())
arr = list(map(int, input().split()))

increase = [1] * n
decrease = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if arr[i] > arr[j]:
            increase[i] = max(increase[i], increase[j]+1)

for i in range(n-2, -1, -1):
    for j in range(n-1, i, -1):
        if arr[i] > arr[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

result = []
for i in range(n):
    result.append(increase[i] + decrease[i] -1)

print(max(result))

# IDEA
# 증가하는 부분수열과 작아지는 부분수열 각각을 dp에 저장한다.
# 각 인덱스별로 증가하는 수열 길이 + 감소하는 수열 길이의 합이 가장 큰 것이 가장긴바이토닉부분수열이 된다.
# 이때 증가하는 부분수열, 작아지는 부분수열에 겹치는 부분이 있으니 -1을 해준다.