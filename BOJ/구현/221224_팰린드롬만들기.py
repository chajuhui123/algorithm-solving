# 1213

import sys
input = sys.stdin.readline

# 팰린드롬?
# 짝수 개인 경우 절반으로 나눴을 때, 마주본 인덱스의 문자끼리 일치하는 경우 
# 홀수 개인 경우 가운데 하나를 제외한 후, 절반으로 나눴을 때, 마주본 인덱스의 문자끼리 일치하는 경우 
# ㄴ 홀수 개인 알파벳은 1개만 존재해야 한다.

alphabets = sorted(input().strip()) # 사전순으로 앞서는 것을 출력하는 조건이 있으므로, 정렬 수행

print(len(alphabets))
print(alphabets)

if len(alphabets) % 2 == 0:
    # half = 각 존재하는 알파벳 1/2 씩으로 구성된 리스트
    # reversed_half = half를 거꾸로 뒤집은 리스트
    # answer = half + reversed_half 을 문자열로 치환
    print()
else:
    print()