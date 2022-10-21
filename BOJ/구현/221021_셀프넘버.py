# 4673

origin = set(range(1, 10001))
delete = set()

for i in range(1, 10001): # ex. i = 33
    for j in str(i): # j = '3', '3'
        i += int(j) # i = 33 + 3 + 3 = 39
    delete.add(i) # 생성자 있는 숫자

self_num = sorted(origin - delete) # 생성자 없는 숫자
for num in self_num:
    print(num)