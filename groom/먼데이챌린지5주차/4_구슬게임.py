import sys
from collections import defaultdict

input = sys.stdin.readline

# 재귀 제한 풀기
sys.setrecursionlimit(10 ** 8)

# 입력받기
n, m, k = map(int, input().split())
dp = defaultdict()

def solve(cur, limit):
    # key는 [구름이가 가지고 있는 구슬의 개수, 남아있는 경기의 수] 로 저장!
    key = str([cur, limit])

    # 종료 조건들 서술
    if key in dp:
        # 이미 탐색한 상황이라면 종료
        return dp[key]
    if cur == 0 or cur == n + m:
        # 둘 중 아무나 구슬을 모두 잃은 상황
        return 1
    if limit == 0:
        # 남은 경기의 수가 0 이면서, 둘 다 구슬을 가지고 있는 경우 종료
        return 0
    
    cnt = 0
		
    # 구름이가 이기는 경우
    cnt += solve(cur + 1, limit - 1)
    # 비기는 경우
    cnt += solve(cur, limit - 1)
    # 지는 경우
    cnt += solve(cur - 1, limit - 1)
		
    # MOD 연산
    cnt %= 100000007
    # 상황에 값 부여
    dp[key] = cnt

    return cnt

print(solve(n, k))

# IDEA
# 특정 상황에서의 경우의 수를 찾는 문제이기 때문에, 동적 프로그래밍으로 해결하는 문제 유형
# 가위바위보를 통해서 승리, 패배, 무승부라는 결과에 따라서 진행된다.
# 또한 구름의 구슬, 친구의 구슬 갯수를 살펴보며 게임 종료 여부를 파악할 수 있다.
# 게임이 종료되는 조건은 구름이가 구슬을 모두 잃었을 때, 구름이가 구슬을 모두 얻었을 때, 경기의 횟수가 K번이 되었을 때 총 3가지로 정리할 수 있다.