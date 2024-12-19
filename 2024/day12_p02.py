import time
from collections import deque

directions = [(0,1),(1,0),(0,-1),(-1,0)]
neighbor_pos = [(1,1),(-1,-1),(-1,1),(1,-1)]
def neighbor(data: list[list[int]], visited: set[int], pos: tuple[int, int]) -> list[tuple[int, int]]:
    next_pos = []
    for (row_off, col_off) in directions:
        (next_row, next_col) = pos[0]+row_off, pos[1]+col_off
        if 0 <= next_row < len(data) and 0 <= next_col < len(data[pos[0]]) and \
            data[pos[0]][pos[1]] == data[next_row][next_col]:
            next_pos.append((next_row, next_col))
    return next_pos

def sides(data, region: dict[int, list[tuple[int, int]]]) -> int:
    if len(region) <= 2:
        return 4
    side_count = 0
    for pos in region:
        if len(region[pos]) == 1:
            side_count += 2
        if len(region[pos]) == 2 and region[pos][0][0] != region[pos][1][0] and region[pos][0][1] != region[pos][1][1]: # corner
            side_count += 1
            (x0,y0) = pos
            (x1,y1) = region[pos][0]
            (x2,y2) = region[pos][1]
            if data[x0+(x1-x0)+(x2-x0)][y0+(y1-y0)+(y2-y0)] != data[x0][y0]: side_count += 1
        if len(region[pos]) == 3:
            (x0,y0) = pos
            on_row = list(filter(lambda x: x[0] == x0, region[pos]))
            (x1,y1), (x2,y2) = on_row if len(on_row) == 2 else list(filter(lambda x: x[1] == y0, region[pos]))
            on_col = list(filter(lambda x: x[1] == y0, region[pos]))
            (x3,y3) = on_col[0] if len(on_col) == 1 else list(filter(lambda x: x[0] == x0, region[pos]))[0]
            if data[x0+(x3-x0)+(x2-x0)][y0+(y3-y0)+(y2-y0)] != data[x0][y0]: side_count += 1
            if data[x0+(x3-x0)+(x1-x0)][y0+(y3-y0)+(y1-y0)] != data[x0][y0]: side_count += 1
        if len(region[pos]) == 4:
            (x0, y0) = pos
            for off in neighbor_pos:
                (x1, y1) = off
                if data[x0][y0] != data[x0+x1][y0+y1]: side_count += 1
    return side_count

if '__main__' == __name__:
    with open('./data/day12.txt') as f:
        data = [[ord(char) for char in row] for row in f.read().split('\n')]

    start = time.perf_counter()
    visited = set()
    starting_pos = []
    cost = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if (i, j) in visited:
                continue
            q = deque([(i, j)])
            region = {}
            visited.add((i, j))
            while q:
                pos = q.popleft()
                next_pos = neighbor(data, visited, pos)
                region[pos] = next_pos
                next_pos = list(filter(lambda x: x not in visited, next_pos))
                q.extend(next_pos)
                visited.update(next_pos)
            side_count = sides(data, region)
            cost += len(region.keys()) * side_count
    end = time.perf_counter()
    
    duration_ns = (end-start)
    print(f"It took {duration_ns}s to calculate {cost}")
