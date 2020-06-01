#!usr/bin/python3
# given x, y, z, n
# print list of coordinates if x, y, z != n
[x, y, z, n]  = [int(i) for i in input("Enter coordinates and target sum: ").split()]

print([
    sublist for sublist in [
        [
            [
                [i, j, k] for k in range(z + 1) if i + j + k != n]
            for j in range(y + 1)]
        for i in range(x + 1)]
    for sublist in sublist
    for sublist in sublist
])
