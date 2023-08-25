import re

i = '1321131112'

def process(input_string):
    buffer = ''
    current_queue = []
    last_character = ''
    for c in input_string:
        if last_character != c:
            if last_character != '':
                buffer += str(len(current_queue)) + current_queue[0]
            last_character = c
            current_queue.clear()
        current_queue.append(c)
    if last_character != '':
        buffer += str(len(current_queue)) + current_queue[0]
    return buffer


for _ in range(50):
    i = process(i)
    
print(len(i))