import re
from collections import defaultdict

def build_map():
    R = defaultdict(list)
    S = ''
    with(open("_input/day19.txt", "r") as file):
        for line in file.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            m = re.match(r"(.+) => (.+)", line)
            if m:
                R[m[1]].append(m[2])
            else:
                S = line
    return R, S

def calibrate(molecule, mappings):
    result = set()

    for match, replacements in mappings.items():
        for i in [m.start() for m in re.finditer(match, molecule)]:
            for replacement in replacements:
                result.add(molecule[:i] + replacement + molecule[i+len(match):])

    return result

def get_reversed_mappins(mappings):
    reverse_mappings = {}
    for match, replacements in mappings.items():
        for replacement in replacements:
            reverse_mappings[replacement] = match
    return dict(sorted(reverse_mappings.items(), key=lambda x: len(x[0]), reverse=True))

def from_molecule(molecule, mappings):
    result = set()
    # Reverse the mappings to find replacements
    reverse_mappings = get_reversed_mappins(mappings)
    while molecule != 'e':
        for match, replacement in reverse_mappings.items():
            if match in molecule:
                # Replace the first occurrence of the match with the replacement
                i = molecule.index(match)
                molecule = molecule[:i] + replacement + molecule[i+len(match):]
                result.add(molecule)
                break
        else:
            # If no replacements were made, we are done
            break

    return result

mappings, molecule = build_map()
print("Part 1:", len(calibrate(molecule, mappings)))
print("Part 2:", len(from_molecule(molecule, mappings)))