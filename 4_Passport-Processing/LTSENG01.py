import re

with open('4.txt', 'r') as fin:
    passports = ''.join([line for line in fin])
    passports = passports.split("\n\n")
    for i in range(0, len(passports)):
        passports[i] = passports[i].replace('\n', ' ')


def passport_checker(passport):
    tokenized_passport = passport.split(" ")
    tokens = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for token in tokens:
        if token not in passport:
            return 0
    for token in tokenized_passport:
        if token[0:3] == "byr":
            if int(token[4:]) < 1920 or int(token[4:]) > 2002:
                return 0
        if token[0:3] == "iyr":
            if int(token[4:]) < 2010 or int(token[4:]) > 2020:
                return 0
        if token[0:3] == "eyr":
            if int(token[4:]) < 2020 or int(token[4:]) > 2030:
                return 0
        if token[0:3] == "hgt":
            if not re.match(r"([0-9]{2}in|[0-9]{3}cm)", token[4:]):
                return 0
            if token[7:] == "cm":
                if int(token[4:7]) < 150 or int(token[4:7]) > 193:
                    return 0
            if token[6:] == "in":
                if int(token[4:6]) < 59 or int(token[4:6]) > 76:
                    return 0
        if token[0:3] == "hcl":
            if not re.match(r"^#([a-f0-9]){6}$", token[4:]):
                return 0
        if token[0:3] == "ecl":
            if not re.match(r"^(amb|blu|brn|gry|grn|hzl|oth)$", token[4:]):
                return 0
        if token[0:3] == "pid":
            if not re.match(r"^([0-9]){9}$", token[4:]):
                return 0
    return 1


valid_count = 0
for p in passports:
    valid_count += passport_checker(p)

print(valid_count)
