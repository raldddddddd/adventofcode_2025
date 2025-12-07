arr = []
total = 0

while True:
    line = input()
    if not line:
        break
    arr.append(list(line))

arr[1][len(arr[0]) // 2] = "|"
        
for i in range(1, len(arr)-1, 2):
    for j in range(len(arr[0])):
        if arr[i][j] == "|" and arr[i+1][j] == "^":
            total += 1
            arr[i+2][j-1] = "|"
            arr[i+2][j+1] = "|"
        elif arr[i][j] == "|":
            arr[i+2][j] = "|"
            
print(total)