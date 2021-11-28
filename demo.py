from cube import Cube
from solver import Solver
from helper import getScramble

cb = Cube()

scramble = getScramble(10)
print("Scramble:", scramble)
cb.doMoves(scramble)
print(cb)

solver = Solver(cb)
solver.solveCube(optimize=True)

moves = solver.getMoves(decorated=True)
print(moves)