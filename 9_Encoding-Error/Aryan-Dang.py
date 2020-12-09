data = '''12
6
33
..complete input'''

def _25(index):
    count = 0
    last25 = list()
    if(index >= 25):
        count = index - 25
        while(count < index and index < len(vals)):
            last25.append(vals[count])
            count += 1
    #this part not entered per this day's requirements
    else :
        while(count < index):
            last25.append(vals[count])
            count += 1
    return last25

def checkSum(ans,last):
    for item in last:
        if ans - item in last:
            return True
    return False

global vals
vals = data.split("\n")

for i in range(len(vals)):
    vals[i] = int(vals[i])

#part1
for i in range(25,len(vals),1):
    last25 = _25(i)
    if(checkSum(vals[i],last25) == False):
        print(vals[i])

#part2
total = 0
resultList = list()
for i in range(len(vals)-1):
    resultList.append(vals[i])
    total += vals[i]
    for j in range(i+1,len(vals)-1):
        resultList.append(vals[j])
        total += vals[j]
        if(total == 258585477):
            print(min(resultList)+max(resultList))
            break;
    total = 0
    resultList = list()


