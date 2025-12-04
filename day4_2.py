def get_adjacent(r, c):
    global arr
    rows = len(arr)
    cols = len(arr[0])
    adjacent_elements = []
    x = [-1, -1, -1, 0, 0, 1, 1, 1]
    y = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    for i in range(len(x)):
        new_r, new_c = r + x[i], c + y[i]
        if 0 <= new_r < rows and 0 <= new_c < cols:
            adjacent_elements.append(arr[new_r][new_c])
    return adjacent_elements

total = 0
changed = True
arr = []
while True:
    line = input()
    if line == "-1":
        break
    arr.append(list(line))

while changed:
    changed = False
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != "@":
                continue
            adjacent_elements = get_adjacent(i, j)
            adjacency = 0
            for element in adjacent_elements:
                if element == "@":
                    adjacency += 1
            if adjacency < 4:
                changed = True
                arr[i][j] = "."
                total += 1
                
print(total)