input = open('C:\\Users\\[USER]\\Downloads\\2025aoc1data.txt', 'r').read()

turns = input.split() # convert input string to list of strings

#### PART 1 ####

dial = 50
password = 0
for turn in turns:
    if turn[0] == 'R':  # strings are kind of a wrapper for lists of characters
        dial += int(turn[1:]) # chop off direction, convert number from string and add
    else:
        dial -= int(turn[1:])
    if dial % 100 == 0: # modulo (%) tells us the remainder, so if dial / 100 = 0, we would've wrapped back around to zero
        password += 1
print(password)





#### PART 2 BRUTE FORCE EDITION ####

dial = 50
password = 0
for turn in turns:
    spin = int(turn[1:])
    if turn[0] == 'R':
        while spin > 0:
            spin -= 1 # enact one click
            dial += 1
            if dial%100 == 0:
                password += 1 # if that click got to zero, increment password
    else:
        while spin > 0:
            spin -= 1
            dial -= 1
            if dial%100 == 0:
                password += 1
print(password)