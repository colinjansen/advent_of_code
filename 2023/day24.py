
def parse():
    H = []
    with open("_input/day24.txt", encoding='utf8') as f:
        for line in f.read().splitlines():
            a, b = line.split('@')
            x, y, z = a.split(',')
            d, e, f = b.split(',')
            H.append((int(x), int(y), int(z), int(d), int(e), int(f)))
    return H

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return None

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

def count_intersections(H, _min=7, _max=27):
    t = 0
    for i in range(len(H)):
        for j in range(i+1, len(H)):
            A = ((H[i][0], H[i][1]), (H[i][0]+H[i][3], H[i][1]+H[i][4]))
            B = ((H[j][0], H[j][1]), (H[j][0]+H[j][3], H[j][1]+H[j][4]))
            res = line_intersection(A, B)
            if res == None:
                #print(i, j, 'never cross')
                continue
            x, y = res
            if H[i][3] > 0 and x < H[i][0]:
                continue
            if H[i][3] < 0 and x > H[i][0]:
                continue
            if H[j][3] > 0 and x < H[j][0]:
                continue
            if H[j][3] < 0 and x > H[j][0]:
                continue
            if H[i][4] > 0 and y < H[i][1]:
                continue
            if H[j][4] < 0 and y > H[j][1]:
                continue
            if H[i][4] > 0 and y < H[i][1]:
                continue
            if H[j][4] < 0 and y > H[j][1]:
                continue
            if _min > x or x > _max or _min > y or y > _max:
                #print(i, j, 'crossed outside of the grid')
                continue
            #print(i, j, 'crossed at', res)
            t += 1
    return t


print(count_intersections(parse(), 200_000_000_000_000, 400_000_000_000_000))
