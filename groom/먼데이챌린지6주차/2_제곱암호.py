import sys
import string
input = sys.stdin.readline

alpha_small = list(string.ascii_lowercase)

n = int(input())
arr = list(input().rstrip())

res = ''

for i in range(0, n, 2):
	ch = arr[i]
	num = int(arr[i+1])
	index = (alpha_small.index(ch) + (num * num)) % 26
	res += alpha_small[index]
	
print(res)

# 암호문의 길이가 n이라면, n/2개의 숫자와 n/2개의 알파벳 소문자로 이루어져 있다. 암호문의 길이는 항상 짝수이다.
# 암호문의 첫 글자는 항상 알파벳 소문자이며, 이후에는 항상 숫자와 알파벳 소문자가 번갈아 가며 등장한다.
# 원문은 n의 길이를 가지고 있으며, 모두 알파벳 소문자이다.
# 암호문의 첫 번째 문자부터 순서대로 아래의 복호화 과정을 거친다. 
# 첫 번째 문자는 문장의 가장 왼쪽 문자를 의미한다.
# i가 홀수일 때, 암호문의 i번째 문자를 알파벳의 사전 기준 다음 문자로 바꾸는 작업을 암호의 i+1번째 수의 제곱 번 시행한다. 작업이 끝난 뒤 변환된 알파벳을 원문의 맨 오른쪽에 추가한다.
# z에서 사전 기준 다음 문자로 바꿔야 하는 경우에는 a로 바뀌게 된다.
# => 홀수 번째 위치 문자는 <문자>이고, 짝수 번째 위치 문자는 <숫자 = 정수>라는 것을 파악할 수 있다