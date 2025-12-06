import re
arr = []
total = 0

while True:
    line = input()
    if not line:
        break
    arr.append(line)
    
problem = ""
for j in range(len(arr[0])-1, -1, -1):
    for i in range(len(arr)):
        if arr[i][j] == "+" or arr[i][j] == "*":
            total += eval(re.sub(r"\s+", arr[i][j], problem.strip()))
            problem = ""
        else:
            problem += arr[i][j]

print(total)