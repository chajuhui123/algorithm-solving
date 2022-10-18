import sys
input = sys.stdin.readline

def binary_search(s, e, nums1, num):
    while s <= e:
        mid = (s+e) // 2
        
        if nums1[mid] == num:
            return 1
        elif nums1[mid] < num:
            s = mid+1
        else:
            e = mid-1
    return 0

t = int(input())
for _ in range(t):
    n = int(input())
    nums1 = list(map(int, input().split()))
    m = int(input())
    nums2 = list(map(int, input().split()))
    nums1.sort()

    for num in nums2:
        print(binary_search(0, n-1, nums1, num))


# IDEA
# 이진 탐색으로 빠르게 해당 숫자가 포함되어있는지 확인할 수 있다.