def divisors(n):
    return [1] + [i for i in range(2, n) if n % i == 0]

def find_invalid_ids_part_1(start, end):
    invalid_ids = []
    for id in range(start, end + 1):
        sid = str(id)
        if len(sid) % 2 != 0:
            continue
        half1 = sid[:len(sid)//2]
        half2 = sid[len(sid)//2:]
        if half1 == half2:
            invalid_ids.append(id)
    return invalid_ids

def find_invalid_ids_part_2(start, end):
    invalid_ids = set()
    for id in range(start, end + 1):
        sid = str(id)
        for div in divisors(len(sid)):
            chunks = [sid[i:i+div] for i in range(0, len(sid), div)]
            if len(chunks) > 1 and all(chunk == chunks[0] for chunk in chunks):
                invalid_ids.add(id)
    return invalid_ids

part_1 = 0
part_2 = 0
with open('_input/day2.txt') as f:
    for code in f.readline().strip().split(','):
        if not code:
            continue
        parts = code.strip().split('-')
        part_1 += sum(find_invalid_ids_part_1(int(parts[0]), int(parts[1])))
        part_2 += sum(find_invalid_ids_part_2(int(parts[0]), int(parts[1])))
        
print('part 1: ', part_1)
print('part 2: ', part_2)