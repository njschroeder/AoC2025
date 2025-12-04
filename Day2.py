input = open('C:\\Users\\[USER]\\Downloads\\2025aoc2data.txt', 'r').read()

IDs = input.split(',')
invalids = 0
for pair in IDs:
    ID = pair.split('-') # break down to individual numbers
    start = int(ID[0])
    end = int(ID[1])
    for i in range(start, end+1): # iterate over provided range. Raise end b/c range function end is exclusive
        index = str(i)
        front = index[:len(index)//2] # slice front half of string
        back = index[len(index)//2:]  # slice back half of string
        if front == back:
            invalids += i # if the halves are the same, add the ID being checked
print(invalids)