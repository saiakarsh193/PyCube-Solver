from cube import Cube

class Solver():
    def __init__(self, cube):
        self.__cube = Cube(faces = cube.getFaces())
        self.__forms = []

    def solveCube(self, debug = False):
        if(debug):
            print("Before:")
            self.__cube.print()
        self.__alignFaces()
        self.__baseCross()
        if(debug):
            print("After:")
            self.__cube.print()
        return True
    
    def getMoves(self):
        return self.__forms

    def __move(self, form):
        self.__cube.doMoves(form)
        self.__forms.append(form)

    def __alignFaces(self):
        if(self.__cube.cube[1][1][1] == "G"):
            self.__move("y")
        elif(self.__cube.cube[2][1][1] == "G"):
            self.__move("y2")
        elif(self.__cube.cube[3][1][1] == "G"):
            self.__move("y'")
        elif(self.__cube.cube[4][1][1] == "G"):
            self.__move("x")
        elif(self.__cube.cube[5][1][1] == "G"):
            self.__move("x'")
        if(self.__cube.cube[1][1][1] == "Y"):
            self.__move("z'")
        elif(self.__cube.cube[4][1][1] == "Y"):
            self.__move("z2")
        elif(self.__cube.cube[3][1][1] == "Y"):
            self.__move("z")

    def __baseCross(self):
        if(self.__cube.cube[4][0][1] == "W" and self.__cube.cube[4][1][0] == "W" and self.__cube.cube[4][1][2] == "W" and self.__cube.cube[4][2][1] == "W" and self.__cube.cube[0][2][1] == "G" and self.__cube.cube[1][2][1] == "O" and self.__cube.cube[2][2][1] == "B" and self.__cube.cube[3][2][1] == "R"):
            return
        if(self.__cube.cube[5][0][1] == "W"):
            if(self.__cube.cube[2][0][1] == self.__cube.cube[2][1][1]):
                self.__move("B2")
            elif(self.__cube.cube[2][0][1] == self.__cube.cube[3][1][1]):
                self.__move("U'")
            else:
                self.__move("U")
        if(self.__cube.cube[5][1][2] == "W"):
            if(self.__cube.cube[1][0][1] == self.__cube.cube[1][1][1]):
                self.__move("R2")
            elif(self.__cube.cube[1][0][1] == self.__cube.cube[2][1][1]):
                self.__move("U'")
            else:
                self.__move("U")
        if(self.__cube.cube[5][2][1] == "W"):
            if(self.__cube.cube[0][0][1] == self.__cube.cube[0][1][1]):
                self.__move("F2")
            elif(self.__cube.cube[0][0][1] == self.__cube.cube[1][1][1]):
                self.__move("U'")
            else:
                self.__move("U")
        if(self.__cube.cube[5][1][0] == "W"):
            if(self.__cube.cube[3][0][1] == self.__cube.cube[3][1][1]):
                self.__move("L2")
            elif(self.__cube.cube[3][0][1] == self.__cube.cube[0][1][1]):
                self.__move("U'")
            else:
                self.__move("U")
        # self.__baseCross()
