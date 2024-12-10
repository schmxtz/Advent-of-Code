# Parse input
file = open('./data/day1.txt')
row_sep, col_sep = '\n', '   '
rows = file.read().split(row_sep)
first_col = [int(row.split(col_sep)[0]) for row in rows]
second_col = [int(row.split(col_sep)[1]) for row in rows]

# Need to match smallest, 2nd smallest, ... nth smallest number
first_col.sort()
second_col.sort()

assert(len(first_col) == len(second_col))
n = len(first_col)
difference = 0
for i in range(n):
    difference += abs(first_col[i] - second_col[i])

print(difference)