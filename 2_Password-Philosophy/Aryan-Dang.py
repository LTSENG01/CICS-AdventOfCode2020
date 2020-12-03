def number(string):
    number = 0
    for x in string:
        if x.isdigit():
            number *= 10
            number += int(x)
    return number

data = """2-7 p: pbhhzpmppb
3-6 h: jkhnhwhx
5-6 x: xxxxxmxf
.... complete input"""

lists = data.split("\n")
count = 0
f,s = 0,0
temp = str()
vals = list()
for line in lists:
    vals = line.split(" ")
    f = number(vals[0][:2])
    if(f/10 == 0):
        s = number(vals[0][1:])
    else:
        s = number(vals[0][2:])
        
    temp = vals[1].rstrip(":")
    if((vals[2][f-1] == temp and vals[2][s-1] != temp) or (vals[2][f-1] != temp and vals[2][s-1] == temp)):
        count += 1
        
    '''
    part1 :
    if(vals[2].count(temp) >= f and vals[2].count(temp) <= s):
        count += 1
    '''
print(count)
