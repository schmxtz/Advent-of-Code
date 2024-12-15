import time
from operator import mul, add
from itertools import product

def is_correct(equation):
    if len(equation) == 2:
        return equation[0] == equation[1]
    result = equation[0]
    # -2 because the first number is the result and between each number is one operator -> 13 8 5 -> 13 = 8 + 5
    for perm in product([mul, add], repeat=len(equation)-2):
        temp = equation[1]
        for i in range(1, len(equation)-1):
            temp=perm[i-1](temp, equation[i+1])
            if temp > result:
                break
        if temp == result:
            return True
    return False

data = open('./data/day7.txt').read()
equations = [list(map(int, line.split(' '))) for line in data.replace(':', '').split('\n')]

start = time.perf_counter()
result = 0
for equation in equations:
    if is_correct(equation): result+=equation[0]
end = time.perf_counter()

duration_ns = (end-start)
print(f"It took {duration_ns}s to calculate {result}")