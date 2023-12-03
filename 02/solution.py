"""

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

"""
def flatten(list):
    return [item for row in list for item in row]

def get_cube_counts(pulls):
    counts = {}
    cubes = flatten([x.split(',') for x in pulls.split(';')])
    for cube in cubes:
        _, number, color = cube.split(' ')
        counts[color] = max(counts.get(color,0), int(number))
    return counts


def is_valid_game(game, conditions):
    #print(game, conditions)
    for key in conditions:
        if game[key] > conditions[key]:
            #print(game[key], conditions[key])
            return False
    return True

def parse(game, conditions):
    id, pulls = game.split(':')
    counts = get_cube_counts(pulls)
    id = int(id[5:])
    if is_valid_game(counts, conditions):
        print(id)
        return id
    else:
        return 0

def get_power(counts):
    total = 1 
    for key in counts:
        total *= counts[key]
    return total


def get_valid_games(game_log, conditions):
    sum_of_valid_games = 0
    with open(game_log, 'r') as f:
        for game in f.readlines():
            sum_of_valid_games += parse(game.strip(), conditions)
    return sum_of_valid_games

def get_sum_of_game_powers(game_log):
    sum_of_powers = 0
    with open(game_log, 'r') as f:
        for game in f.readlines():
            counts = get_cube_counts(game.strip().split(':')[1])
            sum_of_powers += get_power(counts)
    return sum_of_powers



conditions = {
        "red": 12,
        "blue": 14,
        "green": 13,
        }
#print(get_valid_games('puzzle_1_input',conditions))
print(get_sum_of_game_powers('puzzle_1_input'))
