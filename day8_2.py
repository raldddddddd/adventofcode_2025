import math

boxes = []
while True:
    line = input()
    if not line:
        break
    boxes.append(line)

distances = []
for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        x1, y1, z1 = map(int, boxes[i].split(','))
        x2, y2, z2 = map(int, boxes[j].split(','))
        distance = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
        distances.append((distance, (i, j)))

distances.sort()

parent = {}

def find(x):
    if x not in parent:
        parent[x] = x
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb:
        parent[rb] = ra
        return True
    return False

last_merge = None

for _, (a, b) in distances:
    if union(a, b):
        last_merge = (a, b) 

i, j = last_merge

print(int(boxes[i].split(',')[0]) * int(boxes[j].split(',')[0]))