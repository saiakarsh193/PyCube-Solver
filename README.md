# PyCube-Solver

## Sai Akarsh (17-09-21)

### Description

Python program that solves the Rubik's cube using CFOP method.
Its currently under development.

You can currently create a cube object and move it using formulas.The code for cube manipulation can be found in `cube.py`.
The parsing and validation for formulas is done and can be found in `helper.py`.

You can create a cube object and move it by doing,

```python
from cube import Cube
cb = Cube()
cb.doMoves("RUR'U'")
cb.print()

```

### Note

The cube object needs a few rules to be followed in order to not cause perspective issues.

The cube printing format is defined as

```
 Y
RGOB
 W

```

The cube front face is assumed as Green and the top face is assumed as Yellow. (If input is given otherwise, it automatically reorients itself).