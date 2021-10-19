from cube import Cube
from solver import Solver
from helper import getScramble

c = Cube()
scramble = getScramble(10)
print(scramble)
c.doMoves(scramble)

s = Solver(c)
s.solveCube(debug = True)
moves = s.getMoves()
print("Moves:")
for mv in moves:
    print(mv)