def lower_bound(id_ranges):
    return int(id_ranges.split('-')[0])

def remove_overlaps(id_ranges):
    total = 0
    new_range = []
    
    for i, id_range in enumerate(id_ranges):
        lower, upper = [int(x) for x in id_range.split('-')]
        if not new_range:
            new_range.append([lower, upper])
        else:
            _, prev_upper = new_range[-1]
            if lower <= prev_upper + 1:
                if upper > prev_upper:
                    new_range[-1][1] = upper
            else:
                new_range.append([lower, upper])
    
    for lower, upper in new_range:
        total += upper - lower + 1
    return total

id_ranges = []
while True:
    line = input()
    if line == "":
        break
    id_ranges.append(line)

id_ranges.sort(key=lower_bound)
print(remove_overlaps(id_ranges))