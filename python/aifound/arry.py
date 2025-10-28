def p():
    c = ['A', 'B', 'C', 'D', 'E']
    for i in range(5):
        print(' ' * (4 - i), end='')
        for n in range(2 * i + 1):
            x = min(n, (2 * i + 1) - n - 1)
            print(c[x], end='')
        print()

p()