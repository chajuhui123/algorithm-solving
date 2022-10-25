# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
people = list(map(int, input().split()))

print(sum(people))

# IDEA
# 2명의 사람 제외하고는 모두 합이 0이 되는 쌍을 이루고 있다.
# 그래서 이 커플이 되지 않은 두 사람의 합을 구하는 것은 전체 리스트의 합을 구하는 것과 같다.