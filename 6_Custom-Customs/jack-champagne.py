file = open('6.txt')

fchars = file.read()

groups = []
for elem in fchars.split('\n\n'):
    groups.append(elem)

counter = 0
for group in groups:
    yes = []
    for person in group.split('\n'):
        if person is not None or person != '':
            for question in person:
                if question not in yes:
                    yes.append(question)
    counter += len(yes)

print(counter)

counter2 = 0
for group in groups:
    allyes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for person in group.split('\n'):
        if person is not None or person != '':
            curyes = []
            for question in person:
                curyes.append(question)
            newallyes = []
            for char in curyes:
                if char in allyes:
                    newallyes.append(char)
                else:
                    continue
            allyes = newallyes;

    counter2 += len(allyes)
                
print(counter2)