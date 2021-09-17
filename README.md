# PyCube-Solver

## Made by Sai Akarsh (17-09-21)

### Description

Code that solves the Rubik's cube using CFOP and is written in python.
Its under development. The basic cube object, moves, and parsing is done.

You can create a cube object and move it by doing

```python
from cube import Cube
cb = Cube()
cb.doMoves("RUR'U'")
cb.print()

```

### Note

The cube object needs a few rules to not cause perspective issues.

The cube printing format is defined as

```
 Y
RGOB
 W
```

The cube front face is assumed as Green and the top face is assumed as Yellow. (If input is given otherwise, it automatically reorients itself).