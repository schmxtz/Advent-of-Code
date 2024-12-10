from pprint import pprint

# 0 -> up, 1 -> right, 2 -> down, 3 -> left
direction_table = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
def next_direction(direction):
    return (direction + 1) % 4

def on_path(obstacles, past_paths, cur_pos):
    (cur_row, cur_col, cur_dir) = cur_pos
    axis = 0 if cur_dir % 2 == 0 else 1  
    # all path going in same direction and on same axis
    possible_paths = [(start, end, path_dir) for (start, end, path_dir) in past_paths if start[axis] == cur_pos[axis] and path_dir == cur_dir]
    return any(start[0] <= cur_row < end[0] and start[1] <= cur_col < end[1] for (start, end, _) in possible_paths)



    
    


def check_circular_path(obstacles, cur_pos):
    (row, col, direction) = cur_pos
    while True:


if __name__ == '__main__':
    with(open('./data/day6.txt') as file):
        lines = file.read().split('\n')
        obstacles = [(row, col) for row in range(len(lines)) for col, cur_char in enumerate(lines[row]) if cur_char == '#']
        row, col = [(row, col) for row in range(len(lines)) if (col:=lines[row].find('^')) != -1][0]

    current_direction = 0
    circular_paths = set()
    while True:
