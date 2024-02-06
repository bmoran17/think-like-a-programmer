hashes = ""
spaces = 0
for row in range(1,5):
    for i in range(row):
        hashes += " "
    for i in range(8-spaces):
        hashes += "#"
    spaces += 2
    hashes += "\n"
    
print(hashes)

# Should produce shape:
#row  #hashes  #amount
#1   ########    8
#2    ######     6
#3     ####      4
#4      ##       2
