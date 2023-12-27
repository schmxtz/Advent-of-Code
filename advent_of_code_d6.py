def main():
    data = open('data/day6.txt', 'r')

    times = []
    total_time = 0
    distances = []
    total_distance = 0
    # Parse input data
    for line in data:
        parsed_data = [int(num) for num in line.split()[1:]]
        if 'Time:' in line:
            total_time = int(line.strip('Time: ').replace(' ', ''))
            times = parsed_data
        if 'Distance:' in line:
            distances = parsed_data
            total_distance = int(line.strip('Distance: ').replace(' ', ''))

    # Part 1
    result = 1
    for time, distance in zip(times, distances):
        result *= count_winning_strats(time, distance)

    print(result)

    # Part 2
    print(count_winning_strats(total_time, total_distance))


def count_winning_strats(time, distance):
    count = 0
    for i in range(1, time):
        if calc_moved_dist(i, time) > distance:
            count += 1
    return count


def calc_moved_dist(time_button_hold, total_time):
    return time_button_hold * (total_time - time_button_hold)


if __name__ == '__main__':
    main()
