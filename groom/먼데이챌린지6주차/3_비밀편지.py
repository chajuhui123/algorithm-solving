import sys
import string
input = sys.stdin.readline

# a~z
alpha_sm = list(string.ascii_lowercase)
# A~Z
alpha_bi = list(string.ascii_uppercase)

t = int(input())

for i in range(t):
    code = input().rstrip()
    com, key = map(str, input().split())

    # 토큰 앞에 붙는 E/D 표시를 통해서 암호화 혹은 복호화를 진행
    # CASE1. E의 경우
    if com == 'E':
        res = ''
        idx = 0
        for i in code:
            if idx == len(key):
                idx = 0
            if i in alpha_bi:
                res += alpha_bi[(alpha_bi.index(i) + ord(key[idx]) )% 26 ]
                idx += 1
            elif i in alpha_sm:
                res += alpha_sm[(alpha_sm.index(i) + ord(key[idx]) )% 26 ]
                idx += 1
            else:
                res += i
                idx += 1

    # CASE1. D의 경우
    else:
        res = ''
        idx = 0
        for i in code:
            if i in alpha_bi:
                res += alpha_bi[(alpha_bi.index(i) - ord(key[idx]) )% 26 ]
                idx += 1
            elif i in alpha_sm:
                res += alpha_sm[(alpha_sm.index(i) - ord(key[idx]) )% 26 ]
                idx += 1
            else:
                res += i
                idx += 1
            if idx == len(key):
                idx = 0
                
    print(res)