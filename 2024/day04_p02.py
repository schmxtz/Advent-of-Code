import time
 
'''
M_M  M_S  S_M  S_S 
_A_  _A_  _A_  _A_ 
S_S  M_S  S_M  M_M
'''
matches = set(['MMASS', 'MSAMS', 'SMASM', 'SSAMM'])
offsets = [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)]

def get_cross(data, row, column):
    return ''.join(data[row+offset[0]][column+offset[1]] for offset in offsets)

def is_cross(data, row, column):
    return get_cross(data, row, column) in matches

file = open('./data/day4.txt')
lines = file.read().split('\n')

start = time.perf_counter()
cross_count = 0
for row in range (len(lines)-2):
    for column in range(len(lines[row])-2):
        if is_cross(lines, row, column): cross_count+=1
end = time.perf_counter()

duration_ns = (end-start)
print(f"It took {duration_ns}ns to calculate {cross_count}")
        

