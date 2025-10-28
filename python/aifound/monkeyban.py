from collections import deque

def bfs():
    locs = ['A', 'B', 'C']
    init = ('A', 'B', False, False)  # (monkey, chair, on_chair, has_banana)
    goal = (None, None, True, True)
    q = deque()
    vis = set()
    par = {}
    act = {}
    q.append(init)
    vis.add(init)
    while q:
        s = q.popleft()
        m, c, on, b = s
        if b:
            path = []
            cur = s
            while cur != init:
                path.append(act[cur])
                cur = par[cur]
            path.reverse()
            for step in path:
                print(step)
            print('Monkey got the bananas!')
            return
        # 1. Walk
        if not on:
            for l in locs:
                if l != m:
                    ns = (l, c, on, b)
                    if ns not in vis:
                        vis.add(ns)
                        par[ns] = s
                        act[ns] = f'Walk to {l}'
                        q.append(ns)
        # 2. Push chair
        if not on and m == c:
            for l in locs:
                if l != c:
                    ns = (l, l, on, b)
                    if ns not in vis:
                        vis.add(ns)
                        par[ns] = s
                        act[ns] = f'Push chair to {l}'
                        q.append(ns)
        # 3. Climb chair
        if not on and m == c:
            ns = (m, c, True, b)
            if ns not in vis:
                vis.add(ns)
                par[ns] = s
                act[ns] = 'Climb chair'
                q.append(ns)
        # 4. Grab bananas
        if on and m == 'C':
            ns = (None, None, True, True)
            if ns not in vis:
                vis.add(ns)
                par[ns] = s
                act[ns] = 'Grab bananas'
                q.append(ns)
    print('No solution found.')

def main():
    print('Solution steps:')
    bfs()

if __name__ == '__main__':
    main()
