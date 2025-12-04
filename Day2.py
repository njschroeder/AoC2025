input = open('C:\\Users\\[USER]\\Downloads\\2025aoc2data.txt', 'r').read()

IDs = input.split(',')

#### PART 1 ####
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


### PART 2 ####
invalids = 0
for pair in IDs:
    ID = pair.split('-') # break down to individual numbers
    start = int(ID[0])
    end = int(ID[1])
    for i in range(start, end+1): # iterate over provided range. Raise end b/c range function end is exclusive
        index = str(i)
        for _ in range(2, len(index)+1): # iterate over all division options (halves up to each individual number)
            check = index[:len(index)//_] # slice first chunk of the string
            if len(index)%len(check)==0:  # make sure the chunk can exactly repeat within the string
                repeated = True
                for j in range(len(check), len(index), len(check)):
                    test = index[j:j+len(check)] # pull the next chunk of the number
                    if test != check:
                        repeated = False # we proved it false, flag as such and move on
                        break
                if repeated:
                    invalids += i
                    break # some IDs are invalid in multiple ways. Once we've counted it as bad, move to the next
print(invalids)