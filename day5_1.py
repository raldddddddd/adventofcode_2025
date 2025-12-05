def lower_bound(id_ranges):
    return int(id_ranges.split('-')[0])

def is_fresh(id_ingredients, id_ranges):
    total = 0
    i = 0
    for id_range in id_ranges:
        lower, upper = [int(x) for x in id_range.split('-')]
        while True:
            if id_ingredients[i] < lower:
                i += 1
            elif id_ingredients[i] > upper:
                break
            else:
                total += 1
                i += 1
    return total

id_ranges = []
id_ingredients = []

while True:
    line = input()
    if line == "":
        break
    id_ranges.append(line)
    
while True:
    id = input()
    if id == "":
        break
    id_ingredients.append(int(id))
    
id_ranges.sort(key=lower_bound)
id_ingredients.sort()

print(is_fresh(id_ingredients, id_ranges))