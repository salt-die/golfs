"""
Golfing tic-tac-toe with magic squares

m is our magic square it looks like:
    4 | 3 | 8
    9 | 5 | 1
    2 | 7 | 6
Note that all the rows, columns, and diagonals sum to 15.
We translate a player's move into a magic square value and then check if any
combinations of 3 moves from a player sum to 15. If any do, they win!

p is the list of the two players moves. (p[0] for player 0's moves, p[1] for
player 1's)

q is which player's turn it is.

b is our board and f() prints the board

We operate under a few constraints:
    An incorrect move should cause the program to crash or otherwise should
    not be accepted.

    The board cells should be labeled like a numpad, that is, a move in the
    top-left corner, say, would be entered with a '7' and bottom-center with a
    '2'.  The cell labels don't necessarily need to be shown.

    We do, however, need to show the board updated with the players moves
    including the starting and ending positions. (Preferably with horizontal
    and vertical seperators.)
"""

from itertools import*;m,p,q,r,s,l=dict(enumerate("276951438")),[[],[]],0,print,'─┼─┼─',' │ │ ';b=[*map(list,[l,s,l,s,l])]
def f(): r('\n'.join(map(''.join,b)))
f()
while m:
 i=int(input(f'P{q} move: '))-1;u=int(m.pop(i));p[q]+=[u];b[~(i//3*2)][i%3*2]='XO'[q];f()
 if any(sum(d)==15for d in combinations(p[q],3)):r(f'P{q} wins');m=0
 elif not m:r('Draw')
 q^=1