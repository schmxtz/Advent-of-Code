from operator import gt, lt
import time

def get_positions_on_path(obstacles, position, direction, data):
    visited_tiles = set()
    position = get_next_position(position, direction)
    while 0 <= position[0] < len(data) and 0 <= position[1] < len(data[position[0]]):
        next_position = get_next_position(position, direction)
        if next_position in obstacles:
            direction = (direction+1)%4
        else:
            visited_tiles.add(position)
            position = next_position
    return visited_tiles


def get_next_position(position, direction):
    next_position = list(position)
    axis, offset = directions[direction]
    next_position[axis] = next_position[axis]+offset
    return tuple(next_position)

def get_previous_position(position, direction):
    previous_position = list(position)
    axis, offset = directions[direction]
    previous_position[axis] = previous_position[axis]-offset
    return tuple(previous_position)

def get_next_obstacle(obstacles, position, direction):
    axis, offset = directions[direction]
    matching_axis = (axis+1)%2
    # offset = 1 means that the obstacle comes after the current POS, so the closest one is the one with the lowest index
    closest = min if offset == 1 else max
    comparator = gt if offset == 1 else lt
    obstacles_on_path = [obstacle for obstacle in obstacles if obstacle[matching_axis] == position[matching_axis] and comparator(obstacle[axis], position[axis])]
    if obstacles_on_path:
        return closest(obstacles_on_path)
    else:
        return None

def traverse(obstacles, position, direction):
    seen_positions = set()   # Set of visited obstacles and in which direction we were going
    while True:
        visited_obstacle = get_next_obstacle(obstacles, position, direction)
        if visited_obstacle is None:    # No obstacle on path means we're leaving the map => no loop
            return False
        else:
            if (visited_obstacle, direction) in seen_positions:
                return True
            seen_positions.add((visited_obstacle, direction))
            position = get_previous_position(visited_obstacle, direction)
            direction = (direction+1)%4
                


lines = open('./data/day6.txt').read().split('\n')
START_TOKEN = '^'
OBSTACLE_TOKEN = '#'
obstacles = set()
for row in range(len(lines)):
    for col in range(len(lines[row])):
        if lines[row][col] == OBSTACLE_TOKEN:
            obstacles.add((row, col))
        elif lines[row][col] == START_TOKEN:
            position = (row, col)
        else:
            continue

start = time.perf_counter()
direction = 0
directions = [(0,-1), (1,1), (0,1), (1,-1)]
looping_obstacles = set()

for obstacle in get_positions_on_path(obstacles, position, direction, lines):
    direction = 0
    is_loop = traverse(obstacles | set([obstacle]), position, direction)
    if is_loop and obstacle != position:
        looping_obstacles.add(obstacle)
end = time.perf_counter()

duration_ns = (end-start)
print(f"It took {duration_ns}s to calculate {len(looping_obstacles)}")
    




    

