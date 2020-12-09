with open('day6.txt', 'r') as f:
	data = list(map(lambda x : x.split('\n')[0], f.readlines()))

group_answers = ' '.join(data).split('  ')

# group_answers = [''.join(answer.split(' ')) for answer in group_answers]

# count = 0
# for answer in group_answers:
# 	question = [] # {char : True/False}
# 	for char in answer:
# 		if char not in question:
# 			question += [char]
# 	count += len(question)
# print(count)

count = 0
for answer in group_answers:
	question = {} # {char : True/False}
	for ind_answer in answer.split(' '):
		for char in ind_answer:
			if char in question:
				question[char] += 1
			else:
				question[char] = 1
	for char in question:
		if question[char] == len(answer.split(' ')):
			count += 1
print(count)