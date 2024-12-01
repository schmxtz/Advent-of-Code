# Part 1: Extract left-most and right-most digit from string and sum their decimal representation.
# Input: "five1four4sixtwo"
# Output: 14

# Part 2: Extract left-most and right-most digit from string and sum their decimal representation, digit might occur
#         in its written form 1 = one.
# Input: "five1four4sixtwo"
# Output: 52

def main():
    data = open('data/day1.txt', 'r')

    # Part 1
    result = 0
    for line in data:
        left_digit = -1
        right_digit = -1
        line_length = len(line)
        for i in range(line_length):
            # left-most digit check
            if line[i].isdigit() and left_digit == -1:
                left_digit = int(line[i])
            # right-most digit check
            if line[line_length - i - 1].isdigit() and right_digit == -1:
                right_digit = int(line[line_length - i - 1])
            if left_digit != -1 and right_digit != -1:
                break
        # left_digit = 4, right_digit = 5, decimal representation: 45 = 4 * 10 + 5
        result += (left_digit * 10) + right_digit
    data.close()
    print('Part 1:', result)

    data = open('data/day1.txt', 'r')

    # Part 2
    digits = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    result = 0
    for line in data:
        left_digit = -1
        right_digit = -1
        line_length = len(line)
        for i in range(line_length):
            # left-most digit check
            if left_digit == -1 and line[i].isdigit():
                left_digit = int(line[i])
            # left-most digit as word check
            for j in range(3, 6):
                if left_digit == -1 and i + j <= line_length and line[i:i+j] in digits:
                    left_digit = digits[line[i:i+j]]
                    break

            # right-most digit check
            if right_digit == -1 and line[line_length - i - 1].isdigit():
                right_digit = int(line[line_length - i - 1])
            # right-most digit as word check
            for j in range(3, 6):
                if right_digit == -1 and line_length-i-j >= 0 and line[line_length-i-j: line_length-i] in digits:
                    right_digit = digits[line[line_length-i-j: line_length-i]]
                    break
        result += (left_digit * 10) + right_digit
    data.close()

    print('Part 2:', result)


if __name__ == '__main__':
    main()
