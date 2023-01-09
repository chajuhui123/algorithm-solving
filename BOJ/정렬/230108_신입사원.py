# 1946

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    answer = 0
    ranks = []

    for __ in range(n):
        doc_rank, interview_rank = map(int, input().split())
        ranks.append((doc_rank, interview_rank))

    for i in range(n):
        isAble = True
        for j in range(n):
            if i != j:
                now_doc, now_interview = ranks[i][0], ranks[i][1]
                other_doc, other_interview = ranks[j][0], ranks[j][1]

                if now_doc > other_doc and now_interview > other_interview: # 서류 심사 결과와 면접 성적이 모두 떨어진다면
                    isAble = False
                    
        if isAble == True:
            answer += 1

    print(answer)



'''
IDEA1.
3 2 => X O, O X, X O, O O => O
1 4 => O X, O X, O X, O O => O
4 1 => X O, X O, O X, O O => O
2 3 => O X, X O, O X, O O => O
5 5 => X X, X X, X X, X X => X

이처럼 서류 심사 결과와 면접 성적이 모두 떨어지는(X X) 경우가 하나라도 있다면 선발할 수 없다.
모든 경우의 수를 따지기 위해 완전탐색을 써야할 것 같다. => BUT 시간 초과
'''

'''
IDEA2.

'''