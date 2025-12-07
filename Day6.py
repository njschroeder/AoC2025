input = open('C:\\Users\\[USER]\\Downloads\\2025aoc6data.txt', 'r').read()

hw = input.split('\n')
#### PART 1 ####
homework = ['', '', '', '', '']
for i in range(len(hw)): # cut up each string into a list
    homework[i] = hw[i].split()

grand_total = 0
for col in range(len(homework[0])): # the problems are in the columns, so that's our primary iteration
    if homework[len(homework)-1][col] == '+':
        for row in range(len(homework) - 1):
            grand_total += int(homework[row][col])
    elif homework[len(homework)-1][col] == '*':
        product = int(homework[0][col]) # intermediate variable to handle the multiplication series
        for row in range(1, len(homework) - 1):
            product *= int(homework[row][col]) # it'd be hard to make this direct to grand_total like in +
        grand_total += product
print(grand_total)


#### PART 2 ####
# Note: for numbers shorter than max length, spaces MATTER

# Other Note: if I were to do this upper part again, I'd probably try to track indices and use array slicing. This solution is CLUNKY
a = []
b = []
c = []
d = []
fixed_hw = [[],[],[],[]]
for i in range(len(hw[0])):
    if (hw[0][i] ==  ' ' and hw[1][i] == ' ' and hw[2][i] == ' ' and hw[3][i] == ' '): # look for separator column of all spaces
        fixed_hw[0].append(''.join(a)) # add the contents of the column into our new homework list
        fixed_hw[1].append(''.join(b))
        fixed_hw[2].append(''.join(c))
        fixed_hw[3].append(''.join(d))
        a = []
        b = []
        c = []
        d = []
    elif i == len(hw[0]) - 1: # catch the last character, then merge
        a.append(hw[0][i])
        b.append(hw[1][i])
        c.append(hw[2][i])
        d.append(hw[3][i])
        fixed_hw[0].append(''.join(a))
        fixed_hw[1].append(''.join(b))
        fixed_hw[2].append(''.join(c))
        fixed_hw[3].append(''.join(d))
    else:
        a.append(hw[0][i]) # store the characters for eventual reassembly
        b.append(hw[1][i])
        c.append(hw[2][i])
        d.append(hw[3][i])

grand_total = 0
for col in range(len(fixed_hw[0])): # the problems are in the columns, so that's our primary iteration
    if homework[len(homework)-1][col] == '+':
        # NUMBER BUILDER
        for num in range(len(fixed_hw[0][col])): # index of specific characters in the overall numbers
            number = 0
            for row in range(len(fixed_hw)): # the rows, i.e. which digit in the number to be added we're pulling
                try:
                    number += int(fixed_hw[row][col][num]) * 10**((len(fixed_hw)-1) - row)
                except ValueError: # the spaces won't cast to int
                    number *= 0.1 # accounts for the number being written on TOP instead of on bottom
                    continue
            grand_total += int(number) # can just accept the zero from case of less than four numbers, x + 0 = x
    
 
    elif homework[len(homework)-1][col] == '*': # the old homework list is fine here, we don't care about spaces for the operators
        product = 1
        # NUMBER BUILDER
        for num in range(len(fixed_hw[0][col])):
            number = 0
            for row in range(len(fixed_hw)):
                try:
                    number += int(fixed_hw[row][col][num]) * 10**((len(fixed_hw)-1) - row)
                except ValueError:
                    number *= 0.1 # fixes power of 10 for holes in bottom rows
                    continue
            product *= int(number)
        grand_total += product

print(grand_total)