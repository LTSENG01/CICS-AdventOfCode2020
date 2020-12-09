with open('9.txt', 'r') as fin:
    data = [int(line[:-1]) for line in fin]


def potential_sums(reference):
    sums = set()
    for i in reference:
        for j in reference:
            sums.add(i + j)
    return sums


invalid_number = -1
for upper_range in range(25, len(data)):
    sliding_window = data[upper_range-25:upper_range]
    next_sum = data[upper_range]

    if next_sum not in potential_sums(sliding_window):
        invalid_number = next_sum
        print(invalid_number)
        break

# find the entries that add up to invalid_number
for value in range(25, len(data)):
    sliding_window = [data[value]]
    for next_elem in range(value + 1, len(data)):
        sliding_window.append(data[next_elem])
        if sum(sliding_window) == invalid_number:
            print(min(sliding_window) + max(sliding_window))
        elif sum(sliding_window) > invalid_number:
            break
