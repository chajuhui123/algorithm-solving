# 1946

import sys
input = sys.stdin.readline

t = int(input())

# for _ in range(t):
#     n = int(input())
#     answer = 0
#     ranks = []

#     for __ in range(n):
#         doc_rank, interview_rank = map(int, input().split())
#         ranks.append((doc_rank, interview_rank))

#     for i in range(n):
#         isAble = True
#         for j in range(n):
#             if i != j:
#                 now_doc, now_interview = ranks[i][0], ranks[i][1]
#                 other_doc, other_interview = ranks[j][0], ranks[j][1]

#                 if now_doc > other_doc and now_interview > other_interview: # 서류 심사 결과와 면접 성적이 모두 떨어진다면
#                     isAble = False
                    
#         if isAble == True:
#             answer += 1

#     print(answer)

for _ in range(t):
    n = int(input())
    rank = [list(map(int, input().split())) for _ in range(n)]
    sorted_rank = sorted(rank) # 1. 0번째 인덱스에 위치한 서류 결과를 기준으로 정렬됨 (서류 결과가 좋은 순으로 정렬된 상태)
    
    result = 1 # 2. 서류 심사 1위는 무조건 포함되므로 1부터 시작
    best = 0
    
    for i in range(1, n):
        # 2. 면접 성적만 비교하여 현재 탐색 중인 아이템의 면접 결과가,
        # 현재까지 제일 성적이 좋았던 값보다 더 좋은 성적 (높은 등수(숫자 작은)) 인 경우
        # top 변경
        if sorted_rank[i][1] < sorted_rank[best][1]:
            top = i
            result += 1
    
    print(result)


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