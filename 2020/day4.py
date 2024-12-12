import re

def parse_input():
    passports = []
    with open('day4.txt', 'r') as file:
        data = []
        for line in file.readlines():
            if line == '\n':
                p = []
                for d in data:
                    p.extend(d.split())
                d = {}
                for kv in p:
                    k, v = kv.split(':')
                    d[k] = v
                passports.append(d)
                data = []
            else:
                data.append(line.strip())
    return passports

def is_valid(p):
    for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        if field not in p:
            return False

    if not 1920 <= int(p['byr']) <= 2002:
        return False

    if not 2010 <= int(p['iyr']) <= 2020:
        return False

    if not 2020 <= int(p['eyr']) <= 2030:
        return False

    if re.match('\\d*(cm|in)', p['hgt']) is None:
        return False
    if 'cm' in p['hgt'] and not 150 <= int(p['hgt'][:-2]) <= 193:
        return False
    if 'in' in p['hgt'] and not 59 <= int(p['hgt'][:-2]) <= 76:
        return False

    if re.match('^#[0-9a-f]{6}$', p['hcl']) is None:
        return False

    if re.match('^(amb|blu|brn|gry|grn|hzl|oth)$', p['ecl']) is None:
        return False

    if re.match('^[0-9]{9}$', p['pid']) is None:
        return False

    return True

def is_valid_2(p):
    if not is_valid(p):
        return False

    return True

C = 0
for p in parse_input():
    if is_valid_2(p):
        C += 1
print(C)