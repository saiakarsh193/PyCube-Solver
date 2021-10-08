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

### Notation  
There are rules and methods that need to be followed in order to use the program. 
- The moves in a rubik's cube are defines as follows,    
  <img src="https://jperm.net/images/notation.png" alt="Rubik's Cube Moves" style="width: 400px;"/>  
- The cube printing format is defined as  
  ```
   Y
  RGOB
   W
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