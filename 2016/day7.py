import re

def tls_supported(ip):
    def inside_brackets(match: re.Match[str]):
        return match.start() > 0 and ip[match.start() - 1] == '['
    def abba(part: str):
        return part[0] != part[1] and part[0] == part[3] and part[1] == part[2]
    tls_supported = False
    for match in re.finditer(r'(\w+)', ip):
        part = match.group(1)
        if not inside_brackets(match):
            if any(abba(part[i:i+4]) for i in range(len(part) - 3)):
                tls_supported = True
        else:
            if any(abba(part[i:i+4]) for i in range(len(part) - 3)):
                return False
    return tls_supported

def ssl_supported(ip):
    def inside_brackets(match: re.Match[str]):
        return match.start() > 0 and ip[match.start() - 1] == '['
    supers = set()
    hypers = set()
    for match in re.finditer(r'(\w+)', ip):
        part = match.group(1)
        if not inside_brackets(match):
            supers.add(part)
        else:
            hypers.add(part)
    for super in supers:
        for i in range(len(super) - 2):
            aba_pattern = super[i:i+3]
            if aba_pattern[0] != aba_pattern[1] and aba_pattern[0] == aba_pattern[2]:
                bab_pattern = aba_pattern[1] + aba_pattern[0] + aba_pattern[1]
                for hyper in hypers:
                    if bab_pattern in hyper:
                        return True
    return False


tls_ips = 0
ssl_ips = 0
with open("_input/day7.txt") as f:
    for line in f.readlines():
        if tls_supported(line.strip()):
            tls_ips += 1
        if ssl_supported(line.strip()):
            ssl_ips += 1
print("Part 1:", tls_ips)
print("Part 2:", ssl_ips)