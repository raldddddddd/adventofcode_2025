arr = []
total = 0

while True:
    line = input()
    if not line:
        break
    arr.append(list(line.replace(".", "0")))

arr[1][len(arr[0]) // 2] = "1"
        
for i in range(1, len(arr)-1, 2):
    for j in range(len(arr[0])):
        if arr[i][j] != "." and arr[i+1][j] == "^":
            arr[i+2][j-1] = int(arr[i+2][j-1]) + int(arr[i][j])
            arr[i+2][j+1] = int(arr[i+2][j+1]) + int(arr[i][j])
        elif arr[i][j] != ".":
            arr[i+2][j] = int(arr[i+2][j]) + int(arr[i][j])
total = 0
for k in range(len(arr[0])):
    total += int(arr[len(arr)-1][k])
    
print(total)