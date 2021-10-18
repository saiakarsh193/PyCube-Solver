from cube import Cube
from solver import Solver
from helper import getScramble

c = Cube()
scramble = "FLFDB'UR'F'"
# scramble = "FLFDB'Uxy"
# c.doMoves(getScramble(10))
c.doMoves(scramble)

s = Solver(c)
s.solveCube(debug = True)
moves = s.getMoves()
print("Moves:")
for mv in moves:
    print(mv)