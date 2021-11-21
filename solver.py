from cube import Cube

movedata = {
    "R": ["R", "B", "L", "F"],
    "R'": ["R'", "B'", "L'", "F'"],
    "U": ["U", "U", "U", "U"],
    "U'": ["U'", "U'", "U'", "U'"],
    "L": ["L", "F", "R", "B"],
    "L'": ["L'", "F'", "R'", "B'"],
    "D": ["D", "D", "D", "D"],
    "D'": ["D'", "D'", "D'", "D'"],
    "F": ["F", "R", "B", "L"],
    "F'": ["F'", "R'", "B'", "L'"],
    "B": ["B", "L", "F", "R"],
    "B'": ["B'", "L'", "F'", "R'"]
    }

def moveMapper(side, form):
    moves = []
    for ch in form:
        if(ch.isalpha() or ch.isdigit()):
            moves.append(ch)
        else:
            moves[-1] += ch
    for i, item in enumerate(moves):
        if moves[i] in movedata:
            moves[i] = movedata[moves[i]][side]
    return ''.join(moves)

class Solver():
    def __init__(self, cube):
        self.cube = Cube(faces = cube.getFaces())
        self.faces = self.cube.cube
        self.forms = []

    def solveCube(self, debug = False):
        if(debug):
            print("Before:")
            print(self.cube)
        self.__alignFaces()
        self.__baseCross()
        self.__firstLayer()
        if(debug):
            print("After:")
            print(self.cube)
        return True
    
    def getMoves(self):
        return self.forms

    def __move(self, form):
        self.cube.doMoves(form)
        self.forms.append(form)

    def __alignFaces(self):
        if(self.faces[1][1][1] == "G"):
            self.__move("y")
        elif(self.faces[2][1][1] == "G"):
            self.__move("y2")
        elif(self.faces[3][1][1] == "G"):
            self.__move("y'")
        elif(self.faces[4][1][1] == "G"):
            self.__move("x")
        elif(self.faces[5][1][1] == "G"):
            self.__move("x'")
        if(self.faces[1][1][1] == "Y"):
            self.__move("z'")
        elif(self.faces[4][1][1] == "Y"):
            self.__move("z2")
        elif(self.faces[3][1][1] == "Y"):
            self.__move("z")

    def __baseCross(self):
        if(self.faces[4][0][1] == "W" and self.faces[4][1][0] == "W" and self.faces[4][1][2] == "W" and self.faces[4][2][1] == "W" and self.faces[0][2][1] == "G" and self.faces[1][2][1] == "O" and self.faces[2][2][1] == "B" and self.faces[3][2][1] == "R"):
            return
        if(self.faces[5][0][1] == "W" or self.faces[5][1][2] == "W" or self.faces[5][2][1] == "W" or self.faces[5][1][0] == "W"):
            if(self.faces[5][0][1] == "W"):
                if(self.faces[2][0][1] == self.faces[2][1][1]):
                    self.__move("B2")
                elif(self.faces[2][0][1] == self.faces[3][1][1]):
                    self.__move("U'")
                else:
                    self.__move("U")
            if(self.faces[5][1][2] == "W"):
                if(self.faces[1][0][1] == self.faces[1][1][1]):
                    self.__move("R2")
                elif(self.faces[1][0][1] == self.faces[2][1][1]):
                    self.__move("U'")
                else:
                    self.__move("U")
            if(self.faces[5][2][1] == "W"):
                if(self.faces[0][0][1] == self.faces[0][1][1]):
                    self.__move("F2")
                elif(self.faces[0][0][1] == self.faces[1][1][1]):
                    self.__move("U'")
                else:
                    self.__move("U")
            if(self.faces[5][1][0] == "W"):
                if(self.faces[3][0][1] == self.faces[3][1][1]):
                    self.__move("L2")
                elif(self.faces[3][0][1] == self.faces[0][1][1]):
                    self.__move("U'")
                else:
                    self.__move("U")
        elif((self.faces[4][0][1] == "W" and self.faces[0][2][1] != "G") or (self.faces[4][1][2] == "W" and self.faces[1][2][1] != "O") or (self.faces[4][2][1] == "W" and self.faces[2][2][1] != "B") or (self.faces[4][1][0] == "W" and self.faces[3][2][1] != "R")):
            if(self.faces[4][0][1] == "W" and self.faces[0][2][1] != "G"):
                side = 0
            elif(self.faces[4][1][2] == "W" and self.faces[1][2][1] != "O"):
                side = 1
            elif(self.faces[4][2][1] == "W" and self.faces[2][2][1] != "B"):
                side = 2
            else:
                side = 3
            self.__move(moveMapper(side, "F2"))
        else:
            for i in range(4):
                if(self.faces[i][0][1] == "W" or self.faces[i][1][2] == "W" or self.faces[i][2][1] == "W" or self.faces[i][1][0] == "W"):
                    if(self.faces[i][0][1] == "W"):
                        self.__move(moveMapper(i, "FRUR'U'F'"))
                    elif(self.faces[i][1][2] == "W"):
                        self.__move(moveMapper(i, "RUR'"))
                    elif(self.faces[i][2][1] == "W"):
                        self.__move(moveMapper(i, "F"))
                    else:
                        self.__move(moveMapper(i, "L'U'L"))
                    break
        self.__baseCross()

    def __firstLayer(self):
        return
