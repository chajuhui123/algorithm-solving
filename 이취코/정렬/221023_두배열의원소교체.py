# p.182

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a는 오름차순 b는 내림차순
a.sort()
b.sort(reverse=True)

for idx in range(k):
    if a[idx] < b[idx]:
        a[idx], b[idx] = b[idx], a[idx]
    else:
        break

print(sum(a))
