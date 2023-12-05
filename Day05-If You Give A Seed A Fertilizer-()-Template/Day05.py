# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helpers import run_puzzles
from re import findall

year, day = "2023", "05"
final = f"Day{day}_input.txt"
test = f"Day{day}_input_.txt"
filename = test


def prepare_input():
    with open(filename) as f:
        content = f.read().split("\n\n")

    seeds = findall("\d+", content[0])
    maps = {block: list(map(int, findall("\d+", content[block]))) for block in range(1, len(content))}
    maps_ranges = {}
    for single_map in maps.keys():
        maps_ranges[single_map] = []
        transform = maps[single_map]
        for j in range(0, len(transform), 3):
            offset = transform[j+2]
            dest = range(transform[j], transform[j]+offset)
            src = range(transform[j+1], transform[j+1] + offset)
            maps_ranges[single_map].append((src,dest))

    return seeds, maps_ranges



def solve_a():
    for seed in my_seeds:
        spot = int(seed)
        for category in my_maps.values():
            for my_range in category:
                if spot in list(my_range[0]):
                    index = my_range[0].find(spot)
                    print(index)
                    spot = my_range[1][index]
                    print(spot)
                    break



    return 0


def solve_b():
    return 0

### ----------- Start ------------- ###

my_seeds, my_maps = prepare_input()
run_puzzles(day, year, solve_a, solve_b)
