# 7795

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))

    start = 0
    count = 0
 
    for j in range(n):
        while True:
            if start == m or a[j] <= b[start]:
                count += start
                break
            else:   
                start += 1
                
    print(count)