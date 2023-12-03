# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helpers import run_puzzles

year, day = "YYYY", "XX"
final = f"Day{day}_input.txt"
test = f"Day{day}_input_.txt"
filename = test


def prepare_input(file_name):
    with open(file_name) as f:
        content = f.read().split("\n")

    return content


def solve_a():
    return 0


def solve_b():
    return 0

### ----------- Start ------------- ###

run_puzzles(day, year, solve_a, solve_b)
