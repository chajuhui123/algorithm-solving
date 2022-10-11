# 2217

n = int(input())
ropes = []

for i in range(n):
    rope = int(input())
    ropes.append(rope)

ropes.sort(reverse=True)

for i in range(n):
    ropes[i] = ropes[i] * (i + 1)

print(max(ropes))

# IDEA
# 1. 로프를 병렬로 연결하면 각 로프에는 w/k만큼의 동일한 중량이 걸린다는 규칙이 있다.
# 2. '가장 작은 무게를 들 수 있는 로프가 들 수 있는 질량 * 병렬 연결 로프 갯수 = 최종 무게' 공식이 나온다
# 3. 가장 무거운 무게를 들 수 있는 로프 부터 내림차순하면, [가장큰값*1, ... 가장작은값*n-1] 과 같은 배열을 얻을 수 있다
# 4. 이때 가장 큰 값을 print하면, '들어올릴 수 있는 물체의 최대 중량'을 구할 수 있다.