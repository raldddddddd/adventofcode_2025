import numpy as np
num_arr = []
operations = []

while True:
    line = input()
    if "+" in line:
        operations.extend(line.split())
        break
    num_arr.append(list(map(int, line.split())))
    
totals = np.full(len(num_arr[0]), "", dtype=object) 

for i in range(len(num_arr)):
    for j in range(len(num_arr[0])):
        if not totals[j]:
            totals[j] = num_arr[i][j]
        elif operations[j] == "+":
            totals[j] += num_arr[i][j]
        else:
            totals[j] *= num_arr[i][j]

print(np.sum(totals))