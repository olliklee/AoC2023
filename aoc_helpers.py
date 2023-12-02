from time import perf_counter

def run(d: str, y: str, func_a, func_b):
    """ This function is specially for the adventofcode project.
    The parameters are:
    Day and year as String,
    Two functions for part1 and part2.
    It prints out the results of the two functions and the time it took to solve it."""
    dotted_line = '-' * 38
    print(f"\nResults from AoC {y} - Day {d}\n{dotted_line}")

    start = perf_counter()
    print(f"Day {d} - Part 1: {func_a()}")
    lap = perf_counter()
    print(f"Day {d} - Part 2: {func_b()}")
    stop = perf_counter()

    print(f"\nPerformance\n{dotted_line}")
    print(f"Part 1: {(lap - start) * 100:.6f} ms"
          f"Part 2: {(stop - lap) * 100:.6f} ms")
    print(f"{dotted_line}\nGesamt: {(stop - start) * 100:.6f} ms")

