import time


def main():
    data = open('data/day9.txt', 'r')
    datasets = []

    for line in data:
        datasets.append([int(num) for num in line.split()])

    result = 0
    result_p2 = 0
    for sequence in datasets:
        temp_sequences = [sequence]
        while any(num != 0 for num in temp_sequences[-1]):
            temp_sequence = []
            for (left, right) in zip(temp_sequences[-1][0:], temp_sequences[-1][1:]):
                temp_sequence.append(right - left)
            temp_sequences.append(temp_sequence)

        next_step = 0
        prev_step = temp_sequences[-2][0]
        for index in range(len(temp_sequences) - 2, -1, -1):
            next_step += temp_sequences[index][-1]
            prev_step = temp_sequences[index][0] - temp_sequences[index + 1][0]
            temp_sequences[index].insert(0, prev_step)
        result_p2 += prev_step
        result += next_step
    print(result, result_p2)


if __name__ == '__main__':
    main()
