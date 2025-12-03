def check_odd_lengths(lower,upper):
    is_lower_odd = len(str(lower)) % 2 == 1
    is_upper_odd = len(str(upper)) % 2 == 1
    return is_lower_odd, is_upper_odd

total = 0
ranges = [tuple(map(int, r.split("-"))) for r in input().split(",")]
for lower, upper in ranges:
    is_lower_odd, is_upper_odd = check_odd_lengths(lower, upper)
    if is_lower_odd and is_upper_odd:
        continue
    mid = len(str(lower)) // 2
    if is_lower_odd:
        half_lower = str(1) + str(0) * mid
    else: 
        half_lower = str(lower)[:mid]
        
    if is_upper_odd:
        half_upper = str(9) * mid
    elif is_lower_odd and not is_upper_odd:
        half_upper = str(upper)[:mid+1]
    else:
        half_upper = str(upper)[:mid]

    while int(half_lower) <= int(half_upper):
        id = int(half_lower * 2)
        if lower <= id <= upper:
            total += id
        half_lower = str(int(half_lower) + 1)

print(total)
