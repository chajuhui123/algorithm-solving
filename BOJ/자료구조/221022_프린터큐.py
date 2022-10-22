# 1966

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    docs = list(map(int, input().split()))

    idx = list(range(n))
    idx[m] = 'target'

    order = 0

    while True:
        if docs[0] == max(docs):
            order += 1

            if idx[0]=='target':
                print(order)
                break
            else:
                docs.pop(0)
                idx.pop(0)

        else:
            docs.append(docs.pop(0))
            idx.append(idx.pop(0))



