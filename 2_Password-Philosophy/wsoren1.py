# Author: Walker Sorensen
# Python 3.8

with open('day2data.txt', 'r') as f:
	rules_and_pwds = [line.split('\n')[0] for line in f.readlines()]
	rules = [combo.split(':')[0] for combo in rules_and_pwds]
	pwds = [combo.split(':')[1][1:] for combo in rules_and_pwds]
	bounds = [rule.split(' ')[0] for rule in rules]
	chars = [rule.split(' ')[1] for rule in rules]
	bounds = [(int(bound.split('-')[0]), int(bound.split('-')[1])) for bound in bounds]

# now we have three useful datatypes:
# bounds: (lower: int, upper: int)[]
# chars: Char[]
# pwds: String[]

def valid_pwd_a(char, bound, password):  # Rules are: character must occur between those bounds
    counter = 0

    for c in password:
        if c == char:
            counter += 1
    
    return counter >= bound[0] and counter <= bound[1]


def valid_pwd_b(char, bound, password):  # Rules are: character must occur in either position lower_bound, or upper bound, not both or neither
    flags = 0

    if password[bound[0] - 1] == char:
        flags += 1
    if password[bound[1] - 1] == char:
        flags += 1

    return flags == 1


count_a, count_b = 0, 0

for i in range(len(rules)):
    if valid_pwd_a(chars[i], bounds[i], pwds[i]):
        count_a += 1
    if valid_pwd_b(chars[i], bounds[i], pwds[i]):
        count_b += 1

print(f'Valid pwds: pt 1: {count_a} \t pt 2: {count_b}')
