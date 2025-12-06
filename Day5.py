input = open('C:\\Users\\[USER]\\Downloads\\2025aoc5data.txt', 'r').read()

two_strings = input.split('\n\n') # the empty separating line will be seen as two newlines in a row
ranges = two_strings[0].split()
indices = two_strings[1].split()


#### PART 1 ####
fresh = 0 # "My yeezys are fresh!" -Woodie Flowers, Huntsville, Alabama, 2017
for index in indices:
    for span in ranges: # range is a python keyword I use later, hence the name change
        bounds = list(map(int, span.split('-')))
        if int(index) >= bounds[0] and int(index) <= bounds[1]:
            fresh += 1  # consider a new fresh index if it fits
            break       # it's only fresh once, stop here and go to the next index
print(fresh)


#### PART 2 ####
freshes = []
fresh_count = 0
for span in ranges:
    bounds = list(map(int, span.split('-')))
    freshes.append((bounds[0], 1)) # 1 marks start of a run
    freshes.append((bounds[1], -1)) # -1 marks the end
freshes_ordered = sorted(freshes, key=lambda tup: tup[0]) # sort freshes by the first value in each of the contained lists
start = freshes_ordered[0][0]
net_startstop = 0
runs = []
for i in range(len(freshes_ordered)):
    net_startstop += freshes_ordered[i][1] # those 1s and -1s let us track this easily
    runs.append(freshes_ordered[i])
    if net_startstop == 0: # when we hit net zero, all starts and stops in a run (i.e. overlapping cases) cancel and we've found its end
        if i < len(freshes_ordered) - 1:
            if freshes_ordered[i+1][0] == freshes_ordered[i][0]:
                continue # if we start another run on the same value, keep going to avoid a double count
        fresh_count += (freshes_ordered[i][0] - start + 1)
        if i < len(freshes_ordered) - 1:
            start = freshes_ordered[i+1][0] # protects against error, we're done anyway if this doesn't run
        runs = []
print(fresh_count)