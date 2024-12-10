def is_safe_with_bad_level(report):
    if is_safe(report): return True
    n = len(report)
    for i in range(n):
        # Check report with leaving out number at index i 
        if is_safe(report[0:i] + report[i+1:n]): return True
    return False

def is_safe(report):
    old_distance = report[0]-report[1]
    n = len(report)-1
    for i in range(n):
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

# Filter safe reports (one bad level allowed)
safe_reports = list(filter(is_safe_with_bad_level, reports))
print(len(safe_reports))

