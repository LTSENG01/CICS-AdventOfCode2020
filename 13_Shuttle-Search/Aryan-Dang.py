data = '''1011416
41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,911,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,23,x,x,x,x,x,29,x,827,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19'''
vals = data.split("\n")

start = int(vals[0])
val = list()
nos = vals[1].split(",")

for no in nos:
    if no != 'x':
        val.append(int(no))
        
ans = 1
c = True

while c:
    for no in val:
        if start % no == 0:
            c = False
            ans = no
    start += 1
print((start-1-1011416)*ans)
