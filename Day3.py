input = open('C:\\Users\\[USER]\\Downloads\\2025aoc3data.txt', 'r').read()

joltages = input.split()


#### PART 1 ####
total = 0
for joltage in joltages:
    first = 0
    second = 0
    for index in joltage: # pull each character from the bank
        if second > first: # run here so that we DON'T swap on the very last index, where we can't actually put the higher second in the tens place
            first = second # we want the highest digit possible in the tens place, so swap up any time second beats first
            second = 0
        if int(index) > second: # save the value if it beats our second digit, this increases our joltage
            second = int(index)
    total += 10*first + second # merge the two into one number and add it in
print(total)


#### PART 2 ####
total = 0
for string in joltages:
    joltage = list(map(int, string))
    output = [0] * 12
    start = 0
    for i in range(12):
        maximum = max(joltage[start:len(joltage)-11+i]) # Run from after last filled in digit to the last point far enough from the end that we can copy remaining list if needed
        start = joltage.index(maximum, start) + 1 # set system to check from just after the last value punched in
        total += maximum * 10**(11-i) # add max value to total, adjusted for its power of 10
print(total)