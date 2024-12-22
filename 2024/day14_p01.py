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
- now both prize coords are padded to 10000000000000, Prize: X=8400, Y=5400 becomes Prize: X=10000000008400, Y=10000000005400

output: minimum amount of tokens spend to win all possible prizes
'''

import time
import re
import math

DIM_WIDTH = 101
DIM_HEIGHT = 103
MID_WIDTH = DIM_WIDTH//2
MID_HEIGHT = DIM_HEIGHT//2
SECONDS = 100

def quadrant_pos(robot_pos: tuple[int, int], middle: tuple[int, int]=(MID_WIDTH, MID_HEIGHT)) -> int:
    if robot_pos[0] > MID_WIDTH and robot_pos[1] < MID_HEIGHT:  # top-right
        return 1
    elif robot_pos[0] < MID_WIDTH and robot_pos[1] < MID_HEIGHT:  # top-left
        return 2
    elif robot_pos[0] < MID_WIDTH and robot_pos[1] > MID_HEIGHT:    # bottom-left
        return 3
    elif robot_pos[0] > MID_WIDTH and robot_pos[1] > MID_HEIGHT:    # bottom-right
        return 4
    else:
        return 0

def simulate_movement(robot_pos: tuple[int, int], robot_vel: tuple[int, int], seconds: int=SECONDS, dim: tuple[int, int]=(DIM_WIDTH, DIM_HEIGHT)) -> tuple[int, int]:
    new_pos = ((robot_pos[0] + robot_vel[0]*SECONDS) % DIM_WIDTH, (robot_pos[1] + robot_vel[1]*SECONDS) % DIM_HEIGHT)
    return new_pos

if '__main__' == __name__:
    with open('./data/day14.txt') as f:
        data = f.read().split('\n')
    quadrants = [0]*5

    start = time.perf_counter()
    for robot in data:
        pos_x, pos_y, vel_x, vel_y = list(map(int, re.findall(r'\-{0,1}\d{1,}', robot)))
        new_pos = simulate_movement((pos_x, pos_y), (vel_x, vel_y))
        in_quadrant = quadrant_pos(new_pos)
        quadrants[in_quadrant] += 1

    result = math.prod(quadrants[1:])
    end = time.perf_counter()

    duration_ns = (end-start)
    print(f"It took {duration_ns}s to calculate {result}")