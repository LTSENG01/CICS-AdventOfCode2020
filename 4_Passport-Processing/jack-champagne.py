file = open('4.txt')

import re

fchars = file.read()

lines = []
for elem in fchars.split('\n\n'):
    lines.append(elem.replace('\n', ' ') + ' ')

#lines.remove()


ans = 0
patt = re.compile(r'([a-z]{3}):((?:#?\d?\w?){1,})\s')
pid_patt = re.compile(r'([0-9]{9})\s')
for line in lines:
    if 'byr' in line and 'iyr' in line and 'eyr' in line and 'hgt' in line and 'hcl' in line and 'ecl' in line and 'pid' in line:
        matches = patt.findall(line)
        stillValid = True
        for tup in matches:
            tag = tup[0]
            data = tup[1]
            if not stillValid:
                break
            if tag == 'byr':
                stillValid = stillValid and (len(data) == 4)
                stillValid = stillValid and (1920 <= int(data) <= 2002)
            elif tag == 'iyr':
                stillValid = stillValid and (len(data) == 4)
                stillValid = stillValid and (2010 <= int(data) <= 2020)
            elif tag == 'eyr':
                stillValid = stillValid and (len(data) == 4)
                stillValid = stillValid and (2020 <= int(data) <= 2030)
            elif tag == 'hgt':
                if 'in' in data:
                    stillValid = stillValid and (59 <= int(str(data).strip('in')) <= 76)
                elif 'cm' in data:
                    stillValid = stillValid and (150 <= int(str(data).strip('cm')) <= 193)
                else:
                    stillValid = stillValid and False

            elif tag == 'hcl':
                stillValid = stillValid and (data[0] == '#')
                stillValid = stillValid and (0 <=  int('0x' + data[1:], 16) <= 16777215)
            elif tag == 'ecl':
                stillValid = stillValid and (data in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] )
            elif tag == 'pid':
                data = data + ' '
                stillValid = stillValid and (pid_patt.match(data) is not None)
            elif tag == 'cid':
                continue
            else:
                print(tag + ' is invalid tag')
        if stillValid:
            ans += 1




print(ans)