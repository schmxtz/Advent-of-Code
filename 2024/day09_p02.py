import time

data = open('./data/day9.txt').read()

files = []
free_spaces = []
index = 0
for i in range(len(data)):
    if i % 2 == 0:
        files.append((i//2, int(data[i]), index))    # ID, SIZE, INDEX
    else:
        free_spaces.append((int(data[i]), index))    # SIZE, INDEX
    index += int(data[i])

start = time.perf_counter()
right = len(files)-1
result = 0
# Iterate over files in reverse
while right >= 0:
    # Find next free space
    left = 0
    was_moved = False
    while free_spaces[left][1] < files[right][2]:
        if free_spaces[left][0] >= files[right][1]:
            result += sum(range(free_spaces[left][1], free_spaces[left][1]+files[right][1]))*files[right][0]
            free_spaces[left] = (free_spaces[left][0]-files[right][1], free_spaces[left][1]+files[right][1])
            free_spaces.append((files[right][1], files[right][2]))
            free_spaces.sort(key=lambda x: x[1])
            was_moved = True
            break
        left += 1
    if not was_moved:
        result += sum(range(files[right][2], files[right][2]+files[right][1]))*files[right][0]
    right -= 1
end = time.perf_counter()

duration_ns = (end-start)
print(f"It took {duration_ns}s to calculate {result}")