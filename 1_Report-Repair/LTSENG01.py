numbers = []

with open("1.txt", 'r') as fin:
    for num in fin:
        numbers.append(int(num))

for i in range(0, len(numbers)):
    for j in range(i, len(numbers)):
        for k in range(j, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == 2020:
                print(numbers[i] * numbers[j] * numbers[k])
