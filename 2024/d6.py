from pprint import pprint

def get_next_index(cursor, row, col):
    match cursor:
        case '^':
            return (row-1, col)
        case '>':
            return (row, col+1)
        case 'v':
            return (row+1, col)
        case '<':
            return (row, col-1)

data = []
with(open('./data/day6.txt') as file):
    row = 0
    col = -1
    line_ctr = 0
    while (line:= file.readline()):
        line = line.strip()
        data.append(list(line))
        if (idx:=line.find('^'))!= -1: row, col = line_ctr, idx
        line_ctr += 1
start_row = row
start_col = col

direction = 0
directions = ['^', '>', 'v', '<']
while(True):
    cursor = data[row][col]
    if not isinstance(cursor, str):
        cursor = cursor[-1]
    (next_row, next_col) = get_next_index(cursor, row, col)

    if not (0 <= next_row < len(data) and 0 <= next_col < len(data[next_row])): break
    next_tile = data[next_row][next_col]
    if not isinstance(next_tile, str):
        next_tile = next_tile[-1]
    match next_tile:
        case '.':
            if isinstance(data[row][col], list):
                data[row][col].append(cursor)
            else:
                data[row][col] = cursor
            data[next_row][next_col] = cursor
            row = next_row
            col = next_col
        case '#':
            direction = (direction + 1) % 4
            if isinstance(data[row][col], list):
                data[row][col].append(directions[direction])
            else:
                data[row][col] = [directions[direction]]
        case _:
            if isinstance(data[next_row][next_col], list):
                data[next_row][next_col].append(cursor)
            else:
                data[next_row][next_col] = [next_tile, cursor]
            row = next_row
            col = next_col

row = start_row
col = start_col
obstruction_ctr = 0
direction = 0
cursor = '^'
while(True):
    print(row, col)
    (next_row, next_col) = get_next_index(cursor, row, col)
    if not (0 <= next_row < len(data) and 0 <= next_col < len(data[next_row])): break
    next_tile = data[next_row][next_col]
    match next_tile:
        case '#':
            print(next_tile)
            direction = (direction + 1) % 4
            cursor = directions[direction]
        case _:
            new_cursor = directions[(direction + 1) % 4]
            if new_cursor in data[row][col] or :
                obstruction_ctr += 1
            row = next_row
            col = next_col


print(obstruction_ctr)


