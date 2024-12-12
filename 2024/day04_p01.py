import time

forward_match = 'XMAS'

def get_cross(data, row, column, row_offset, column_offset):
    return ''.join([data[row+(i*row_offset)][column+(i*column_offset)] for i in range(4)])

def get_cross_count(data, row, column):
    # row check
    count = 0
    if 0 <= column-3 and get_cross(data, row, column, 0, -1) == forward_match:
        count += 1
    if column+3 < len(data[row]) and get_cross(data, row, column, 0, 1) == forward_match:
        count += 1
    # column check
    if 0 <= row-3 and get_cross(data, row, column, -1, 0) == forward_match:
        count += 1
    if row+3 < len(data) and get_cross(data, row, column, 1, 0) == forward_match:
        count += 1
    # main diagonal check
    if 0 <= row-3 and 0 <= column-3 and get_cross(data, row, column, -1, -1) == forward_match:
        count += 1
    if row+3 < len(data) and column+3 < len(data[row]) and get_cross(data, row, column, 1, 1) == forward_match:
        count += 1
    # antidiagonal check
    if row+3 < len(data) and 0 <= column-3 and get_cross(data, row, column, 1, -1) == forward_match:
        count += 1
    if 0 <= row-3 and column+3 < len(data[row]) and get_cross(data, row, column, -1, 1) == forward_match:
        count += 1
    return count

file = open('./data/day4.txt')
lines = file.read().split('\n')

start = time.perf_counter()
cross_count = 0
for row in range(len(lines)):
    for col in range(len(lines[row])):
        cross_count += get_cross_count(lines, row, col)
end = time.perf_counter()

duration_ns = (end-start)
print(f"It took {duration_ns}ns to calculate {cross_count}")


