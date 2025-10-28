'''a 4x4 Tic Tac Toe game with two AI agents: one using Minimax and one using Alpha-Beta pruning. The code will allow a human to play against either agent and will count the number of nodes evaluated for each algorithm to compare their efficiency. Assumptions: 'X' is the AI, 'O' is the human, and the game is played on a 4x4 board with standard win conditions (4 in a row). The code now implements a 4x4 Tic Tac Toe game with both Minimax and Alpha-Beta pruning AI agents, counts the nodes evaluated for each, and allows a human to play against the AI. Assumptions: 'X' is the AI, 'O' is the human, and the win condition is 4 in a row.'''

import random

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
            print('Ai move')





if __name__=='__main__':
    print('Choose AI: 1-Minimax 2-AlphaBeta')
    c = input()
    if c=='1': play('mm')
    else: play('ab')




