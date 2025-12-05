input = open('C:\\Users\\[USER]\\Downloads\\2025aoc5data.txt', 'r').read()

two_strings = input.split('\n\n') # the empty separating line will be seen as two newlines in a row
ranges = two_strings[0].split()
indices = two_strings[1].split()
fresh = 0 # "My yeezys are fresh!" -Woodie Flowers, Huntsville, Alabama, 2017
for index in indices:
    for range in ranges:
        bounds = list(map(int, range.split('-')))
        if int(index) >= bounds[0] and int(index) <= bounds[1]:
            fresh += 1  # consider a new fresh index if it fits
            break       # it's only fresh once, stop here and go to the next index
print(fresh)

