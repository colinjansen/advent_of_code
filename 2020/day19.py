import re

def parse():
    codes = []
    rules = {}
    with open('_input/day19.txt') as fp:
        for line in fp.readlines():
            if ':' not in line:
                codes.append(line.strip())
            else:
                parts = line.split(':')
                rules[parts[0]] = parts[1].strip()
    return (codes, rules)

def get_chunk_size(regex, codes):
    for code in codes:
        match = regex.match(code)
        if match:
            return match.end()
    return -1

def get_pattern(rules, n):
    def expand(rule):
        if rule.startswith('"'):
            return rule.strip('"')
        return f"({''.join(['|' if p == '|' else expand(rules[p]) for p in rule.split()])})"
    return re.compile(expand(rules[str(n)]))

def part1():
    codes, rules = parse()
    rx = get_pattern(rules, 0)
    return sum([1 for c in codes if rx.fullmatch(c)])

def part2():
    codes, rules = parse()
    rules['8'] = '42 | 42 8'
    rules['11'] = '42 31 | 42 11 31'
    
    rx42 = get_pattern(rules, 42)
    rx31 = get_pattern(rules, 31)
    chunk_size = get_chunk_size(rx42, codes)
    count = 0
    for code in codes:
        if len(code) % chunk_size != 0 or len(code) < chunk_size * 3:
            continue
        num42 = 0
        num31 = 0
        chunks = [code[i:i+chunk_size] for i in range(0, len(code), chunk_size)]
        i = 0
        j = len(chunks) - 1
        while i < len(chunks) and rx42.match(chunks[i]):
            i += 1
            num42 += 1
        while j >= 0 and rx31.match(chunks[j]):
            j -= 1
            num31 += 1
        if num42 < 2 or num31 < 1 or num42 <= num31 or num42 + num31 != len(chunks): 
            continue
        count += 1
    return count

print('part 1: ', part1())
print('part 2: ', part2())