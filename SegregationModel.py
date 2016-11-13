import random

def rs():
    """ rs chooses a random step and returns it
        note that a call to rs() requires parentheses
        inputs: none at all!
    """
    return random.choice([0,1])

def createOneRow(width):
    """ returns one row of zeros of width "width"...
         You should use this in your
         createBoard(width, height) function """
    row = []
    for col in range(width):
        row += [0]
    return row

#print createOneRow(10)


def createBoard(width, height):
    """
    returns "height" rows of zeros of width "width"...
    """
    I = []
    for i in range(height):
        I += [createOneRow(width)]
    return I


def printBoard(I):
    for row in I:
        line = ''
        for col in row:
            line += str(col)
        print line

I = createBoard(5,5)
#printBoard(I)

def unsegregatedBoard(width,height,percentX,percent0):
    numberX = int(width*height*percentX)
    numberY = int(width*height*percent0)
    numberO = width*height-numberY-numberX
    population = numberO*'0' + numberX*'X' + numberY*'Y'
    population = random.sample(population, width*height)
    oiii=0
    Z = createBoard(width,height)
    for r in range(width):
        for c in range(height):
            Z[r][c] = population[oiii]
            oiii = oiii + 1
            if r == 0:
                Z[r][c] = "*"
            elif r == height-1:
                Z[r][c] = "*"
            elif c == 0:
                Z[r][c] = ">"
            elif c == width-1:
                Z[r][c] = "<"


    return Z


#Z = unsegregatedBoard(10,10,0.30,.25)
#printBoard(Z)

def SimilarNeighborsPercent(row,col,A):
    alikeNeighborCount = -1
    totalNeighborCount = -1

   # number of alike neighbors/number of unalike neighbors+number of alike neighbors
    for r in range(row-1, row+2):
        for c in range(col-1,col+2):
            if A[row][col] == '0':
                return 'base is 0'
            else:
                if A[r][c]!='0':
                    totalNeighborCount += 1
                if A[r][c] == A[row][col]:
                    alikeNeighborCount += 1
    return float(alikeNeighborCount)/totalNeighborCount


#Z = unsegregatedBoard(5,5,0.30,.25)
#printBoard(Z)
#print SimilarNeighborsPercent(1,1,Z)

def emptySpaces(A):
    L = []
    h = len(A)
    w = len(A[0])
    for row in range(h):
        for col in range(w):
            if A[row][col] == '0':
               L.append([row,col])
            else:
                pass
    return L

#Z = unsegregatedBoard(5,5,0.30,.25)
#printBoard(Z)
#print emptySpaces(Z)

def copy(A):
    height = len(A)
    width = len(A[0])
    newA = createBoard(width,height)
    for row in range(height):
        for col in range(width):
            newA[row][col]= A[row][col]
    return newA

def nextGeneration(A,thresh):
    height = len(A)
    width = len(A[0])
    newA = copy(A)
    emptyList = random.sample(emptySpaces(A), len(emptySpaces(A)))
    print emptyList
    i=0
    for row in range(1,height-1):
        for col in range(1,width-1):
            if SimilarNeighborsPercent(row,col,A)< thresh and i<len(emptyList):
                newA[row][col] = 0
                newA[emptyList[i][0]][emptyList[i][1]] = A[row][col]
                i+=1
    return newA

#Take boarder out of neighbor count

A = unsegregatedBoard(11,11,.4,.4)
printBoard(A)
A = nextGeneration(A,.5)
printBoard(A)

