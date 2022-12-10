import re

with open("_input/day9.txt", encoding='utf8') as f:
    lines = f.read().splitlines()

def clamp(n):
  if n > 0: return 1
  if n < 0: return -1
  return 0

class Point:
  def __init__(self):
    self.x = 0
    self.y = 0
  def move(self, d):
    if d == 'U': self.y += 1
    if d == 'D': self.y -= 1
    if d == 'R': self.x += 1
    if d == 'L': self.x -= 1
  def follow(self, x, y):
    if abs(self.x - x) <= 1 and abs(self.y - y) <= 1: return
    self.x += clamp(x - self.x)
    self.y += clamp(y - self.y)

p = [Point() for _ in range(0,10)]

v1 = {(p[1].x, p[1].y)}
v2 = {(p[9].x, p[9].y)}

for move in lines:
  d, m = move.split(' ')
  for _ in range(0, int(m)):
    p[0].move(d)
    for j in range(1, len(p)):
      p[j].follow(p[j-1].x, p[j-1].y)
      v1.add((p[1].x, p[1].y))
      v2.add((p[9].x, p[9].y))

print(f'{len(v1)} {len(v2)}')