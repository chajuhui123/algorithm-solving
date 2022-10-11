# 2529

def isAbleSign(x, y, op) :
  if op == '<' :
    if x > y : return False
  if op == '>' :
    if x < y : return False
  return True

def checkWithSign(index, num) :
  if index == n+1 : # 부등호가 n개 입력되니까, 숫자는 n+1개이므로 n+1이 되면 종료
    ans.append(num)
    return
  
  for i in range(10) : # 0~9 까지 검사
    if check[i]: continue # 해당 숫자를 이미 사용했다면 pass

    if index == 0 or isAbleSign(num[index-1], str(i), a[index-1]): # 이전 값이랑 비교
      check[i] = True
      checkWithSign(index+1, num + str(i))
      check[i] = False

n = int(input())
a = input().split()

ans = []
check = [False] * 10 # 0~9 숫자를 사용했는지 안 했는지 체크

# 가능한 모든 조합 구하기
checkWithSign(0, '')
ans.sort()

print(ans[-1])
print(ans[0])

# IDEA
# 재귀함수를 활용하여, 0~9 숫자를 하나씩 대입하고
# isAbleSign 함수를 호출해 부등호 공식에 성립하는지 체크한다
# (부등호 공식 성립하는) 가능한 모든 조합을 ans 배열에 저장한 후, 가장 큰 값과 가장 작은 값을 print 해준다.