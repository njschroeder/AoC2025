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


#### PART 2 ####

dial = 50
password = 0
for i in range(len(turns)):
    # // performs integer division, simply shifting the hundreds place "bit" over two slots. We click on the scale of hundreds, hence why we measure this
    turn = turns[i]
    hundreds_last = dial // 100
    if turn[0] == 'R':
        dial += int(turn[1:])
    else:
        dial -= int(turn[1:])
    hundreds_current = dial // 100
    # however many changes we get in the hundreds level is our count of zero passes (with some edge cases)
    delta = hundreds_current - hundreds_last
    password += abs(delta) # we only care about count, not direction, hence absolute value
    
    #### EDGE CASE HANDLING ####
    if dial%100 == 0:
        try: # while my specific data doesn't try this on the last index, it's good to consider
            next = turns[i+1]
        except IndexError: 
            if delta < 0: # down from above case, we've currently undercounted by one
                password += 1
            break
        if delta > 0 and next[0] == 'L': # up from below case
            password -= 1 # if we next go back down, the hundreds count will change AGAIN and cause a double count
        elif delta < 0 and next[0] == 'R': # down from above case
            password += 1 # if we next go back up, the hundreds count never changes for this and misses the case
print(password)