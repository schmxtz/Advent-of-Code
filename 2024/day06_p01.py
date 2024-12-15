import time

# 0 -> up, 1 -> right, 2 -> down, 3 -> left
def next_directon(i):
    return (i+1) % 4

def traverse(obstacles, position, direction):
    row, column = position
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
        case _:
            raise Exception('invalid direction')
    return (row, column), direction

def points_on_line(start, end):
    x1, y1 = start
    x2, y2 = end
    deltax = x2-x1
    deltax = 1 if deltax == 0 else int(abs(deltax)/deltax)
    deltay = y2-y1
    deltay = 1 if deltay == 0 else int(abs(deltay)/deltay)
    return set([(i,j) for i in range(x1, x2+deltax, deltax) for j in range(y1, y2+deltay, deltay)])

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

start = time.perf_counter()
# Traverse map
visited_tiles = set()
direction = 0
position = (start_row,start_col)
next_position = (-1,-1)
while True:
    next_position, next_direction = traverse(obstacles, position, direction)
    if position != next_position: 
        visited_tiles |= points_on_line(position, next_position)
        position = next_position
        direction = next_direction
    elif direction != next_direction:
        direction = next_direction
        continue
    else: 
        match direction:
            case 0:
                visited_tiles |= points_on_line(position, (0, position[1]))
            case 1:
                visited_tiles |= points_on_line(position, (position[0], MAX_COL-1))
            case 2:
                visited_tiles |= points_on_line(position, (MAX_ROW-1, position[0]))
            case 3:
                visited_tiles |= points_on_line(position, (position[0], 0))
        break
end = time.perf_counter()

duration_ns = (end-start)
print(f"It took {duration_ns}s to calculate {len(visited_tiles)}")
    




