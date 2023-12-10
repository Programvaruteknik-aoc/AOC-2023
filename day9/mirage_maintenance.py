from utils.util import get_input
import re
import math
import itertools

def main() -> None:
    file_input = get_input("day9/input.txt")
    print(f"Part one: {part_one(file_input)}")
    print(f"Part two: {part_two(file_input)}")

def part_one(input:list[str]) -> int:
    return sum([predict_next_value(line) for line in input])

def part_two(input:list[str]) -> int:
    return 0

def predict_next_value(history_line:str) -> int:
    history: list[int] = parse_numbers(history_line)
    expanded_history:list[list[int]] = [history]
    while not all(value == 0 for value in expanded_history[-1]):
        expanded_history.append(create_next_sequence(expanded_history[-1]))
    return extrapolate(expanded_history)

def parse_numbers(history_line:str) -> list[int]:
    return [int(value) for value in history_line.split(" ")]

def create_next_sequence(values:list[int]) -> list[int]:
    new_values = []
    for i in range(1, len(values)):
        new_values.append(calculate_difference(values[i-1], values[i]))
    return new_values

def extrapolate(history_sequences:list[list[int]]) -> int:
    temp_values = 0
    for i in range(len(history_sequences), 0, -1):
        prev_last = history_sequences[i-1][-1]
        temp_values = prev_last + temp_values
    return temp_values

def calculate_difference(first:int, second:int) -> int:
    return second - first

if __name__ == "__main__":
    main()