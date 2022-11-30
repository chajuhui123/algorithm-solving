# 11656

s = str(input())
s_list = []

for _ in s:
    s_list.append(s)
    s = s[1:]

for i in sorted(s_list):
    print(i)

# IDEA
# s=s[1:] 을 통해 1자씩 줄여가며 접미사를 만든다
# s_list에 저장된 접미사들을 sorted 메서드를 통해 정렬한다.