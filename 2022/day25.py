

with open('_input/day25.txt') as f:
    input = f.read().splitlines()


def from_snafu(snafu: str) -> int:

    SNAFU = {}
    SNAFU['2'] = 2
    SNAFU['1'] = 1
    SNAFU['0'] = 0
    SNAFU['-'] = -1
    SNAFU['='] = -2

    number = 0
    for idx in range(len(snafu)):
        place = len(snafu) - idx - 1
        number += 5**place * SNAFU[snafu[idx]]
    return number


def to_snafu(number: int) -> int:

    place = 0
    snafu = ''
    snafu_place_values = []

    SNAFU = {}
    SNAFU[2] = '2'
    SNAFU[1] = '1'
    SNAFU[0] = '0'
    SNAFU[-1] = '-'
    SNAFU[-2] = '='

    def get_snafu_at_place(number: int, place: int) -> tuple:
        possibles = {}
        best_index = -2
        for idx in range(-2, 3):
            val = 5**place * idx
            dif = val - number
            possibles[idx] = (idx, val, dif)
            if abs(possibles[best_index][2]) > abs(dif):
                best_index = idx
        return possibles[best_index]

    # find the 'place' to start from
    while number > 2 * 5**place:
        place += 1
    # roll back 'places' until we get to 5**0
    while place >= 0:
        result = get_snafu_at_place(number, place)
        place -= 1
        snafu_place_values.append(result[0])
        number -= result[1]
    
    for place_value in snafu_place_values:
        snafu += SNAFU[place_value]
        
    return snafu


def part1(lines):
    t = 0
    for line in lines:
        n = from_snafu(line)
        t += n
    return to_snafu(t)


print(part1(input))
