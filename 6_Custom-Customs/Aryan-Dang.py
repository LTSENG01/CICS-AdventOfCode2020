data = '''xav
uavx
xavsi
yavx

efokjptizdcwmqnuh
qgfdvurtnjwpichxk
taqkcunfzpmydiwjsh

... complete input'''

vals = data.split("\n\n")

temp = list()
count = 0
tempVal = list()
flag = True

for val in vals:
    temp = list()
    for x in val:
        '''
        part1
        if x not in temp and x != "\n":
            temp.append(x)
    count += len(temp)
    '''
        #part2:
        if x not in temp and x != "\n":
            temp.append(x)
            
    tempVal = val.split("\n")
    for t in temp:
        for Val in tempVal:
            if t not in Val:
                flag = False
        if(flag):
            count += 1
        flag = True
print(count)
