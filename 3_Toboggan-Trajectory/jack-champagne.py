file = open('3.txt')

lines = file.read()

line = []
for elem in lines.split('\n'):
    line.append(elem.strip('\n'))


line.remove('')

xpos = 0
ypos = 0

tcount = 0

final = 1

def trees(lines, dx, dy):
    tcount = 0
    xpos = 0
    ypos = 0
    for level in line:
        if (ypos % dy == 0):
            if (level[xpos % 31] == '#'):
                tcount += 1
            xpos += dx
        ypos += 1
    return tcount

print(trees(line, 3, 1))
print(trees(line, 3, 1) * trees(line, 1, 1) * trees(line, 5, 1) * trees(line, 7, 1) * trees(line, 1, 2))