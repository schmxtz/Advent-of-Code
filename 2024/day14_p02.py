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
SECONDS = 100

def simulate_movement(robot_pos: tuple[int, int], robot_vel: tuple[int, int], seconds: int=SECONDS, dim: tuple[int, int]=(DIM_WIDTH, DIM_HEIGHT)) -> tuple[int, int]:
    new_pos = ((robot_pos[0] + robot_vel[0]*seconds) % dim[0], (robot_pos[1] + robot_vel[1]*seconds) % dim[1])
    return new_pos

def print_robos_pos(positions: set[tuple[int, int]]):
    image = [[' ' for _ in range(DIM_WIDTH)]+['\n'] for _ in range(DIM_HEIGHT)]   # init
    for pos in positions:
        image[pos[1]][pos[0]] = '#' # draw
    image = [c for r in image for c in r]   # flatten
    print(''.join(image))

if '__main__' == __name__:
    with open('./data/day14.txt') as f:
        data = f.read().split('\n')
    
    old_pos = [list(map(int, re.findall(r'\-{0,1}\d{1,}', robot))) for robot in data]

    for i in range(10000):
        new_pos = []
        for pos in old_pos:
            pos_x, pos_y, vel_x, vel_y = pos
            new_pos.append(simulate_movement((pos_x, pos_y), (vel_x, vel_y), i))
        if (i-187) % 101 == 0:
            print_robos_pos(new_pos)
            print(f'Seconds: {i}')
            input('')

            #57, 86, 160, 187, 288, 389, 490
