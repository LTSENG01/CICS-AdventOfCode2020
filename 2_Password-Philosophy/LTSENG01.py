import re

# first problem
with open('2.txt', 'r') as fin:
    count = 0

    for line in fin:
        parts = line.split(" ")
        num_range = parts[0].split("-")
        # ^([^r]*r){3,5}[^r]*$ where r is the character
        regex = f'^([^{parts[1][0]}]*{parts[1][0]}){{{num_range[0]},{num_range[1]}}}[^{parts[1][0]}]*$'
        result = re.search(regex, parts[2])
        if result is not None:
            count += 1

    print(count)

# second problem
with open('2.txt', 'r') as fin:
    count = 0

    for line in fin:
        parts = line.split(" ")
        num_range = parts[0].split("-")
        if (parts[2][int(num_range[0]) - 1] == parts[1][0]) ^ (parts[2][int(num_range[1]) - 1] == parts[1][0]):
            count += 1

    print(count)
