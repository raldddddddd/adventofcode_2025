total = 0
length = 12 # only thing changed
while True:
    bank = input()
    if bank == "-1":
        break
    num = ['0'] * length
    index = 0
    pos = 0
    last = 0
    while index < length:
        for i, char in enumerate(bank[pos:len(bank)-(length-index)+1]):
            if int(char) > int(num[index]):
                num[index] = char
                last = i
        if last == 0:
            pos += 1
        else:
            pos += last + 1
        index +=1
    total += int("".join(map(str, num)))
    
print(total)