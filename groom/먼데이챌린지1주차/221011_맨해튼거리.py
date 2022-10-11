# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

arr = list(map(int, input().split()))
arr.sort()

x = abs(arr[0] - arr[3])
y = abs(arr[1] - arr[2])

print(x + y)

# IDEA
# Greedy한 선택을 할 수 있는 규칙을 찾아본다.
# 정렬 후, (가장 작은값 - 가장 큰값)의 절댓값, (두 번째로 작은값 - 두 번째로 큰값)의 절댓값 을 구하면 최장 맨해튼 거리가 보장된다.