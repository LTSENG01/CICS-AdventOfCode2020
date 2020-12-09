with open('6.txt', 'r') as fin:
    data = ''.join(fin.readlines())[:-1].split("\n\n")

total = 0
for group in data:
    people = set(group.replace("\n", ""))
    total += len(people)

print(total)

total = 0
for group in data:
    num_people = group.count("\n") + 1
    people = list(group.replace("\n", ""))
    common_questions = set()
    for question in people:
        if people.count(question) == num_people:
            common_questions.add(question)
    total += len(common_questions)

print(total)

