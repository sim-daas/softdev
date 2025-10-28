import random
class Env:
    def __init__(self, g, w, p):
        self.s = [[[] for _ in range(4)] for _ in range(4)]
        self.g = g
        self.w = w
        self.p = p
        self.s[g[0]][g[1]].append('G')
        self.s[w[0]][w[1]].append('W')
        for x, y in p:
            self.s[x][y].append('P')
    def prc(self, x, y):
        r = []
        if 'G' in self.s[x][y]: r.append('Glitter')
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<4 and 0<=ny<4:
                if 'P' in self.s[nx][ny]: r.append('Breeze')
                if 'W' in self.s[nx][ny]: r.append('Stench')
        return list(set(r))
    def bump(self, x, y):
        return not (0<=x<4 and 0<=y<4)
    def scream(self, x, y, d):
        dx, dy = d
        nx, ny = x+dx, y+dy
        while 0<=nx<4 and 0<=ny<4:
            if 'W' in self.s[nx][ny]:
                self.s[nx][ny].remove('W')
                return True
            nx += dx
            ny += dy
        return False
class Ag:
    def __init__(self):
        self.x, self.y = 0,0
        self.k = [['U']*4 for _ in range(4)]
        self.a = True
        self.g = False
        self.d = False
        self.t = []
        self.path = [(0,0)]
    def inf(self, p):
        inf = []
        if 'Breeze' in p:
            for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                nx,ny = self.x+dx,self.y+dy
                if 0<=nx<4 and 0<=ny<4 and self.k[nx][ny]=='U':
                    inf.append(f'Pit?({nx},{ny})')
        if 'Stench' in p:
            for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                nx,ny = self.x+dx,self.y+dy
                if 0<=nx<4 and 0<=ny<4 and self.k[nx][ny]=='U':
                    inf.append(f'Wumpus?({nx},{ny})')
        if not p: inf.append('Safe cell.')
        return inf
    def upd(self, p):
        self.k[self.x][self.y] = 'S'
        if 'Breeze' in p:
            for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                nx,ny = self.x+dx,self.y+dy
                if 0<=nx<4 and 0<=ny<4 and self.k[nx][ny]=='U':
                    self.k[nx][ny] = 'P?'
        if 'Stench' in p:
            for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                nx,ny = self.x+dx,self.y+dy
                if 0<=nx<4 and 0<=ny<4 and self.k[nx][ny]=='U':
                    self.k[nx][ny] = 'W?'
    def act(self, p, e):
        if 'Glitter' in p and not self.g:
            self.g = True
            self.t.append('Grab Gold')
            return True
        if 'Stench' in p and self.a:
            for d in [(0,1),(1,0),(0,-1),(-1,0)]:
                nx,ny = self.x+d[0],self.y+d[1]
                if 0<=nx<4 and 0<=ny<4 and self.k[nx][ny]=='W?':
                    sc = e.scream(self.x,self.y,d)
                    self.a = False
                    if sc:
                        self.t.append('Shoot '+str(d))
                        self.t.append('Scream heard')
                        self.k[nx][ny]='S'
                        return False
        for d in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx,ny = self.x+d[0],self.y+d[1]
            if 0<=nx<4 and 0<=ny<4 and self.k[nx][ny]=='S' and (nx,ny) not in self.path:
                self.x,self.y = nx,ny
                self.path.append((nx,ny))
                self.t.append('Move '+str((nx,ny)))
                return False
        for d in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx,ny = self.x+d[0],self.y+d[1]
            if 0<=nx<4 and 0<=ny<4 and self.k[nx][ny]=='U':
                self.x,self.y = nx,ny
                self.path.append((nx,ny))
                self.t.append('Move '+str((nx,ny)))
                return False
        return False
    def ret(self):
        if self.g and (self.x,self.y)==(0,0):
            self.t.append('Climb out')
            return True
        if self.g:
            if self.path[-2]==(0,0):
                self.x,self.y=0,0
                self.t.append('Move (0,0)')
                self.t.append('Climb out')
                return True
            else:
                self.x,self.y=self.path[-2]
                self.t.append('Move '+str(self.path[-2]))
        return False
    def dead(self, e):
        if 'P' in e.s[self.x][self.y]:
            self.t.append('Fell in Pit')
            return True
        if 'W' in e.s[self.x][self.y]:
            self.t.append('Eaten by Wumpus')
            return True
        return False
def sim(g, w, p):
    e = Env(g, w, p)
    a = Ag()
    while True:
        print(f'Agent at ({a.x},{a.y})')
        pr = e.prc(a.x,a.y)
        print('Percepts:',pr)
        inf = a.inf(pr)
        print('Inference:',inf)
        a.upd(pr)
        if a.dead(e):
            print('Action:',a.t[-1])
            print('Final Result: FAIL')
            break
        if a.act(pr,e):
            print('Action:',a.t[-1])
        else:
            print('Action:',a.t[-1] if a.t else 'None')
        if a.g:
            while not a.ret():
                print(f'Agent at ({a.x},{a.y})')
                print('Action:',a.t[-1])
            print(f'Agent at ({a.x},{a.y})')
            print('Action:',a.t[-1])
            print('Final Result: SUCCESS')
            break
def tc1():
    sim((1,2),(2,1),[(0,1),(2,3)])
def tc2():
    sim((3,3),(1,2),[(0,1),(1,1)])
if __name__=='__main__':
    print('Test Case 1:')
    tc1()
    print('\nTest Case 2:')
    tc2()
