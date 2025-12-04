import math

def get_Bounds(lower, upper):
    len_lower = math.floor(math.log10(int(lower)) + 1)
    len_upper = math.floor(math.log10(int(upper)) + 1)
    if len_lower % 2 == 1:
        half_lower = int("1{0}".format('0' * (len_lower // 2)))
    else:
        half_lower = int(str(lower)[:len_lower // 2])
        if half_lower < int(str(lower)[len_lower // 2:]):
            half_lower += 1

    if len_upper % 2 == 1:
        half_upper = int("9{0}".format('9' * ((len_upper // 2) - 1)))
    else:
        half_upper = int(str(upper)[:len_upper // 2])
        if half_upper > int(str(upper)[len_upper // 2:]):
            half_upper -= 1 
        
    print(half_lower,half_upper)
    return half_lower, half_upper
    
total = 0
ranges = [tuple(map(int, r.split("-"))) for r in input().split(",")]
for lower, upper in ranges:
    half_lower, half_upper = get_Bounds(lower, upper)
    total += (half_upper-half_lower+1) * (int(str(half_upper)*2)+int(str(half_lower)*2)) // 2

print(total)
