import re
import math

def part1():
    P = (0, 0)
    D = 0
    with open('day12.txt', 'r') as fp:
        for line in fp.readlines():
            d, v = re.match('(\w)(\d+)', line).groups()
            v = int(v)
            if d == 'N':
                P = (P[0], P[1]+v)
            if d == 'S':
                P = (P[0], P[1]-v)
            if d == 'E':
                P = (P[0]+v, P[1])
            if d == 'W':
                P = (P[0]-v, P[1])
            if d == 'L':
                D += v
                
                D %= 360
            if d == 'R':
                D -= v
                D %= 360
            if d == 'F':    
                rads = math.radians(D)
                dx = v*math.cos(rads)  # Adjacent = hypotenuse * cos(θ)
                dy = v*math.sin(rads)  # Opposite = hypotenuse * sin(θ)
                P = (P[0] + dx, P[1] + dy)
        return round(abs(P[0])+abs(P[1]))
    
def rotate_point(point: tuple[float, float], pivot: tuple[float, float], degrees: float) -> tuple[float, float]:
    theta = math.radians(degrees)
    
    # Translate point to origin by subtracting pivot
    translated_x = point[0] - pivot[0]
    translated_y = point[1] - pivot[1]
    
    # Rotate around origin using rotation matrix
    # | cos θ  -sin θ | | x |
    # | sin θ   cos θ | | y |
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)
    
    rotated_x = translated_x * cos_theta - translated_y * sin_theta
    rotated_y = translated_x * sin_theta + translated_y * cos_theta
    
    # Translate back by adding pivot
    final_x = rotated_x + pivot[0]
    final_y = rotated_y + pivot[1]
    
    return (final_x, final_y)

def part2():
    P = (0, 0)
    D = 0
    W = (10, 1)
    with open('day12.txt', 'r') as fp:
        for line in fp.readlines():
            d, v = re.match('(\w)(\d+)', line).groups()
            v = int(v)
            if d == 'N':
                W = (W[0], W[1]+v)
            if d == 'S':
                W = (W[0], W[1]-v)
            if d == 'E':
                W = (W[0]+v, W[1])
            if d == 'W':
                W = (W[0]-v, W[1])
            if d == 'L':
                W = rotate_point(W, P, v)
            if d == 'R':
                W = rotate_point(W, P, -v)
            if d == 'F':    
                dx = W[0] - P[0]
                dy = W[1] - P[1]
                P = (P[0] + dx * v, P[1] + dy * v)
                W = (P[0] + dx, P[1] + dy)
        return round(abs(P[0])+abs(P[1]))

print(part1())
print(part2())