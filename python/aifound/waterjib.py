from collections import deque

def bfs(m, n, d):
    q = deque()
    vis = set()
    par = {}
    q.append((0, 0))
    vis.add((0, 0))
    found = None
    while q:
        x, y = q.popleft()
        if x == d or y == d:
            found = (x, y)
            break
        nxt = []
        nxt.append((m, y))
        nxt.append((x, n))
        nxt.append((0, y))
        nxt.append((x, 0))
        pourA = min(x, n - y)
        pourB = min(y, m - x)
        nxt.append((x - pourA, y + pourA))
        nxt.append((x + pourB, y - pourB))
        for s in nxt:
            if s not in vis:
                vis.add(s)
                par[s] = (x, y)
                q.append(s)
    if not found:
        print('No solution possible.')
        return
    path = []
    cur = found
    while cur != (0, 0):
        path.append(cur)
        cur = par[cur]
    path.append((0, 0))
    path.reverse()