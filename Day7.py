input = open('C:\\Users\\[USER]\\Downloads\\2025aoc7data.txt', 'r').read()

rows = input.split()
beams = [['.' for i in range(len(rows[0]))] for j in range(len(rows))]
for row in range(len(rows)):
    beams[row] = list(rows[row]) # convert list of strings to 2D array so we can do substitution

#### PART 1 ####
splits = 0
# small caveat: this implementation only works because the splitters are all spaced with at least one blank line between them
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


#### PART 2 ####
options = [[0 for i in range(len(rows[0]))] for j in range(len(rows))]
# for this implementation, we take advantage of the fact that Part 1 already filled in the beams for us
for row in range(len(beams)):
    for space in range(len(beams[row])):
        if beams[row][space] == 'S':
            options[row+1][space] = 1 # one option out of the starting point
            break # we only have one starting point, go to next row
        if beams[row][space] == '|':
            try: # We had a certain number of options to get to the beam, so we put that to both sides
                if beams[row+1][space] == '^': 
                    try:
                        options[row+1][space-1] += options[row][space]
                    except IndexError: # The provided data never tries to send the beam out of bounds sideways, but protecting against errors is still generally good practice
                        pass                
                    try: # if another splitter sends a beam there, we add those options in
                        options[row+1][space+1] += options[row][space]
                    except IndexError:
                        pass
                else: # += instead of = is actually important here. If a splitter lines up just right, it can merge a beam in and add to the uninterrupted beam coming down
                    options[row+1][space] += options[row][space] 
            except IndexError:
                continue
print(sum(options[len(options)-1]))