from queue import PriorityQueue
from collections import defaultdict

def search(starting_state, pods_in_group):
    # game states
    states = defaultdict(lambda: float('inf'))
    target_states = defaultdict(int)
    states[starting_state] = 0
    lowest_energy = int(1e9)
    # 'visited' states
    visited = []
    queue = PriorityQueue()
    queue.put((0, starting_state))
    while not queue.empty():
        (energy, current_state) = queue.get()
        #print(queue.qsize())
        visited.append(current_state)
        if is_target_state(current_state):
            if energy < lowest_energy:
                target_states[current_state] = energy
                print(f'found target state: {current_state} energy {energy}')
                lowest_energy = energy
            continue
        for (energy, next_state) in get_moves(current_state, pods_in_group):   
            if next_state not in visited:
                old_energy = states[next_state]
                new_energy = states[current_state] + energy
                if new_energy < lowest_energy and new_energy < old_energy:
                    queue.put((new_energy, next_state))
                    states[next_state] = new_energy
    return target_states

def is_target_state(state):
    for i, a in enumerate(state):
        target_room = 2*(i//2)+2
        if a[1] == 0 or a[0] != target_room:
            return False
    return True

def get_hallway_path(x, target):
    start = min(x, target)
    end = max(x, target)
    path = list(range(start, end))
    path.append(end)
    path.remove(x)
    return path

def get_energy(i, moves):
    if i in [0,1,2,3]: return moves
    if i in [4,5,6,7]: return moves * 10
    if i in [8,9,10,11]: return moves * 100
    if i in [12,13,14,15]: return moves * 1000

DPM = {}
def get_moves(state, pods_in_group):

    if state in DPM: 
        return DPM[state]

    moves = []
    rooms = defaultdict(lambda: [])
    hallway = []
    for i, a in enumerate(state):
        if a[1] < 0:
            rooms[a[0]].append((i, a))
        else:
            hallway.append(a[0])
    # state
    #    A     A     B     B     C     C     D     D
    # [(x,y),(x,y),(x,y),(x,y),(x,y),(x,y),(x,y),(x,y)]
    for i, a in enumerate(state):
        target_room = pods_in_group*(i//pods_in_group)+2

        # are we where we belong?
        if a[0] == target_room:

            # if we're at the back, we're fine
            if a[1] == pods_in_group * -1:
                continue

            # if the room only contains my peeps, we're fine
            if all(pods_in_group*(t[0]//pods_in_group)+2 == target_room for t in rooms[target_room]):
                continue

        # if we are in the hallway
        if (a[1] == 0):

            # do we have a line of site to our room?
            # - figure out which spaces we'll need to move to on our way to our room
            hallway_path = get_hallway_path(a[0], target_room)

            # - are we blocked by someone else in the hallway?
            if any(step in hallway_path for step in hallway):
                continue

            # can we enter our target room?
            if len([x for x in rooms[target_room] if x[0]//pods_in_group != i//pods_in_group]) > 0:
                continue

            # - move into our room
            room_steps = pods_in_group - len(rooms[target_room])
            new_state = list(state)
            new_state[i] = (target_room, room_steps * -1)
            energy = get_energy(i, len(hallway_path) + room_steps)
            move = list()
            move.append((energy, tuple(new_state)))
            DPM[state] = move
            return move

        # if we are moving into a hallway
        if a[1] < 0:      

            # are we blocked?
            if a[0] != target_room and a[1] < -1 and len(rooms[a[0]]) > 1:
                for i, b in rooms[a[0]]:
                    if b[1] > a[1]:
                        continue

            # for all of the possible destinations in the hallway
            for destination in [0,1,3,5,7,9,10]:
                hallway_path = get_hallway_path(a[0], destination)
                
                # - are we blocked by someone else in the hallway?
                if any(step in hallway_path for step in hallway):
                    continue
                new_state = list(state)
                new_state[i] = (destination, 0)
                energy = get_energy(i, len(hallway_path) + (a[1] * -1))
                moves.append((energy, tuple(new_state)))

    DPM[state] = moves
    return moves

##################
#     01234567890
#    #############
#  0 #...........#
# -1 ###B#C#B#D###
# -2   #D#C#B#A#
# -3   #D#B#A#C#
# -4   #A#D#C#A#
#      #########
#start = ((2,-4),(8,-2),(8,-4),(6,-3),(2,-1),(6,-1),(4,-3),(6,-2),(4,-1),(6,-2),(4,-2),(8,-3),(4,-2),(8,-1),(2,-2),(2,-3))
#energy = 12521
#    #############
#  0 #...........#
# -1 ###D#C#A#B###
# -2   #D#C#B#A#
# -3   #D#B#A#C#
# -4   #D#C#B#A#
#      #########
#start = ((6,-1),(8,-2),(6,-2),(8,-1),(4,-2),(4,-1),(2,-2),(2,-1))
#energy = 

states = search(start, 4)
key_min = min(states.keys(), key=(lambda k: states[k]))
print(f'looks like {states[key_min]} is the least energy possible')