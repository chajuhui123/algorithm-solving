# tree : array
# skills : array
def skill_set(skills, require):

    # root 구하기
    root = -1
    for i in range(0, len(skills)):
        if i == skills[i]:
            root = i

    # 찍어야하는 스킬 하나씩 탐색
    need_skill = []
    
    # 각 스킬의 부모 검사하며 need_skill에 추가하고
    # root 노드인 경우 탐색 중지함 
    for skill in require:
        need_skill.append(skill)
        if skill == root: continue
        next = skills[skill]
        need_skill.append(next)

        while True:
            if next == root : break
            next = skills[next]
            need_skill.append(next)

    # 부모 노드 중복 제거후 갯수 리턴
    return len(list(set(need_skill)))
            


# Tree 구조를 활용하기
# 각 노드의 상위 부모 노드 갯수를 구하고
# 갯수를 세는 부모 노드 값은 중복되면 안됨 따라서 각 노드의 부모노드를 list(set)에 저정하고,
# length 값을 return 하면 좋을 것 같다
# Tree 인줄앗앗는디 아닌듯..? 구현..?
