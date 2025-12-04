input = open('C:\\Users\\[USER]\\Downloads\\2025aoc4data.txt', 'r').read()

array = [list(row) for row in input.split()]

#### PART 1 ####
available = 0
for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] == '.': # not a roll, so we can't possibly remove it and skip
            continue
        total = 0
        # i/j comparisons skip cases that reach outside the grid
        if i > 0:
            if j > 0 and array[i-1][j-1] == '@':
                total += 1
            if array[i-1][j] == '@':
                total += 1
            if j < len(array[i]) - 1 and array[i-1][j+1] == '@':
                total += 1
        if j > 0 and array[i][j-1] == '@':
            total += 1
        if j < len(array[i]) - 1 and array[i][j+1] == '@':
            total += 1
        if i < len(array) - 1:
            if j > 0 and array[i+1][j-1] == '@':
                total += 1
            if array[i+1][j] == '@':
                total += 1
            if j < len(array[i]) - 1 and array[i+1][j+1] == '@':
                total += 1
        if total < 4:
            available += 1
print(available)


#### PART 2 ####
available = 0
prev_available = 0
while True:
    prev_available = available
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == '.': # not a roll, so we can't possibly remove it and skip
                continue
            total = 0
            # i/j comparisons skip cases that reach outside the grid
            if i > 0:
                if j > 0 and array[i-1][j-1] == '@':
                    total += 1
                if array[i-1][j] == '@':
                    total += 1
                if j < len(array[i]) - 1 and array[i-1][j+1] == '@':
                    total += 1
            if j > 0 and array[i][j-1] == '@':
                total += 1
            if j < len(array[i]) - 1 and array[i][j+1] == '@':
                total += 1
            if i < len(array) - 1:
                if j > 0 and array[i+1][j-1] == '@':
                    total += 1
                if array[i+1][j] == '@':
                    total += 1
                if j < len(array[i]) - 1 and array[i+1][j+1] == '@':
                    total += 1
            if total < 4:
                available += 1
                array[i][j] = '.' # remove roll
    if prev_available == available: # if we removed zero rolls of paper in the entire last check, we're done
        break
print(available)