hashes = ""
spaces = 6
for row in range(1,9):
    for i in range(spaces//2):
        hashes += "_"
    for i in range(8-spaces):
        hashes += "#"
    spaces -= 2
    if ()
    hashes += "\n"
print(hashes)

# Should produce shape:
#row #hashes #amount #spaces(T-total, h-half/sides)
#1     ##      2       6T-3h
#2    ####     4       4T-2h
#3   ######    6       2T-1h
#4  ########   8       0T-0h
#5  ########   8       0T-0h
#6   ######    6       2T-1h
#7    ####     4       4T-2h
#8     ##      2       6T-3h