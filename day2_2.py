def is_invalid(num):
    n = len(num)
    for length in range(1, n):
        if n % length == 0:
            sequence = num[:length]
            if sequence * (n // length) == num:
                return True
    return False

total = 0
ranges = [tuple(map(int, r.split("-"))) for r in input().split(",")]
for lower, upper in ranges:
    for num in range(lower, upper+1):
        if is_invalid(str(num)):
            total += num
print(total)