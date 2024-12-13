import time

# 0 -> up, 1 -> right, 2 -> down, 3 -> left
def next_directon(i):
    return i+1 % 4

def traverse(obstacles, row, column, direction):
    match direction:
        case 0: # all obstacles above current position on same column
            obstacles_on_path = [obstacle for obstacle in obstacles if column == obstacle[1] and row > obstacle[0]]
            if obstacles_on_path:
                next_obstacle = max(obstacles_on_path)
                return (next_obstacle[0]+1, next_obstacle[1]), next_directon(direction)
        case 1: # all obstacles to the right of current position on same row
            obstacles_on_path = [obstacle for obstacle in obstacles if row == obstacle[0] and column < obstacle[1]]
            if obstacles_on_path:
                next_obstacle = min(obstacles_on_path)
                return (next_obstacle[0], next_obstacle[1]-1), next_directon(direction)
        case 2: # all obstacles below current position on same column
            obstacles_on_path = [obstacle for obstacle in obstacles if column == obstacle[1] and row < obstacle[0]]
            if obstacles_on_path:
                next_obstacle = min(obstacles_on_path)
                return (next_obstacle[0]-1, next_obstacle[1]), next_directon(direction)
        case 3: # all obstacles to the left of current position on same row
            obstacles_on_path = [obstacle for obstacle in obstacles if row == obstacle[0] and column > obstacle[1]]
            if obstacles_on_path:
                next_obstacle = max(obstacles_on_path)
                return (next_obstacle[0], next_obstacle[1]+1), next_directon(direction)
    return (row, column), direction    

# Parse data
lines = open('./data/day6.txt').read().split('\n')
MAX_ROW = len(lines)
MAX_COL = len(lines[0])
obstacles = []
start_row, start_col = -1, -1
for row in range(len(lines)):
    for col, cur_char in enumerate(lines[row]):
        if cur_char == '#': obstacles.append((row, col))
        if start_row == -1 and cur_char == '^':
            start_row, start_col = row, col

# Traverse map
direction = 0
(next_row, next_col) = (-1, -1)
while (start_row, start_col) != (next_row, next_col):
    (next_row, next_col), next_direction = traverse(obstacles, start_row, start_col, direction)
       



