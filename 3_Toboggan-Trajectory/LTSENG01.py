chars_per_row = 31  # bounds [0, 30]

with open('3.txt', 'r') as fin:
    tree_map = [line[:-1] for line in fin]


def slope_checker(run, rise):
    row = 0
    column = 0
    tree_count = 0

    while row < len(tree_map):
        # check if there's a tree
        if tree_map[row][column] == '#':
            tree_count += 1
        column = (column + run) % chars_per_row
        row += rise

    return tree_count


slope_1_1 = slope_checker(1, 1)
slope_3_1 = slope_checker(3, 1)
slope_5_1 = slope_checker(5, 1)
slope_7_1 = slope_checker(7, 1)
slope_1_2 = slope_checker(1, 2)

print(slope_1_1 * slope_3_1 * slope_5_1 * slope_7_1 * slope_1_2)
