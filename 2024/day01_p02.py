# Parse input
file = open('./data/day1.txt')
row_sep, col_sep = '\n', '   '
rows = file.read().split(row_sep)
first_col = [int(row.split(col_sep)[0]) for row in rows]
second_col = [int(row.split(col_sep)[1]) for row in rows]

# Similarity is the sum of all numbers in the first column and their count of occurences in the second column
similarity = 0
for number in first_col:
    similarity += number * second_col.count(number)

print(similarity)