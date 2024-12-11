import time

file = open('./data/day3.txt')
chars = file.read()

# Build own state machine with input mapping to next state
start = time.perf_counter()
left_number_state = {'0': 4, '1': 4, '2': 4, '3': 4, '4': 4, '5': 4, '6': 4, '7': 4, '8': 4, '9': 4, ',': 5}
right_number_state = {'0': 5, '1': 5, '2': 5, '3': 5, '4': 5, '5': 5, '6': 5, '7': 5, '8': 5, '9': 5, ')': 6} 
states = [{'m': 1}, {'u': 2}, {'l': 3}, {'(': 4}, left_number_state, right_number_state]

cur_state = 0
operand_i = ''
operand_j = ''

result = 0
for char in chars:
    if cur_state == 6:
        if operand_i and operand_j:
            result += int(operand_i) * int(operand_j)
        cur_state = 0
        operand_i = ''
        operand_j = ''
    elif cur_state == 4 and char.isnumeric():
        operand_i += char
    elif cur_state == 5 and char.isnumeric():
        operand_j += char
    else:
        pass
    if char in states[cur_state]:
        cur_state = states[cur_state][char]
    else:
        operand_i = ''
        operand_j = ''
        cur_state = 0
end = time.perf_counter()

duration_ns = (end-start)
print(f"It took {duration_ns}ns to calculate {result}")

# <------------------------------------------------------------------------------------------------------------->
# I'm not sure if my own state-machine is performant, so I'll compare it to a regex
import re

start = time.perf_counter()
pattern = r'mul\((\d*)\,(\d*)\)'
matches = re.findall(pattern, chars)
result = 0

result = sum([int(match[0])*int(match[1]) for match in matches])
end = time.perf_counter()

regex_duration_ns = (end-start)
duration_ratio = (duration_ns/regex_duration_ns)

print(f"It took {regex_duration_ns}ns to calculate {result}")
print(f"The regex approach was ~{int(duration_ratio)}x faster") # my benchmark: regex ~7x faster..., will be using regex from now on


