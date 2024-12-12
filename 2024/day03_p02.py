import time
import re

# Parse data
file = open('./data/day3.txt')
chars = file.read()

start = time.perf_counter()
pattern = r'mul\((\d*)\,(\d*)\)|(do\(\))|(don\'t\(\))'
matches = re.findall(pattern, chars)

result = 0
skip_instruction = False
for match in matches:
    if match[2]: skip_instruction = False   # matched do
    if match[3]: skip_instruction = True    # matched don't

    if not skip_instruction and match[0] and match[1]:
        result += int(match[0]) * int(match[1])
end = time.perf_counter()

duration_ns = (end-start)
print(f"It took {duration_ns}ns to calculate {result}")
