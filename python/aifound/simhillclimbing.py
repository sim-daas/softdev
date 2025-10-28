import random
import copy

def pb(b):
    for r in b:
        print(" ".join(str(x) for x in r))
    print()

def bstr(b):
    return "\n".join(" ".join(str(x) for x in r) for r in b)

def h(b):
    n = len(b)
    p = [(i, r.index(1)) for i, r in enumerate(b)]
    c = 0
    for i in range(n):
        for j in range(i+1, n):
            if p[i][1] == p[j][1] or abs(p[i][0] - p[j][0]) == abs(p[i][1] - p[j][1]):
                c += 1
    return c

def rb(n=8):
    b = [[0]*n for _ in range(n)]
    for i in range(n):
        col = random.randint(0, n-1)
        b[i][col] = 1
    return b

def nb(b):
    n = len(b)
    res = []
    for r in range(n):
        c = b[r].index(1)
        for nc in range(n):
            if nc != c:
                nb_ = [row[:] for row in b]
                nb_[r][c] = 0
                nb_[r][nc] = 1
                res.append(nb_)
    return res

def shc(s):
    cur = copy.deepcopy(s)
    it = 0
    while True:
        it += 1
        nbs = nb(cur)
        nxt = None
        for n in nbs:
            if h(n) < h(cur):
                nxt = n
                break
        if nxt is None:
            break
        cur = nxt
        if h(cur) == 0:
            break
    return cur, it

def sahc(s):
    cur = copy.deepcopy(s)
    it = 0
    while True:
        it += 1
        nbs = nb(cur)
        best = min(nbs, key=h)
        if h(best) >= h(cur):
            break
        cur = best
        if h(cur) == 0:
            break
    return cur, it

def runexp(runs=20):
    n = 8
    ss = 0
    sa = 0
    sit = []
    sait = []
    for _ in range(runs):
        b = rb(n)
        s1, i1 = shc(b)
        s2, i2 = sahc(b)
        if h(s1) == 0:
            ss += 1
            sit.append(i1)
        if h(s2) == 0:
            sa += 1
            sait.append(i2)
    print(f"Simple Hill Climbing Success Rate: {ss}/{runs}")
    print(f"Steepest Ascent Hill Climbing Success Rate: {sa}/{runs}")
    if sit:
        print(f"Avg iterations (simple): {sum(sit)/len(sit):.2f}")
    if sait:
        print(f"Avg iterations (steepest): {sum(sait)/len(sait):.2f}")
    if ss > sa:
        print("Simple Hill Climbing had a higher success rate.")
    elif ss < sa:
        print("Steepest Ascent Hill Climbing had a higher success rate.")
    else:
        print("Both methods had the same success rate.")

print("Initial Board:")
tb = rb()
pb(tb)
h_init = h(tb)
print(f"Initial Heuristic: {h_init}")

s1, i1 = shc(tb)
h_final1 = h(s1)
print("Simple Hill Climbing Solution:")
pb(s1)
print(f"Final Heuristic: {h_final1}, Iterations: {i1}")
if h_final1 == 0:
    print("Simple Hill Climbing: solution found.")
else:
    print("Simple Hill Climbing: local maximum or plateau.")

s2, i2 = sahc(tb)
h_final2 = h(s2)
print("Steepest Ascent Hill Climbing Solution:")
pb(s2)
print(f"Final Heuristic: {h_final2}, Iterations: {i2}")
if h_final2 == 0:
    print("Steepest Ascent Hill Climbing: solution found.")
else:
    print("Steepest Ascent Hill Climbing: local maximum or plateau.")

runexp(runs=1000)
