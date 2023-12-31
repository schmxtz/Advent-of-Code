import queue


def main():
    data = open('data/day4.txt', 'r')

    result_pone = 0
    result_ptwo = 0
    intersec_count = {}
    for (index, line) in enumerate(data):
        game = line[line.find(': ') + 1:]

        # Part 1
        winning_nums, owned_nums = game.split('|')
        winning_nums = parse_list(winning_nums)
        owned_nums = parse_list(owned_nums)
        num_intersec = winning_nums.intersection(owned_nums)
        if len(num_intersec):
            result_pone += 2**(len(num_intersec) - 1)

        # Part 2
        intersec_count[index + 1] = len(num_intersec)

    # Init FIFO Queue
    q = queue.Queue()
    [q.put(i) for i in range(1, len(intersec_count) + 1)]
    while not q.empty():
        # For each card, increment result
        num = q.get()
        result_ptwo += 1

        # Range: num + 1, because we need the cards after the current one
        # Range: num + intersec_count[num] + 1, one more plus 1 because the upper bound is exclusive
        lower_bound = num + 1
        upper_bound = min(num + intersec_count[num] + 1, len(intersec_count) + 1)
        for i in range(lower_bound, upper_bound):
            q.put(i)

    print(int(result_pone))
    print(int(result_ptwo))


def parse_list(list_str) -> set:
    return set(int(num) for num in list_str.split())


if __name__ == '__main__':
    main()
