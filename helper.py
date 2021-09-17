import random

def getScramble(length):
    vMoves = ['U', 'D', 'R', 'L', 'F', 'B'] # 'Uw', 'Dw', 'Rw', 'Lw', 'Fw', 'Bw', 'E', 'M', 'S', 'x', 'y', 'z']
    scr = ""
    for _ in range(length):
        scr += vMoves[int(random.random() * len(vMoves))]
        if(random.random() > 0.7):
            scr += '\''
    return condenseFormula(scr)

def condenseFormula(form):
    # string to array
    temp = []
    for i in range(len(form)):
        if((form[i] >= 'a' and form[i] <= 'z') or (form[i] >= 'A' and form[i] <= 'Z')):
            temp.append(form[i])
        else:
            temp[-1] += form[i]
    # array to 2d count array
    val = []
    for i in range(len(temp)):
        if(len(val) > 0 and val[-1][0] == temp[i]):
            val[-1][1] += 1
        else:
            val.append([temp[i], 1])
    # limit count to 2 and inverse moves for 3
    for i in range(len(val)):
        val[i][1] = ((val[i][1] - 1) % 4) + 1
        if(val[i][1] == 3):
            val[i][0] = val[i][0][0] if (len(val[i][0]) == 2) else val[i][0] + '\''
            val[i][1] = 1
        elif(val[i][1] == 4):
            val[i][1] = 0
    # removing negating moves
    for i in range(len(val) - 1):
        if(len(val[i][0]) != len(val[i + 1][0]) and val[i][0][0] == val[i + 1][0][0]):
            minv = min(val[i][1], val[i + 1][1])
            val[i][1] -= minv
            val[i + 1][1] -= minv
    # 2d count array to string
    cform = ""
    for i in range(len(val)):
        if(val[i][1] > 0):
            cform += val[i][0]
            if(val[i][1] == 2):
                cform += '2'
    return cform

def parseFormula(form, condense = True):
    if(condense):
        form = condenseFormula(form)
    moves = [ch for ch in form]
    vwMoves = ['U', 'D', 'R', 'L', 'F', 'B']
    # Convert w moves to base moves
    for i in range(len(moves)):
        if(moves[i] == 'w'):
            moves.pop(i)
            if(i > 0 and moves[i - 1] in vwMoves):
                moves[i - 1] = moves[i - 1].lower()
    # Convert outprimes to base moves
    vMoves = ['U', 'D', 'R', 'L', 'F', 'B', 'E', 'M', 'S', 'x', 'y', 'z', 'u', 'd', 'r', 'l', 'f', 'b']
    cvm = -1
    for i in range(len(moves)):
        if(moves[i] in vMoves):
            cvm = i
        if(moves[i] == '\'' or moves[i] == 'P'):
            moves.pop(i)
            if(cvm >= 0):
                moves.insert(cvm + 1, "P")
                cvm = -1
    # Converting the characters into move blocks
    ans = []
    for i in range(len(moves)):
        if(moves[i] in vMoves):
            cm = moves[i]
            ctr = 1
            if(i + 1 < len(moves) and moves[i + 1] == 'P'):
                cm += 'P'
                ctr = 2
            cnt = 1
            if(i + ctr < len(moves) and moves[i + ctr] >= '0' and moves[i + ctr] <= '9'):
                cnt = int(moves[i + ctr])
            for _ in range(cnt):
                ans.append(cm)
    return ans
