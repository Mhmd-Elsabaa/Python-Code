import random
Queens = 0


def Try(Arr):
    global Queens
    # check if the 8 Queens settled peacefully
    if Queens == 8:
        return True
    # check for Available locations to put Queen
    for i in range(0, 8, 1):
        for j in range(0, 8, 1):
            if Arr[i][j] == 0:
                putQueen(Arr, i, j)
                if Try(Arr):
                    return True
                # if Not Possible, Remove Last Queen
                removeQueen(Arr, i, j)
    # if No Available Locations Exist
    return False


def putQueen(Arr, x, y):
    global Queens
    # Horizontal Adding
    for i in range(0, 8, 1):
        Arr[i][y] += 1
    # Vertical Adding
    for i in range(0, 8, 1):
        Arr[x][i] += 1
    # Diagonal Adding
    i = x-1
    j = y-1
    while i >= 0 and j >= 0:
        Arr[i][j] += 1
        i -= 1
        j -= 1
    i = x + 1
    j = y + 1
    while i < 8 and j < 8:
        Arr[i][j] += 1
        i += 1
        j += 1
    i = x + 1
    j = y - 1
    while i < 8 and j >= 0:
        Arr[i][j] += 1
        i += 1
        j -= 1
    i = x - 1
    j = y + 1
    while i >= 0 and j < 8:
        Arr[i][j] += 1
        i -= 1
        j += 1
    # Marking the Queen Location
    Arr[x][y] += 50
    Queens += 1


def removeQueen(Arr, x, y):
    global Queens
    for i in range(0, 8, 1):
        Arr[i][y] -= 1
    for i in range(0, 8, 1):
        Arr[x][i] -= 1
    i = x-1
    j = y-1
    while i >= 0 and j >= 0:
        Arr[i][j] -= 1
        i -= 1
        j -= 1
    i = x + 1
    j = y + 1
    while i < 8 and j < 8:
        Arr[i][j] -= 1
        i += 1
        j += 1
    i = x + 1
    j = y - 1
    while i < 8 and j >= 0:
        Arr[i][j] -= 1
        i += 1
        j -= 1
    i = x - 1
    j = y + 1
    while i >= 0 and j < 8:
        Arr[i][j] -= 1
        i -= 1
        j += 1
    Arr[x][y] -= 50
    Queens -= 1


def createChess():
    # Initialize 8*8 Array with 0s
    temp = []
    for i in range(0, 8, 1):
        temp.append([])
        for j in range(0, 8, 1):
            temp[i].append(0)
    # Randomly Put First Queen
    x = random.randint(0, 7)
    y = random.randint(0, 7)
    putQueen(temp, x, y)
    print(" First Queen in row: "+str(8-x)+", col: "+str(y+1))
    return temp


def printChess(Arr):
    temp = ""
    for j in range(0, 8, 1):
        temp += "____"
    temp += "\n"
    for i in range(0, 8, 1):
        for j in range(0, 8, 1):
            temp += "|   "
        temp += "|\n"
        for j in range(0, 8, 1):
            if Arr[i][j] > 30:
                temp += "| Q "
            else:
                temp += "|   "
        temp += "| " + str(8-i) + "\n"
        for j in range(0, 8, 1):
            temp += "|___"
        temp += "|\n"
    print (temp)
    print("  A   B   C   D   E   F   G   H ")

# Main Function..
Array = createChess()
Try(Array)
printChess(Array)