file = open('5.txt')

fchars = file.read()

lines = []
for elem in fchars.split('\n'):
    lines.append(elem)

lines.remove('')

def getRow(line):
    min = 0
    max = 127

    for char in line[0:7]:
        mid = min + int((max - min) / 2)
        if char == 'F':
            min = min
            max = mid
        elif char == 'B':
            min = mid + 1
            max = max
    return min

def getCol(line):
    min = 0
    max = 7

    for char in line[7:]:
        mid = min + int((max - min) / 2)
        if char == 'L':
            min = min
            max = mid
        elif char == 'R':
            min = mid + 1
            max = max
    return min

r1 = getRow('FBFBBFFRLR')
c1 = getCol('FBFBBFFRLR')

max = 0
points = [[0 for i in range(8)] for j in range(128)] 
for line in lines:
    row = getRow(line)   
    col = getCol(line)
    
    try:
        rowList = points[row]
        rowList[col] = 1
    except IndexError as identifier:
        print(str(row) + ':' + str(col))

    id = row * 8 + col
    if id > max:
        max = id
    
prevElem = 0
curElem = 0
nextElem = 0
for i in range(128):
    for j in range(8):
        prevElem = curElem
        curElem = nextElem
        nextElem = points[i][j]

        if (prevElem == 1 and curElem == 0 and nextElem == 1):
            print(i*8 + j - 1)

print(max)
def printPl(points):
    for i in range(0, 128):
        print(points[i])