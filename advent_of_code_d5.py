def main():
    data = open('data/day5.txt', 'r')

    mappings = []
    seeds = []
    mapping_ctr = -1

    # Parse input data
    for line in data:
        if line.startswith('seeds:'):
            seeds = [int(num) for num in line[6:].split()]
        elif 'map:' in line:
            mappings.append([])
            mapping_ctr += 1
        elif line[0].isdigit():
            destination, source, range_length = [int(num) for num in line.split()]
            mappings[mapping_ctr].append((source, source + range_length, destination, destination + range_length))

    # Part 1
    # Map the seed with each mapping to its location
    locations = []
    for seed in seeds:
        number = seed
        for mapping in mappings:
            for (source_start, source_end, dest_start, dest_end) in mapping:
                if number in range(source_start, source_end):
                    number = dest_start + (number - source_start)
                    break
        locations.append(number)

    print(min(locations))

    # Part 2
    # Do reverse lookup from lowest location and check if its a seed
    mappings.reverse()
    minimum_found = False
    for i in range(0, max(mappings[-1])[1]):
        location = i
        if not minimum_found:
            number = i
            for mapping in mappings:
                for (source_start, source_end, dest_start, dest_end) in mapping:
                    if number in range(dest_start, dest_end):
                        number = source_start + (number - dest_start)
                        break
            for (seed, seed_range) in zip(seeds[0::2], seeds[1::2]):
                if number in range(seed, seed + seed_range):
                    print(location)
                    minimum_found = True
                    break
        else:
            break


if __name__ == '__main__':
    main()
