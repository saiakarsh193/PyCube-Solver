from cube import Cube
from solver import Solver
from helper import getScramble

c = Cube()
c.doMoves(getScramble(10))
c.doMoves("xy")

s = Solver(c)
moves = s.solveCube(debug = True)
print("Moves:")
for mv in moves:
    print(mv)