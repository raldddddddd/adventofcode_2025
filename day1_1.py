def rotate(rotation):
    global x, i
    if rotation.startswith("R"):
        add = int(rotation[1:])
        x = (x+add) % 100
    else:
        minus = int(rotation[1:])
        x = (x-minus) % 100
    if x == 0:
        i += 1

i = 0
x = 50
rotation = ""
while rotation != -1:
    rotation = input("Enter:")
    print(rotation)
    if rotation == "-1":
        break
    rotate(rotation)

print(i)