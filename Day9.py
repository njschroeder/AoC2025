input = open('C:\\Users\\[USER]\\Downloads\\2025aoc9data.txt', 'r').read()

coords = input.split()

max_area = 0

for i in range(len(coords)):
    start = list(map(int, coords[i].split(',')))
    for j in range(i+1, len(coords)): # any pair before i+1 was already tried earlier
        end = list(map(int, coords[j].split(',')))
        area = abs(start[0]-end[0]+1)*abs(start[1]-end[1]+1) # +1 b/c we need inclusive (i.e. 5-3 is 3 long, not 2 long)
        if area > max_area:
            max_area = area
print(max_area)