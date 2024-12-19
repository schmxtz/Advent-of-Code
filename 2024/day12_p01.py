import time
from collections import deque

directions = [(0,1),(1,0),(0,-1),(-1,0)]
def neighbor(data: list[list[int]], visited: set[int], pos: tuple[int, int]) -> list[tuple[int, int]]:
    next_pos = []
    for (row_off, col_off) in directions:
        (next_row, next_col) = pos[0]+row_off, pos[1]+col_off
        if 0 <= next_row < len(data) and 0 <= next_col < len(data[pos[0]]) and \
            data[pos[0]][pos[1]] == data[next_row][next_col]:
            next_pos.append((next_row, next_col))
    return next_pos

def circumference(region: dict[int, list[tuple[int, int]]]) -> int:
    circ = 0
    for pos in region:
        circ += (4-len(region[pos]))
    return circ

if '__main__' == __name__:
    with open('./data/day12.txt') as f:
        data = [[ord(char) for char in row] for row in f.read().split('\n')]
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
            cost += len(region.keys()) * circumference(region)
    print(cost)
