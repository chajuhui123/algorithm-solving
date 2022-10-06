n = int(input())

dotObj = {
    'Q1': 0,
    'Q2': 0,
    'Q3': 0,
    'Q4': 0,
    'AXIS': 0
}

for _ in range(n):
    x, y = map(int, input().split(' '))

    if x == 0 or y == 0:
        dotObj['AXIS'] += 1
    elif x > 0 and y > 0:
        dotObj['Q1'] += 1
    elif x < 0 and y > 0:
        dotObj['Q2'] += 1
    elif x < 0 and y < 0:
        dotObj['Q3'] += 1
    elif x > 0 and y < 0:
        dotObj['Q4'] += 1

for key, value in dotObj.items():
    print('%s: %d' % (key, value))