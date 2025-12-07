input = open('C:\\Users\\[USER]\\Downloads\\2025aoc7data.txt', 'r').read()

rows = input.split()
beams = [['.' for i in range(len(rows[0]))] for j in range(len(rows))]
for row in range(len(rows)):
    beams[row] = list(rows[row]) # convert list of strings to 2D array so we can do substitution

splits = 0
for row in range(len(beams)):
    for space in range(len(beams[row])):
        if beams[row][space] == 'S':
            beams[row+1][space] = '|'
            break # we only have one starting point, go to next row
        if beams[row][space] == '|':
            try:
                if beams[row+1][space] == '^': # found a splitter beneath a beam, thus we actually get a split
                    splits += 1
                    try:
                        beams[row+1][space-1] = '|'
                    except IndexError: # The provided data never tries to send the beam out of bounds sideways, but protecting against errors is still generally good practice
                        pass                
                    try:
                        beams[row+1][space+1] = '|'
                    except IndexError:
                        pass
                else: # if no splitter, the beam propogates on
                    beams[row+1][space] = '|'
            except IndexError:
                continue
print(splits)