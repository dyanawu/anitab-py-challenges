#!usr/bin/python3
# given x, y, z, n
# print list of coordinates if x + y + z != n
[x, y, z, n]  = [int(i) for i in input("Enter coordinates and target sum: ").split()]

print([
    [i, j, k]
    for i in range(x + 1)
    for j in range(y + 1)
    for k in range(z + 1)
    if i + j + k != n
])
