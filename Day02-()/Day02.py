# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from time import perf_counter

year, day = "2023", "02"
final = f"Day{day}_input.txt"
test = f"Day{day}_input_.txt"
filename = final


def run(d, y):
    print(f"\nResults from AoC {y} - Day {d}\n{'-' * 30}")

    start = perf_counter()
    print(f"Day {d} - Part 1: {solve_a()}")

    lap = perf_counter()
    print(f"Day {d} - Part 2: {solve_b()}")

    stop = perf_counter()

    print(f"\nPerformance\n{'-' * 30}")
    print(f"Part 1: {(lap - start) * 100:.6f} ms\nPart 2: {(stop - lap) * 100:.6f} ms")
    print(f"{'-' * 30}\nGesamt: {(stop - start) * 100:.6f} ms")


def prepare_input(file_name):
    with open(file_name) as f:
        content = f.read().split("\n")

    return content


def translate(text: str):
    new_text = ''
    for index, letter in enumerate(text):
        if letter in digits:
            new_text += letter
            continue
        for key in int_dict.keys():
            if text.find(key, index) == index:
                new_text += str(int_dict[key])
                break

    return new_text


def solve_a():

    return 0


def solve_b():
    return 0


run(day, year)
