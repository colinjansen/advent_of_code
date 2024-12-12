from collections import Counter

with open('2019/_input/day8.txt') as fp:
    line = fp.readline().strip()

def get_layers(line:str, width, height):
    layers = {}
    layer = 0
    offset = 0
    min_zeros = float('inf')
    out = None
    while offset + (width*height) < len(line):
        layers[layer] = []
        zeros = 0
        ones = 0
        twos = 0
        for i in range(height):
            offset = (i + (layer*height)) * width
            data = line[offset:offset+width]
            zeros += data.count('0')
            ones += data.count('1')
            twos += data.count('2')
            layers[layer].append(data)
        layer += 1
        if zeros < min_zeros:
            min_zeros = zeros
            out = ones * twos

    def get_pixel(x, y):
        for layer in layers.values():
            if layer[y][x] == '0':
                return '#'
            if layer[y][x] == '1':
                return '.'
        return ' '
    
    image = []
    for y in range(height):
        line = ''
        for x in range(width):
            line += get_pixel(x, y)
        image.append(line)
    return layers, out, image
    
layers, out, image = get_layers(line, 25, 6)
print(out)
for line in image:
    print(line)