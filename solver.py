from cube import Cube
from solver_data import movedata, positionTransformData, whiteEdgePairs, whiteEdgeDirectMoves

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

    def moveMapper(self, side, form):
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

    def positionMapper(self, target, side, row, col):
        aside, arow, acol = positionTransformData[target][side][row][col]
        return self.faces[aside][arow][acol]

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
        # G O B R
        t_slot = 0
        t_score = 0
        for i in range(4):
            score = bool(self.positionMapper(i, 0, 2, 1) == "G" and self.positionMapper(i, 4, 0, 1) == "W") + bool(self.positionMapper(i, 1, 2, 1) == "O" and self.positionMapper(i, 4, 1, 2) == "W") + bool(self.positionMapper(i, 2, 2, 1) == "B" and self.positionMapper(i, 4, 2, 1) == "W") + bool(self.positionMapper(i, 3, 2, 1) == "R" and self.positionMapper(i, 4, 1, 0) == "W")
            if(score > t_score):
                t_slot = i
                t_score = score
        if(t_score == 4):
            if(t_slot == 1):
                self.__move("D'")
            elif(t_slot == 2):
                self.__move("D2")
            elif(t_slot == 3):
                self.__move("D")
            return
        #  0
        # 3 1
        #  2
        slotToColorMap = {"G": (0 + t_slot) % 4, "O": (1 + t_slot) % 4, "B": (2 + t_slot) % 4, "R": (3 + t_slot) % 4}
        slot_to_persp = [[0, 1, 2, 3], [3, 0, 1, 2], [2, 3, 0, 1], [1, 2, 3, 0]]
        target = ""
        target_other = ""
        target_persp = ""
        for persp in range(4):
            for pos in whiteEdgePairs.keys():
                aside, arow, acol = pos
                if(self.positionMapper(persp, aside, arow, acol) == "W"):
                    target = pos
                    target_other = whiteEdgePairs[pos]
                    break
            if(bool(target)):
                target_persp = persp
                break
        if(bool(target)):
            target_other_color = self.positionMapper(target_persp, target_other[0], target_other[1], target_other[2])
            g_slot = slotToColorMap[target_other_color]
            p_slot = slot_to_persp[target_persp][g_slot]
            edgeMove = whiteEdgeDirectMoves[target][p_slot]
            self.__move(self.moveMapper(target_persp, edgeMove))
        else:
            if(self.positionMapper(t_slot, 0, 2, 1) != "G"):
                self.__move(self.moveMapper(t_slot, "F2"))
            elif(self.positionMapper(t_slot, 1, 2, 1) != "O"):
                self.__move(self.moveMapper(t_slot, "R2"))
            elif(self.positionMapper(t_slot, 2, 2, 1) != "B"):
                self.__move(self.moveMapper(t_slot, "B2"))
            else:
                self.__move(self.moveMapper(t_slot, "L2"))
        self.__baseCross()

    def __firstLayer(self):
        return