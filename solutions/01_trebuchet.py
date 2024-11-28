"""
This is a solution to day 1 of AoC 2023

Challenge title: Trebuchet?!
Challenge link : https://adventofcode.com/2023/day/1

Solution: https://github.com/florianbuetow/advent_of_code_2023/blob/main/solutions/01_trebuchet.py
Dialogue: https://github.com/florianbuetow/advent_of_code_2023/blob/main/dialogues/01_trebuchet.ipynb

Time complexity: O(n * m)
                 where n = # of lines in the input, m = average line length
Space complexity: O(1)

"""

from aocd import get_data
inp = get_data(day=1, year=2023)

total = 0
for line in inp.splitlines():
    first_digit = last_digit = 0
    for chr in line:
        if chr.isdigit():
            if not first_digit:
                first_digit = chr
            last_digit = chr
    number = 10 * int(first_digit) + int(last_digit)
    total += number

print(f"The answer is: {total}")
