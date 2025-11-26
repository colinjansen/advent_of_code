
from hashlib import md5

i = 'ojvtpuvg'
b = [None]*8
c = 0
d = 0
while d < 8:
    c += 1
    h = md5(f'{i}{str(c)}'.encode('utf-8')).hexdigest()
    if h.startswith('00000'):
        p1 = int(h[5], base=16)
        p2 = h[6]
        print(p1, p2)
        if p1 < 8 and b[p1] == None:
            d += 1
            b[p1] = p2

print(str(b))