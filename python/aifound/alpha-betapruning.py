import random

def p(b):
    for r in b:
        print(' '.join(r))
    print()

def w(b, s):
    for i in range(4):
        if all(b[i][j]==s for j in range(4)): return True
        if all(b[j][i]==s for j in range(4)): return True
    if all(b[i][i]==s for i in range(4)): return True
    if all(b[i][3-i]==s for i in range(4)): return True
    return False

def f(b):
    return all(b[i][j]!='.' for i in range(4) for j in range(4))

def sc(b):
    if w(b,'X'): return 1
    if w(b,'O'): return -1
    return 0

def moves(b):
    return [(i,j) for i in range(4) for j in range(4) if b[i][j]=='.']

mc = 0

def mm(b, turn, d=4):
    global mc
    mc += 1
    if w(b,'X') or w(b,'O') or f(b) or d==0: return sc(b)
    if turn:
        v = -2
        for i,j in moves(b):
            b[i][j] = 'X'
            v = max(v, mm(b,0,d-1))
            b[i][j] = '.'
        return v
    else:
        v = 2
        for i,j in moves(b):
            b[i][j] = 'O'
            v = min(v, mm(b,1,d-1))
            b[i][j] = '.'
        return v

ac = 0

def ab(b, turn, a, be, d=4):
    global ac
    ac += 1
    if w(b,'X') or w(b,'O') or f(b) or d==0: return sc(b)
    if turn:
        v = -2
        for i,j in moves(b):
            b[i][j] = 'X'
            v = max(v, ab(b,0,a,be,d-1))
            b[i][j] = '.'
            a = max(a,v)
            if be <= a: break
        return v
    else:
        v = 2
        for i,j in moves(b):
            b[i][j] = 'O'
            v = min(v, ab(b,1,a,be,d-1))
            b[i][j] = '.'
            be = min(be,v)
            if be <= a: break
        return v

def h(b):
    while True:
        try:
            i,j = map(int,input('Move (row col): ').split())
            if b[i][j]=='.': return i,j
        except: pass

def ai(b, alg):
    best = -2
    mv = None
    for i,j in moves(b):
        b[i][j] = 'X'
        if alg=='mm':
            v = mm(b,0,4)
        else:
            v = ab(b,0,-2,2,4)
        b[i][j] = '.'
        if v > best:
            best = v
            mv = (i,j)
    return mv

def play(alg):
    global mc, ac
    b = [['.']*4 for _ in range(4)]
    turn = random.choice([0,1])
    mc = 0
    ac = 0
    while True:
        p(b)
        if w(b,'X'): print('AI wins'); break
        if w(b,'O'): print('You win'); break
        if f(b): print('Draw'); break
        if turn:
            print('AI move')
            i,j = ai(b,alg)
            b[i][j] = 'X'
        else:
            print('Your move')
            i,j = h(b)
            b[i][j] = 'O'
        turn = 1-turn
    if alg=='mm': print('Minimax nodes:',mc)
    else: print('AlphaBeta nodes:',ac)

if __name__=='__main__':
    print('Choose AI: 1-Minimax 2-AlphaBeta')
    c = input()
    if c=='1': play('mm')
    else: play('ab')
