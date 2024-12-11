import time

# Parse input
file = open('./data/day1.txt')
row_sep, col_sep = '\n', '   '
rows = file.read().split(row_sep)
first_col = [int(row.split(col_sep)[0]) for row in rows]
second_col = [int(row.split(col_sep)[1]) for row in rows]

# Similarity is the sum of all numbers in the first column and their count of occurences in the second column
start = time.perf_counter()
similarity = 0
for number in first_col:
    similarity += number * second_col.count(number)
end = time.perf_counter()

duration_ns = (end-start)
print(f"It took {duration_ns}ns to calculate {similarity}")

# <------------------------------------------------------------------------------------------------------------->
# Using count is very primitive, instead we can iterate the second column once and count the number of occurences
start = time.perf_counter()
similarity = 0
first_col.sort()
second_col.sort()

# Count occurences
occurences = {}
for num in second_col:
    occurences[num] = occurences.get(num, 0) + 1


for num in first_col:
    similarity += occurences.get(num, 0) * num
end = time.perf_counter()

optimized_duration_ns = (end-start)
duration_ratio = (duration_ns/optimized_duration_ns)

print(f"It took {optimized_duration_ns}ns to calculate {similarity}")
print(f"The optimized approach was ~{int(duration_ratio)}x faster")



    