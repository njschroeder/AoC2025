input = open('C:\\Users\\[USER]\\Downloads\\2025aoc6data.txt', 'r').read()

homework = input.split('\n')
for i in range(len(homework)): # cut up each string into a list
    homework[i] = homework[i].split()
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