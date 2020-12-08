with open('8.txt', 'r') as fin:
    data = [line[:-1].split(" ") for line in fin]


def execute_instruction(line, acc):
    operator = data[line][0]
    operand = int(data[line][1])

    if operator == 'acc':
        acc += operand
    elif operator == 'jmp':
        return line + operand, acc

    return line + 1, acc


def routine():
    acc = 0
    visited_lines = []
    next_line = 0
    while True:
        if next_line == len(data):
            print("Finished.")
            return 1, acc
        if visited_lines.__contains__(next_line):
            # print("Already visited: " + str(next_line + 1))
            return -1, visited_lines
        visited_lines.append(next_line)
        (next_line, acc) = execute_instruction(next_line, acc)


status, visited = routine()
while len(visited) > 0:
    current_operator = data[visited[-1]][0]

    if current_operator == "acc":
        # go back another instruction
        visited = visited[:-1]
        continue

    # invert the instruction before the loop instruction
    data[visited[-1]][0] = "nop" if current_operator == "jmp" else "jmp"

    # run the routine
    status, accumulator = routine()

    # reset the instruction if it failed
    if status == -1:
        data[visited[-1]][0] = current_operator
        # go back another instruction
        visited = visited[:-1]
    else:
        # it succeeded
        print(accumulator)
        break
