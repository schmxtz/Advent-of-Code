# Part 1: Parse all numbers that are in direct contact with a symbol and sum them up
# Input: "467..114..
#         ...*......"
# Output: 467 is in direct contact, 114 is not

# Part 2: Store the highest count of cubes for each color, build the product of their counts and sum them
# Input: "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
# Output: 4 * 2 * 6 = 48 (4 red, 2 red, 6 blue)


def main():
    data = open('data/day3.txt', 'r')
    # Numbers will be saved as (value, column, length) tuples in their designated array indexed by row
    numbers = []
    # Symbols will be saved as (symbol, column) tuples in their designated array indexed by row
    symbols = []

    for (row, line) in enumerate(data):
        numbers.append([])
        symbols.append([])
        number = []
        length = 0
        i = 0
        while i < len(line):
            while line[i].isdigit():
                number.append(line[i])
                length += 1
                i += 1
            if length != 0:
                numbers[row].append((number_as_char_list(number), i - length, length))
                length = 0
                number = []
            if line[i] not in ['.', '\n']:
                symbols[row].append((line[i], i))
            i += 1

    # Part 1
    result = 0
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            num = numbers[i][j]
            if check_symbol_in_vicinity(i, num[1], num[2], symbols):
                result += num[0]
    print(result)

    # Part 2
    result = 0
    # Save checked symbols to avoid duplicates
    checked_symbols = []
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            num_one = numbers[i][j]
            symbol = check_symbol_in_vicinity(i, num_one[1], num_one[2], symbols, '*')
            if symbol:
                for k in range(max(symbol[1] - 1, 0), min(symbol[1] + 1, len(numbers)) + 1):
                    for l in range(len(numbers[k])):
                        num_two = numbers[k][l]
                        if symbol == check_symbol_in_vicinity(i, num_two[1], num_two[2], symbols, '*') and symbol not in checked_symbols and num_one != num_two:
                            result += num_one[0] * num_two[0]
                            checked_symbols.append(symbol)
    print(result)


# Returns (symbol, row, column) tuple if it's in the close vicinity, empty tuple else
def check_symbol_in_vicinity(number_row, number_column, number_length, symbols, filter_symbol='') -> (str, int, int):
    upper_row_bound = max(0, number_row - 1)
    lower_row_bound = min(number_row + 1, len(symbols) - 1) + 1
    left_column_bound = number_column - 1
    right_column_bound = number_column + number_length + 1
    for i in range(upper_row_bound, lower_row_bound):
        for symbol in symbols[i]:
            if symbol[1] in range(left_column_bound, right_column_bound):
                if not filter_symbol:
                    return symbol[0], i, symbol[1]
                if filter_symbol == symbol[0]:
                    return symbol[0], i, symbol[1]
    return ()


def number_as_char_list(number) -> int:
    return int(''.join(number))


if __name__ == '__main__':
    main()
