from itertools import combinations

while True:
    nums = list(input().split(" "))[1:]
    if nums == []: break
    lottos = list(combinations(nums, 6))

    for lotto in lottos:
        print(" ".join(lotto))
    print()

