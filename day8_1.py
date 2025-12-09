import math
import bisect

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
        bisect.insort(distances, (distance, [i, j]))
        if len(distances) > 1000:
            distances.pop()
            
distances = [set(pair_indices) for _, pair_indices in distances]

print(distances)

merged = True
while merged:
    merged = False
    results = []
    while distances:
        common = distances.pop(0)
        rest = []
        for item in distances:
            if not item.isdisjoint(common):
                common |= item
                merged = True
            else:
                rest.append(item)
        results.append(common)
        distances = rest
    distances = results
distances.sort(key=len, reverse=True)
print(math.prod(len(s) for s in distances[:3]))