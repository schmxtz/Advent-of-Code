from pprint import pprint


# cursor information is encoded as 4 byte number 
def get_next_index(cursor: int, row: int, col: int) -> tuple[int, int]:
    match cursor:
        case 0b0001: # ^
            return (row-1, col)
        case 0b0010: # >
            return (row, col+1)
        case 0b0100: # v
            return (row+1, col)
        case 0b1000: # <
            return (row, col-1)
        
def four_byte_rotate_left(cursor: int) -> int:
    # 1000 -> 0001, 0001 -> 0010 ...
    return ((cursor << 1) | ((cursor >> 3) & 1)) & 15

def map_input(char: str) -> int:
    match char:
        case '.':
            return 0
        case '#':
            return -1
        case '^':
            return 0b0001
        case _:
            raise Exception(f"Unknown input: {char}")

def check_with_new_obstacle(data: int[int[]], row: int, col: int, cursor]):
    while True:

if __name__ == '__main__':
    data = []
    with(open('./data/day6.txt') as file):
        line_ctr = 0
        row = -1
        col = -1
        while (line:= file.readline()):
            if row == -1 and (idx:=line.find('^'))!= -1: row, col = line_ctr, idx
            line = list(map(map_input, line.strip()))
            data.append(list(line))
            line_ctr += 1
    start_row = row
    start_col = col

    # Traverse entire map and save visited tiles' informatio (in which direction it has been crossed)
    next_cursor = 0b0001
    while(True):
        cursor = next_cursor
        next_row, next_col = get_next_index(cursor, row, col) 
        if not (0 <= next_row < len(data) and 0 <= next_col < len(data[next_row])): break

        next_tile = data[next_row][next_col]
        match next_tile:
            case -1: # next tile is an obstacle (#)
                next_cursor = four_byte_rotate_left(cursor)
            case _: # next tile can be visited
                data[row][col] |= cursor
                data[next_row][next_col] |= cursor
                row, col = next_row, next_col

    row = start_row
    col = start_col
    obstruction_ctr = 0
    next_cursor = 0b0001
    while(True):
        cursor = next_cursor
        next_row, next_col = get_next_index(cursor, row, col) 
        if not (0 <= next_row < len(data) and 0 <= next_col < len(data[next_row])): break

        next_tile = data[next_row][next_col]
        match next_tile:
            case -1: # next tile is an obstacle (#)
                next_cursor = four_byte_rotate_left(cursor)
            case _: # next tile can be visited
                data[row][col] |= cursor
                data[next_row][next_col] |= cursor
                row, col = next_row, next_col

    print(obstruction_ctr)


