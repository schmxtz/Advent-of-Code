import time
from itertools import product
from operator import mul, add


def concat(op_left, op_right):
    return int(str(op_left)+str(op_right))

def calc_equation(equation, ops, result):
    temp = equation[0]
    for i in range(0, len(equation)-1):
        temp=ops[i](temp, equation[i+1])
        if temp > result: break
    return temp

def is_correct(equation):
    if len(equation) == 2:
        return equation[0] == equation[1]
    result = equation[0]
    for ops in product(possible_ops, repeat=len(equation)-2):
        if result == calc_equation(equation[1:], ops, result): return True
    return False
    
possible_ops = [mul, add, concat]

data = open('./data/day7.txt').read()
equations = [list(map(int, line.split(' '))) for line in data.replace(':', '').split('\n')]

start = time.perf_counter()
result = 0
for equation in equations:
    if is_correct(equation): result+=equation[0]
end = time.perf_counter()

duration_ns = (end-start)
print(f"It took {duration_ns}s to calculate {result}")