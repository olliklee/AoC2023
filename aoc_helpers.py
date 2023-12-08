from time import perf_counter

def run_puzzles(d: str, y: str, func_a, func_b):
    """ This function is specially for the adventofcode project.
    The parameters are:
    Day and year as String,
    Two functions for part1 and part2.
    It prints out the results of the two functions and the time it took to solve it."""
    dotted_line = '-' * 26
    print(f"{dotted_line}\n"
          f"|   AoC {y} - Day {d}    |\n"
          f"{dotted_line}")

    start = perf_counter()
    print(f"|  Part 1: {func_a():<14.0f}|")
    lap = perf_counter()
    print(f"|  Part 2: {func_b():<14.0f}|")
    stop = perf_counter()

    print(f"{dotted_line}\n"
          f"|      Performance       |\n"
          f"{dotted_line}\n"
          f"|  Part 1: {(lap - start) * 100:>7.4f} ms    |\n"
          f"|  Part 2: {(stop - lap) * 100:>7.4f} ms    |\n"
          f"{dotted_line}\n"
          f"|  Gesamt: {(stop - start) * 100:>7.4f} ms    |\n"
          f"{dotted_line}\n")

'''

-   AoC 2023 - Day 08    -
--------------------------
- Part 1: 11567   -
- Part 2: 9858474970153  -
--------------------------
Performance
--------------------------
-    Part 1:  0.09455 ms - 
-    Part 2:  3.81688 ms -
----------------------------------------
-     Gesamt: 3.91143 ms -
--------------------------

'''
