data = """1711
1924
1384
1590
1876
.... rest of input
"""
vals = data.split("\n")

for i in range(len(vals)):
    vals[i] = int(vals[i])
'''
for part 1

for i in vals:
    if(2020-i) in vals:
        print(i*(2020-i))
'''
for j in vals:
    for i in vals:
        if(2020 - i-j) in vals:
            print(i*j*(2020-i-j))
