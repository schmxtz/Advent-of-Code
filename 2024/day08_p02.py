import time

def is_in_bounds(coord):
    return 0 <= coord[0] < MAX_ROW and 0 <= coord[1] < MAX_COL

data = open('./data/day8.txt').read().split('\n')
EMPTY_TOKEN = '.'
MAX_ROW = len(data)
MAX_COL = len(data[0])
antennas = {}
for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char != EMPTY_TOKEN: antennas[char] = antennas.get(char, set()) | set([(i, j)])

start = time.perf_counter()
antinodes = set()
for frequency in antennas:
    while len(antennas[frequency]) > 1:
        antenna = antennas[frequency].pop()
        for remaining_antenna in antennas[frequency]:
            antinodes.add(antenna)
            antinodes.add(remaining_antenna)
            deltax = antenna[0] - remaining_antenna[0]
            deltay = antenna[1] - remaining_antenna[1]
            i = 1
            left_antinode = (antenna[0]+(deltax*i), antenna[1]+(deltay*i))
            while is_in_bounds(left_antinode):
                antinodes.add(left_antinode)
                i += 1
                left_antinode = (antenna[0]+(deltax*i), antenna[1]+(deltay*i))
            i = 1
            right_antinode = (remaining_antenna[0]-(deltax*i), remaining_antenna[1]-(deltay*i))
            while is_in_bounds(right_antinode):
                antinodes.add(right_antinode)
                i += 1
                right_antinode = (remaining_antenna[0]-(deltax*i), remaining_antenna[1]-(deltay*i))
end = time.perf_counter()

duration_ns = (end-start)
print(f"It took {duration_ns}s to calculate {len(antinodes)}")