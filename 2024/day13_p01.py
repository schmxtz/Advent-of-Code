'''
example input:
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279

conditions:
- it costs 3 tokens to move A, 1 token to move B
- to get prize, claw needs to be directly above its position
- each button can only be pressed no more than 100 times

output: minimum amount of tokens spend to win all possible prizes
result: (80*3 + 40*1) + (38*3 + 86*1) = 480 tokens (first machine and third machine)
'''

import time
import re
import math

def is_solution(a_x, a_y, b_x, b_y, p_x, p_y, a_count, b_count):
    if 0 <= a_count <= 100 and 0 <= b_count <= 100 and a_x*a_count+b_x*b_count == p_x and a_y*a_count+b_y*b_count == p_y:
        return a_count, b_count
    return 0, 0

def solve_equation(a_x, a_y, b_x, b_y, p_x, p_y):
    ratio = b_x/b_y
    a_count = (p_x-p_y*ratio)/(a_x-a_y*ratio)
    b_count = (p_y-a_y*a_count)/b_y
    return is_solution(a_x, a_y, b_x, b_y, p_x, p_y, round(a_count), round(b_count))

if '__main__' == __name__:
    with open('./data/day13.txt') as f:
        data = f.read().split('\n\n')
    
    start = time.perf_counter()
    cost = 0
    for machine in data:
        a_x, a_y, b_x, b_y, p_x, p_y = list(map(int, re.findall(r'\d{1,}', machine)))
        a_count, b_count = solve_equation(a_x, a_y, b_x, b_y, p_x, p_y)
        cost += 3*a_count + b_count
    end = time.perf_counter()
    
    duration_ns = (end-start)
    print(f"It took {duration_ns}s to calculate {cost}")