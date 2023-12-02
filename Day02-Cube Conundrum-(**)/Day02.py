# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helpers import run

year, day = "2023", "02"
final = f"Day{day}_input.txt"
test = f"Day{day}_input_.txt"
filename = final


def prepare_input(file_name):
    with open(file_name) as f:
        content = f.read().split("\n")

    return content


def solve_a():
    id_sum = 0
    possible = {'red': 12,
                'green': 13,
                'blue': 14}

    for game in puzzle:
        invalid = False
        game_id = int(game.split(':')[0].replace('Game ', ''))

        game_results = game.split(':')[1].strip().split(';')

        for turn in game_results:
            color_dict = {c.split()[1]: int(c.split()[0]) for c in turn.split(', ')}

            for key in possible.keys():
                if color_dict.get(key, 0) > possible[key]:
                    invalid = True
                    break

        if not invalid:
            id_sum += game_id

    return id_sum


def solve_b():
    id_sum = 0

    for game in puzzle:
        game_results = game.split(':')[1].strip().split(';')

        maxred, maxgreen, maxblue = 0, 0, 0
        for turn in game_results:
            color_dict = {c.split()[1]: int(c.split()[0]) for c in turn.split(', ')}

            maxred = max(maxred, color_dict.get("red", 0))
            maxgreen = max(maxgreen, color_dict.get("green", 0))
            maxblue = max(maxblue, color_dict.get("blue", 0))

        id_sum += maxred * maxblue * maxgreen

    return id_sum

puzzle = prepare_input(filename)
run(day, year, solve_a, solve_b)
