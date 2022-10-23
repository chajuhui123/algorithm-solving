# p.178

n = int(input())

li = []
for _ in range(n):
    li.append(int(input()))

li.sort(reverse=True)

print( " ".join(str(item) for item in li))
