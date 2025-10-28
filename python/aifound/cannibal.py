from collections import deque

def valid(a, b, A, B):
    if a < 0 or b < 0 or A < 0 or B < 0:
        return False
    if a > 0 and b > a:
        return False
    if A > 0 and B > A:
        return False
    return True

def bfs():
    init = (3, 3, 'L')
    goal = (0, 0, 'R')
    q = deque()
    vis = set()
    par = {}
    act = {}
    q.append(init)
    vis.add(init)
    while q:
        s = q.popleft()
        a, b, side = s
        A = 3 - a
        B = 3 - b
        if s == goal:
            path = []
            cur = s
            while cur != init:
                path.append(act[cur])
                cur = par[cur]
            path.reverse()
            for step in path:
                print(step)
            print('All agents crossed safely!')
            return
        moves = []
        for da in range(3):
            for db in range(3):
                if 1 <= da + db <= 2:
                    if side == 'L':
                        na, nb = a - da, b - db
                        nA, nB = A + da, B + db
                        nside = 'R'
                    else:
                        na, nb = a + da, b + db
                        nA, nB = A - da, B - db
                        nside = 'L'
                    if valid(na, nb, nA, nB):
                        ns = (na, nb, nside)
                        if ns not in vis:
                            vis.add(ns)
                            par[ns] = s
                            act[ns] = f"Move {da} A, {db} B to {nside} -> {ns}"
                            q.append(ns)
    print('No solution found.')

def main():
    print('Solution steps:')
    bfs()

if __name__ == '__main__':
    main()
