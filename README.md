# PyCube-Solver  
## Sai Akarsh (17-09-21)  

### Description  
Python program that models and solves a Rubik's cube (_as soon as the code is completed smh_) using the **CFOP** method.  
Its currently under development.  
**(CFOP : Cross, First two layers, Orientation of last layer, Permutation of last layer)**  

Right now, the program can solve the cross (white as base) pretty efficiently.  

The code for cube manipulation can be found in `cube.py`.  
The parsing, condenstion and validation for formulas can be found in `helper.py`.  

You can create a cube object and move it by using the following code  
  
```python
from cube import Cube
cb = Cube()
cb.doMoves("RUR'U'")
print(cb)
```
<br/>

The code for solving the cube can be found in `solver.py` and its helper data objects in `solver_data.py`.  

If you want to use the solver (assuming you scrambled the cube duh), add the following code to the above code  
  
```python
from solver import Solver
solver = Solver(cb)
solver.solveCube()
moves = solver.getMoves()
for move in moves:
    print(move)
```
_**Since its still under development, it does not totally solve the cube yet :(**_  

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
