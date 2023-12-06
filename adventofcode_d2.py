import requests

# example line
# Game 15: 8 blue, 3 green, 15 red; 13 red, 10 blue; 2 red

# Get input
session_cookie = {'session': 'your_sessiom_cookie'}
input_req = requests.get(url='https://adventofcode.com/2023/day/2/input', cookies=session_cookie)

is_valid_game = True
game_ctr = 1
sum_id = 0
sum_power = 0
max_cubes = {'red': 0, 'green': 0, 'blue': 0}

games = input_req.text.split('\n')

for game in games:
    last_num_index = 0
    count = 0
    for i in range(1, len(game)):
        # remember the index of the first cube count digit
        if game[i].isnumeric() and not game[i-1].isnumeric():
            last_num_index = i
        # do the check for the red cubes
        elif game[i-1:i+1] == ' r':
            # Parse the count as an integer, -1 because there is a space between count and color
            count = int(game[last_num_index:i-1])
            max_cubes['red'] = max(max_cubes['red'], count)
            # Skip this game if condition is not met
            if count > 12:
                is_valid_game = False
        elif game[i-1:i+1] == ' g':
            # Parse the count as an integer, -1 because there is a space between count and color
            count = int(game[last_num_index:i-1])
            max_cubes['green'] = max(max_cubes['green'], count)
            # Skip this game if condition is not met
            if count > 13:
                is_valid_game = False
        elif game[i-1:i+1] == ' b':
            # Parse the count as an integer, -1 because there is a space between count and color
            count = int(game[last_num_index:i-1])
            max_cubes['blue'] = max(max_cubes['blue'], count)
            # Skip this game if condition is not met
            if count > 14:
                is_valid_game = False
        else:
            continue

    # Check if game was valid and update the sum
    if is_valid_game and game_ctr <= 100:
        sum_id += game_ctr

    mult = max_cubes['red'] * max_cubes['green'] * max_cubes['blue']
    sum_power += mult

    # Reset Flags
    is_valid_game = True
    game_ctr += 1
    max_cubes = {'red': 0, 'green': 0, 'blue': 0}

print(sum_id)
print(sum_power)

