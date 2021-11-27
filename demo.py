from cube import Cube
from solver import Solver
from helper import getScramble

cb = Cube()

# to manually scramble the cube uncomment the following
# cb.doMoves("RUR'U'")

# to auto scramble the cube
cb.doMoves(getScramble(10))

print(cb)

solver = Solver(cb)
solver.solveCube()

# to get raw moves uncomment the following
# moves = solver.getMoves()
# for move in moves:
#     print(move)

# or for more detailed, decorated and condensed output
moves = solver.getMoves(decorated=True)
print(moves)