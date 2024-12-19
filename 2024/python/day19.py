def get_parts():
    with open('2024/_input/day19.txt') as f:
        parts = f.readline()
        parts = parts.split(",")
        f.readline()
        quilts = f.readlines()
        parts = frozenset([p.strip() for p in parts])
        quilts = [q.strip() for q in quilts]
    return parts, quilts

def can_make(quilt, parts, i=0, memo=None):
    """
    Returns True if the quilt can be made from the parts, False otherwise.

    quilt: str, the quilt to be made
    parts: set, the parts that can be used to make the quilt
    i:     int, the index of the quilt we are currently trying to make
    memo:  dict, a memoization dictionary to store the results of subproblems
    """
    if i == len(quilt):
        return True
    if memo is None:
        memo = {}
    if i in memo:
        return memo[i]
    for part in parts:
        # if this part fits the quilt
        if (i + len(part) <= len(quilt) and
            # and it matches the quilt
            quilt[i:i+len(part)] == part and  
            # and we can complete the quilt
            can_make(quilt, parts, i + len(part), memo)):
            # remember that from this point, with the previous parts
            # we can make the quilt
            memo[i] = True
            return True
    memo[i] = False
    return False

parts, quilts = get_parts()

part1 = 0
for i, quilt in enumerate(quilts):
    part1 += can_make(quilt, parts)

print(part1)
