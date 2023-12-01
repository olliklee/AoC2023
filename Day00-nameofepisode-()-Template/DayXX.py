# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helpers import run

year, day = "YYYY", "XX"
final = f"Day{day}_input.txt"
test = f"Day{day}_input_.txt"
filename = final


def prepare_input(file_name):
    with open(file_name) as f:
        content = f.read().split("\n")

    return content


def solve_a():
    return 0


def solve_b():
    return 0


run(day, year, solve_a, solve_b)
