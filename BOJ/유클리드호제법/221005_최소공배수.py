# 1934

T = int(input())

def getGcd(x,y):
    # x와 y의 최대 공약수는 y와 r의 최대 공약수와 같다 (여기서 r은 나머지. x % y = r)
    # 따라서 y에는 r값을 x에는 y값을 대입하다보면 x % y===0인 순간이 있다
    # 그 때의 y값이 x, y의 최대 공약수
    while y:
        x,y = y, x%y
    return x

def getLCM(x,y):
    result = x * y // getGcd(x,y)
    return result


for i in range(T):
    a,b = map(int, input().split())
    print(getLCM(a,b))

# IDEA
# 1. 최대공약수, 최소공배수를 구하는 다양한 방식이 있다. `import math`를 하여 라이브러리로 간단하게 구할 수도 있다.