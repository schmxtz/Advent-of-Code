from collections import deque
import time

offsets = [(-1,0),(1,0),(0,1),(0,-1)]
def get_next_positions(data, visited, pos):
    next_positions = []
    for (row_off, col_off) in offsets:
        next_row, next_col = pos[0]+row_off, pos[1]+col_off
        if 0 <= next_row < len(data) and 0 <= next_col < len(data[next_row]) and \
            (next_row, next_col) not in visited and \
            1 == data[next_row][next_col] - data[pos[0]][pos[1]]:
            next_positions.append((next_row, next_col))
    return next_positions

if '__main__' == __name__:
    with open('./data/day10.txt') as file:
        data = file.read()
    data = [[int(col) for col in row] for row in data.split('\n')]
    trailheads = [(row_index, col_index) for row_index, row in enumerate(data) for col_index, col in enumerate(row) if 0 == col]
    
    start = time.perf_counter()
    # Move from trailhead away until you find a trailhead end
    score = 0
    for trailhead in trailheads:
        visited = set([trailhead])
        path = deque([trailhead])   
        while path:
            pos = path.popleft()
            if 9 == data[pos[0]][pos[1]]:
                score += 1
            else:
                next_positions = get_next_positions(data, visited, pos)
                path.extend(next_positions)
                visited.add(pos)
    end = time.perf_counter()
    print(score)
    
    duration_ns = (end-start)
    print(f"It took {duration_ns}s to calculate {score}")



