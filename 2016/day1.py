P = "R4, R3, L3, L2, L1, R1, L1, R2, R3, L5, L5, R4, L4, R2, R4, L3, R3, L3, R3, R4, R2, L1, R2, L3, L2, L1, R3, R5, L1, L4, R2, L4, R3, R1, R2, L5, R2, L189, R5, L5, R52, R3, L1, R4, R5, R1, R4, L1, L3, R2, L2, L3, R4, R3, L2, L5, R4, R5, L2, R2, L1, L3, R3, L4, R4, R5, L1, L1, R3, L5, L2, R76, R2, R2, L1, L3, R189, L3, L4, L1, L3, R5, R4, L1, R1, L1, L1, R2, L4, R2, L5, L5, L5, R2, L4, L5, R4, R4, R5, L5, R3, L1, L3, L1, L1, L3, L4, R5, L3, R5, R3, R3, L5, L5, R3, R4, L3, R3, R1, R3, R2, R2, L1, R1, L3, L3, L3, L1, R2, L1, R4, R4, L1, L1, R3, R3, R4, R1, L5, L2, R2, R3, R2, L3, R4, L5, R1, R4, R5, R4, L4, R1, L3, R1, R3, L2, L3, R1, L2, R3, L3, L1, L3, R4, L4, L5, R3, R5, R4, R1, L2, R3, R5, L5, L4, L1, L1"

current_location = (0,0)
current_direction = 0
part_2 = None

DIRECTIONS = [(0,1), (1, 0), (0,-1), (-1, 0)]
VISITED = set()

def distance(current_location):
    return abs(current_location[0]) + abs(current_location[1])
    
for p in P.split(", "):
    # spin
    if p[:1] == "R":
        current_direction = (current_direction + 1) % 4
    else:
        current_direction = (current_direction - 1) % 4
    x, y = DIRECTIONS[current_direction]
    
    # move
    for _ in range(int(p[1:])):
        current_location = (current_location[0] + x, current_location[1] + y)
        if current_location in VISITED and part_2 == None:
            #print(current_location, abs(current_location[0]) + abs(current_location[1]))
            part_2 = distance(current_location)
        VISITED.add(current_location)
        
print(distance(current_location), part_2)