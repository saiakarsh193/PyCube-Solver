import random

def getScramble(length):
    vMoves = ['U', 'D', 'R', 'L', 'F', 'B'] # 'Uw', 'Dw', 'Rw', 'Lw', 'Fw', 'Bw', 'E', 'M', 'S', 'x', 'y', 'z']
    scr = ""
    for _ in range(length):
        scr += vMoves[int(random.random() * len(vMoves))]
        if(random.random() > 0.7):
            scr += '\''
    return condenseFormula(scr)

def condenseFormula(form, advanced=True):
    if(not isValid(form)):
        return "ERROR"
    if(not advanced):
        return rawCondense(form)
    ans = ""
    tmp = ""
    for ch in form:
        if(ch == '(' or ch == ')'):
            if(len(tmp) > 0):
                ans += rawCondense(tmp)
            tmp = ""
            ans += ch
        else:
            tmp += ch
    if(len(tmp) > 0):
        ans += rawCondense(tmp)
    maxlevel = getMaxLevel(ans)
    for level in range(maxlevel, 0, -1):
        ans = parCondense(ans, level)
    return ans

def isValid(form):
    level = 0
    valid = True
    validAlpha = ['U', 'D', 'R', 'L', 'F', 'B', 'E', 'M', 'S', 'x', 'y', 'z', 'u', 'd', 'r', 'l', 'f', 'b']
    boolAlpha = False
    boolPrime = False
    boolDec = False
    for ch in form:
        if(ch == '('):
            level += 1
            boolAlpha = False
            boolPrime = False
            boolDec = False
        elif(ch == ')'):
            if(level > 0):
                level -= 1
            else:
                valid = False
            boolAlpha = True
            boolPrime = False
            boolDec = False
        else:
            if(ch in validAlpha):
                boolAlpha = True
                boolPrime = False
                boolDec = False
            elif((ch == '\'' or ch == 'P') and boolAlpha and not boolPrime and not boolDec):
                if(boolDec):
                    boolAlpha = False
                    boolDec = False
                else:
                    boolPrime = True
            elif(ch.isdigit() and boolAlpha):
                boolDec = True
            else:
                valid = False
    if(level != 0):
        valid = False
    return valid

def getMaxLevel(form):
    level = 0
    maxlevel = 0
    for ch in form:
        if(ch == '('):
            level += 1
            if(level > maxlevel):
                maxlevel = level
        elif(ch == ')'):
            level -= 1
    return maxlevel

def parCondense(form, tar):
    form += '@'
    ans = ""
    temp = ""
    ref = ""
    refctr = 0
    ctr = 0
    for ch in form:
        if(ch == '('):
            ctr += 1
        if(ctr >= tar):
            temp += ch
        else:
            if(len(ref) > 0):
                ans += ref
                ans += str(refctr) if refctr > 1 else ""
                ref = ""
                refctr = 0
            ans += ch
        if(ch == ')'):
            if(ctr == tar):
                if(temp == ref):
                    refctr += 1
                else:
                    ans += ref
                    ans += str(refctr) if refctr > 1 else ""
                    ref = temp
                    refctr = 1
                temp = ""
            ctr -= 1
    return ans[:-1]

def rawCondense(form):
    if(form.isdigit()):
        return form
    # string to 2d count array
    temp = []
    for i, item in enumerate(form):
        if(form[i].isalpha() and not form[i] == 'P'):
            temp.append([form[i], ""])
        else:
            if(form[i].isdigit()):
                temp[-1][1] += form[i]
            else:
                temp[-1][0] += '\''
    # int() of count
    for i, item in enumerate(temp):
        if(temp[i][1] == ""):
            temp[i][1] = 1
        else:
            temp[i][1] = int(temp[i][1])
    # removing anti moves and combining same moves
    while True:
        isChange = False
        for i in range(len(temp) - 1):
            if(isPrimePair(temp[i][0], temp[i + 1][0])):
                minv = min(temp[i][1], temp[i + 1][1])
                temp[i][1] -= minv
                temp[i + 1][1] -= minv
                if(temp[i + 1][1] == 0):
                    temp.pop(i + 1)
                if(temp[i][1] == 0):
                    temp.pop(i)
                isChange = True
                break
            elif(temp[i][0] == temp[i + 1][0]):
                temp[i][1] += temp[i + 1][1]
                temp.pop(i + 1)
                isChange = True
                break
        if(not isChange):
            break
    # limit count to 2 and inverse moves for 3
    for i, item in enumerate(temp):
        temp[i][1] = ((temp[i][1] - 1) % 4) + 1
        if(temp[i][1] == 3):
            if(len(temp[i][0]) == 2):
                temp[i][0] = temp[i][0][0]
            else:
                temp[i][0] += '\''
            temp[i][1] = 1
        elif(temp[i][1] == 4):
            temp[i][1] = 0
    # 2d count array to string
    cform = ""
    for i, item in enumerate(temp):
        if(temp[i][1] > 0):
            cform += temp[i][0]
            if(temp[i][1] == 2):
                cform += '2'
    return cform

def isPrimePair(s1, s2):
    return bool(len(s1) != len(s2) and s1[0] == s2[0])

def parseFormula(form, condense = True):
    if(not isValid(form)):
        return []
    if(condense):
        form = condenseFormula(form)
    moves = [ch for ch in form]
    vwMoves = ['U', 'D', 'R', 'L', 'F', 'B']
    # Convert w moves to base moves
    for i, item in enumerate(moves):
        if(moves[i] == 'w'):
            moves.pop(i)
            if(i > 0 and moves[i - 1] in vwMoves):
                moves[i - 1] = moves[i - 1].lower()
    # Convert outprimes to base moves
    vMoves = ['U', 'D', 'R', 'L', 'F', 'B', 'E', 'M', 'S', 'x', 'y', 'z', 'u', 'd', 'r', 'l', 'f', 'b']
    cvm = -1
    for i, item in enumerate(moves):
        if(moves[i] in vMoves):
            cvm = i
        if(moves[i] == '\'' or moves[i] == 'P'):
            moves.pop(i)
            if(cvm >= 0):
                moves.insert(cvm + 1, "P")
                cvm = -1
    # Converting the characters into move blocks
    ans = []
    for i, item in enumerate(moves):
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
