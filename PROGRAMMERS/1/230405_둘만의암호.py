def solution(s, skip, index):
    answer = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz" # 알파벳 a~z
    
    for item in skip:
        if item in alphabet:
            alphabet = alphabet.replace(item, "") # skip 문자에 해당할경우 replace
    
    for i in s:
        change = alphabet[(alphabet.index(i) + index) % len(alphabet)] # s의 문자 인덱스 + index를 alphabet의 길이로 나눈 나머지를 알파벳으로 변환
        answer += change
    
    return answer


# IDEA
# 문제에서 문자열 규칙을 찾아
# 문자열을 다루는 문제이다!