# PyCube-Solver  
## Sai Akarsh (17-09-21)  

### Description  
Python program that solves the Rubik's cube using CFOP method.  
Its currently under development.  
Right now, the program can realign the cube and solve the base white cross pretty efficiently.  

You can create a cube object and move it using formulas.The code for cube manipulation can be found in `cube.py`.  
The parsing and validation for formulas is done and can be found in `helper.py`.  

You can create a cube object and move it by using the following code  

```python
from cube import Cube
cb = Cube()
cb.doMoves("RUR'U'")
print(cb)
```

If you want to use the cube solver (assuming you scrambled the cube), add the following code  

```python
from solver import Solver
solver = Solver(cb)
solver.solveCube()
moves = solver.getMoves()
for move in moves:
    print(move)
```
_**Since its still under development, it does not totally solve the cube but rather does the white cross**_  

### Notation  
There are rules and methods that need to be followed in order to use the program. 
- The moves in a rubik's cube are defines as follows,    
  <img src="https://jperm.net/images/notation.png" alt="Rubik's Cube Moves" style="width: 400px;"/>  
- The cube printing format is defined as  
  ```
      YYY
      YYY
      YYY
  RRR GGG OOO BBB
  RRR GGG OOO BBB
  RRR GGG OOO BBB
      WWW
      WWW
      WWW
  ```
- The cube index format (if you want to tinker with the code) is defined as  
  ```
   5
  3012
   4
  ```
- The cube front face is assumed as Green and the top face is assumed as Yellow (If input is given otherwise, it automatically reorients itself)  
- The cube face notation followed in this code,  
  <img src="https://i.ibb.co/7W8mHRN/cubenotation.jpg" alt="ThreeJS Coordinates" style="width: 400px;"/>
