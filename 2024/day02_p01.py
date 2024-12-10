def is_safe(report):
    old_distance = report[0]-report[1]
    for i in range(len(report)-1):
        distance = report[i]-report[i+1]
        if not check_condition(old_distance, distance): return False
        old_distance = distance
    return True

def check_condition(old_distance, distance):
    return 1 <= abs(distance) <= 3 and distance*old_distance > 0


# Parse input
file = open('./data/day2.txt')
row_sep, col_sep = '\n', ' '
rows = file.read().split(row_sep)
reports = [[int(col) for col in row.split(col_sep)] for row in rows]

# Filter safe reports, count is solution
safe_reports = list(filter(is_safe, reports))
print(len(safe_reports))
