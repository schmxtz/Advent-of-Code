from functools import reduce
from math import lcm


def main():
    data = open('data/day8.txt', 'r')

    instructions = []
    node_mapping = {}
    for index, line in enumerate(data):
        if index == 0:
            for instruction in line:
                if instruction == 'L':
                    instructions.append(0)
                    continue
                if instruction == 'R':
                    instructions.append(1)
                    continue

        if index > 1:
            node, mapping = line.replace(' ', '').replace('\n', '').split('=')
            node_mapping[node] = tuple([node for node in mapping.replace('(', '').replace(')', '').split(',')])

    steps = 0
    destination_node = 'AAA'
    while destination_node != 'ZZZ':
        destination_node = node_mapping[destination_node][instructions[steps % len(instructions)]]
        steps += 1
    print(steps)

    # steps = 0
    start_nodes = [node for node in node_mapping if node[2] == 'A']
    # while not all(start_node[2] == 'Z' for start_node in start_nodes):
    #     for index, node in enumerate(start_nodes):
    #         start_nodes[index] = node_mapping[start_nodes[index]][instructions[steps % len(instructions)]]
    #     steps += 1
    # print(steps)

    # LCM solution
    step_counts = []
    for start_node in start_nodes:
        steps = 0
        destination_node = start_node
        while destination_node[2] != 'Z':
            destination_node = node_mapping[destination_node][instructions[steps % len(instructions)]]
            steps += 1
        step_counts.append(steps)
    print(reduce(lcm, step_counts))


if __name__ == '__main__':
    main()
