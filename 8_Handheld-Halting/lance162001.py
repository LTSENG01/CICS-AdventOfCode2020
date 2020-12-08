with open("input.txt","r") as f:
    data=f.read()
data=data.split('\n')

def test(data,index,accumulator):
    seen=[]
    while True: 
        if index == len(data):
            return accumulator
        line=data[index]
        if index in seen:
            break
        seen.append(index)
        s = line.split(" ")
        if s[1] == "+":
            s[1] = s[1][:0]
        if s[0] == "acc":
            accumulator+=int(s[1])
        elif s[0] == "jmp":
            index+=int(s[1])
            continue
        index+=1
    return [seen,accumulator]
        
def run(index,data,accumulator):
    output = test(data,index,accumulator)
    origOutput=output
    lastIn=-1
    while isinstance(output, list):
        while data[lastIn].split(" ")[0] != "jmp" and data[lastIn].split(" ")[0] != "nop":
            lastIn-=1
        dat = data[lastIn]
        if dat.split(" ")[0] == "jmp":
            data[lastIn]="nop "+dat.split(" ")[1]
        else:
            data[lastIn]="jmp "+dat.split(" ")[1]
        
        output = test(data,0,0)
        if isinstance(output, list):
            data[lastIn]=dat
            lastIn-=1
    return output

print("@@@",run(0,data,0))
