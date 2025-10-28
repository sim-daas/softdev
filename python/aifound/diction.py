def p():
    d = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E'}
    for i in range(5):
        print(' ' * (4 - i), end='')
        for n in range(2 * i + 1):
            x = min(n, (2 * i + 1) - n - 1) + 1
            print(d[x], end='')
        print()

p()
