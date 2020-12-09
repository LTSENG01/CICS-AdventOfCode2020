data = """"....#..#.......#........#....#.
..##.#.#.#...................#.
....#.#.##..#....#......#......
... complete input"""

vals = data.split("\n")

def counter(vals,right,down):
    hor = len(vals[0])-1
    ver = len(vals)
    count = 0
    i,j = 0,0
    while(j < ver):
        if(vals[j][i] == "#"):
            count += 1
        i += right
        i %= hor
        j += down
    #for first part call counter(vals,3,1) which prints count and stops
    #print(count)

    return count

print(counter(vals,1,1)*counter(vals,3,1)*counter(vals,5,1)*counter(vals,7,1)*counter(vals,1,2))





