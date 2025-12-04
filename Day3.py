input = open('C:\\Users\\[USER]\\Downloads\\2025aoc3data.txt', 'r').read()

joltages = input.split()

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