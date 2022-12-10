with open("_input/day6.txt", encoding='utf8') as f:
    input = f.read()

def check(items):
    sortedItems = sorted(items)
    for i in range(1, len(sortedItems)):
        if sortedItems[i-1] == sortedItems[i]: return False
    return True

def findMarker(length):
    for i in range(length, len(input)):
        result = check(list(input[i-length:i]))
        if (result == True): 
            return i

print(f'part 1 is {findMarker(4)}, part 2 is {findMarker(14)}')