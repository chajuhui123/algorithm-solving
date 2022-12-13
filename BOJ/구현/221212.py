# target : string
# alphabets : string
# 특정 문자열(target)을 몇 번 제거할 수 있는지

def count_delete_alphabet_order(target, alphabets):
    count = 0
    while True:
        index_target = alphabets.find(target)
        if index_target == -1:
            break
        else :
            count += 1
            alphabets = alphabets[0 : index_target] + alphabets[index_target+len(target) :len(alphabets)]
    return count



from itertools import permutations

# given : string
# alphabets : string
def count_delete_alphabet(given, alphabets):
    count = 0
    enable_alphabets = []

    # 순열 (permutation) 서로 다른 n 개 중 r 개를 골라 순서를 정해 나열하는 가짓수 
    # 가능한 모든 순열 조합을 탐색하며, alphabets에서 given에 대한 순열 조합을 제거할 때, 몇 번 제거 가능한지 return 한다.
    for item in permutations(list(given), 6):
        enable_alphabets.append(''.join(item))
    enable_alphabets = list(set(enable_alphabets))

    for target in enable_alphabets:
        while True:
            index_target = alphabets.find(target)
            if index_target == -1:
                break
            else :
                count += 1
                alphabets = alphabets[0 : index_target] + alphabets[index_target+len(target) :len(alphabets)]
    return count