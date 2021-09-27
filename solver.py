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
        if(debug):
            print("After:")
            self.__cube.print()
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
