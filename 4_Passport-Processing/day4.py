# Author: Walker Sorensen
# python3.8

with open('day4data.txt', 'r') as f:
	data = [line.split('\n')[0] for line in f.readlines()]
	data = '_'.join(data)
	passports = data.split('__')

fields = [
	'byr',
	'iyr',
	'eyr',
	'hgt',
	'hcl',
	'ecl',
	'pid']


valid_passports = 0
valid_data = 0

for passport in passports:
	passport_field_count = 0
	field_valid = []

	for field in fields:
		valid_field = False
		if field in passport:
			passport_field_count += 1

			if field == 'byr':
				byr = 0
				if len(passport.split('byr:')[1].split('_')[0]) == 4:
					byr = int(passport.split('byr:')[1].split('_')[0])
				else:
					byr = int(passport.split('byr:')[1].split(' ')[0])

				if byr >= 1920 and byr <= 2002:
					valid_field = True

			if field == 'iyr':
				iyr = 0
				if len(passport.split('iyr:')[1].split('_')[0]) == 4:
					iyr = int(passport.split('iyr:')[1].split('_')[0])
				else:
					iyr = int(passport.split('iyr:')[1].split(' ')[0])

				if iyr >= 2010 and iyr <= 2020:
					valid_field = True
				
			if field == 'eyr':
				eyr = 0
				if len(passport.split('eyr:')[1].split('_')[0]) == 4:
					eyr = int(passport.split('eyr:')[1].split('_')[0])
				else:
					eyr = int(passport.split('eyr:')[1].split(' ')[0])

				if eyr >= 2020 and eyr <= 2030:
					valid_field = True

			if field == 'hgt':
				hgt = 0
				if len(passport.split('hgt:')[1].split('cm')[0]) == 2 or len(passport.split('hgt:')[1].split('cm')[0]) == 3:
					hgt = passport.split('hgt:')[1].split('cm')[0]
					if len(hgt) <= 3:
						if int(hgt) >= 150 and int(hgt) <= 193:
							valid_field = True

				else:
					hgt = passport.split('hgt:')[1].split('in')[0]
					if len(hgt) <= 3:
						if int(hgt) >= 59 and int(hgt) <= 76:
							valid_field = True

			if field == 'hcl':
				print(passport)
				if len((pain := passport.split('hcl:')[1].split(' ')[0])) == 7:
					for char in pain:
						if char in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] or char in ['a', 'b', 'c', 'd', 'e', 'f', '#']:
							valid_field = True

				elif len(pain := pain.split('_')[0]) == 7:
					print(pain)
					for char in pain:
						if char in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] or char in ['a', 'b', 'c', 'd', 'e', 'f', '#']:
							valid_field = True



			if field == 'ecl':
				if passport.split('ecl:')[1][:3] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
					valid_field = True

			if field == 'pid':
				if len(pwd := passport.split('pid:')[1].split(' ')[0]) == 9:
					try:
						int(pwd)
						valid_field = True
					except ValueError:
						valid_field = False
				if len(pwd := passport.split('pid:')[1].split('_')[0]) == 9:
					try:
						int(pwd)
						valid_field = True
					except ValueError:
						valid_field = False
		print(valid_field, field)
		field_valid += [valid_field]

	if passport_field_count == len(fields):
		valid_passports += 1

	if not False in field_valid:
		valid_data += 1

print(valid_data) # Yeah, I don't know how this script works either
