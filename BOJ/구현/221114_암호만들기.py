from itertools import combinations

l, c = map(int, input().split())
alpha = input().split()
alpha.sort()

# 주어진 알파벳의 l개씩 조합해서 조합을 구한다. 
# 순열과 달리 순서 상관을 안하기 때문에 (A,B == B,A) 딕셔너리 순서대로 조합이 구해진다. [A,B], [A,C], [B,C] ...)
result = list(combinations(alpha, l))

for idx in range(len(result)):
    result[idx] = ''.join(result[idx])
    length = l
    # 모음(a,e,i,o,u) 가 포함되어 있다면 length -1 해주기
    if 'a' in result[idx]:
        length -= 1
    if 'e' in result[idx]:
        length -= 1
    if 'i' in result[idx]:
        length -= 1
    if 'o' in result[idx]:
        length -= 1
    if 'u' in result[idx]:
        length -= 1
    if length >= 2 and length <= (l-1):    
        print(result[idx])