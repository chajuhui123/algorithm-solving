
while True:
    password = input()
    if password == "end": exit(0)

    pass_arr = list(password)
    pass_arr_is_aeiou = []

    is_able = True
    aeiou = ['a', 'e', 'i', 'o', 'u']

    for item in pass_arr:
        if item in aeiou:
            pass_arr_is_aeiou.append(1)
        else:
            pass_arr_is_aeiou.append(-1)
    
    print(pass_arr_is_aeiou)
    print(pass_arr)

    # step 1. 모음 포함 해야함


