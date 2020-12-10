with open('10.txt', 'r') as fin:
    data = [int(line[:-1]) for line in fin]

data.sort()

joltage_differences = {
    '1': 0,
    '3': 1
}

joltage_differences[str(data[0])] += 1
for i in range(1, len(data)):
    joltage_differences[str(data[i] - data[i - 1])] += 1

print(joltage_differences['1'] * joltage_differences['3'])


def recursive_count(index):
    if index == len(data) - 1:
        return 1
    if index in cache:
        return cache[index]

    count_paths = 0
    if index + 1 < len(data) and (data[index + 1] - data[index] <= 3):
        count_paths += recursive_count(index + 1)
    if index + 2 < len(data) and (data[index + 2] - data[index] <= 3):
        count_paths += recursive_count(index + 2)
    if index + 3 < len(data) and (data[index + 3] - data[index] <= 3):
        count_paths += recursive_count(index + 3)

    cache[index] = count_paths

    return count_paths


data.insert(0, 0)
data.append(data[-1] + 3)
cache = {}
print(recursive_count(0))

