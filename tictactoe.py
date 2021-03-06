"""
Golfing tic-tac-toe with magic squares

m is our magic square it looks like:
    4 | 3 | 8
    9 | 5 | 1
    2 | 7 | 6
Note that all the rows, columns, and diagonals sum to 15.
We translate a player's move into a magic square value and then check if any
combinations of 3 moves from a player sum to 15. If any do, they win!

We operate under a few constraints:
    An incorrect move should cause the program to crash or otherwise should
    not be accepted.

    The board cells should be labeled like a numpad, that is, a move in the
    top-left corner, say, would be entered with a '7' and bottom-center with a
    '2'.  The cell labels don't necessarily need to be shown.

    We do, however, need to show the board updated with the players moves
    including the starting and ending positions. (Preferably with horizontal
    and vertical seperators.)

Here's a not-condensed version:
```
from itertools import combinations

moves_to_values = dict(enumerate([2, 7, 6, 9, 5, 1, 4, 3, 8]))
players_values = [[], []]
current_player = 0
board = [[' ', '│', ' ', '│', ' '],
         ['─', '┼', '─', '┼', '─'],
         [' ', '│', ' ', '│', ' '],
         ['─', '┼', '─', '┼', '─'],
         [' ', '│', ' ', '│', ' ']]

def print_board():
    print('\n'.join(''.join(row) for row in board))

print_board()

while moves_to_values:
    move = int(input('XO'[current_player] + ' move: ')) - 1
    players_values[current_player].append(moves_to_values.pop(move))
    board[~(move // 3 * 2)][move % 3 * 2] = 'XO'[current_player]
    print_board()
    if any(sum(d) == 15 for d in combinations(players_values[current_player], 3)):
        print('XO'[current_player] + ' wins')
        break
    current_player ^= 1
else:
    print('Draw')
```
"""

from itertools import*;m,p,q,r,s,l,a=dict(enumerate("276951438")),[[],[]],0,print,' │ │ ','─┼─┼─','XO';b=[*map(list,[s,l,s,l,s])];f=lambda:r('\n'.join(map(''.join,b)));f()
while m:
 i=int(input(a[q]+' move: '))-1;p[q]+=[int(m.pop(i))];b[~(i//3*2)][i%3*2]=a[q];f()
 if any(sum(d)==15for d in combinations(p[q],3)):r(a[q]+' wins');break
 q^=1
else:r('Draw')

