from utils.util import get_input
import itertools
import re
from functools import cache

def main() -> None:
    file_input = get_input("day12/input.txt")
    print(f"Part one: {part_one(file_input)}")
    print(f"Part two: {part_two(file_input)}")

def part_one(input: list[str]) -> int:
    total_count = 0
    for line in input:
        conditions, group_sizes_str = line.split()
        group_sizes = [int(size) for size in group_sizes_str.split(",")]

        valid_permutations = filter(lambda s: get_valid_permutation(s, group_sizes), generate_permutations(conditions))
        total_count += sum(1 for _ in valid_permutations)

    return total_count

def part_two(input:list[str]) -> int:
    total_count = 0
    for line in input:
        conditions, group_sizes = line.split()
        conditions = unfold_conditions(conditions)
        group_sizes = unfold_group_sizes(group_sizes)
        total_count += count_valid_permutations(conditions, group_sizes)
    return total_count

def separate_groups(input: str) -> list[str]:
    pattern = re.compile(r'[?#]+|\.+')
    return pattern.findall(input)

def generate_permutations(string):
    question_mark_indices = [i for i, char in enumerate(string) if char == '?']
    for replacement in itertools.product(*(['.#'] * len(question_mark_indices))):
        new_string = list(string)
        for index, char in zip(question_mark_indices, replacement):
            new_string[index] = char
        yield ''.join(new_string)

def get_valid_permutation(full_string: str, group_sizes: list[int]) -> bool:
    groups = re.findall(r'[#]+', full_string)
    if len(groups) != len(group_sizes):
        return False
    for i, group in enumerate(groups):
        if len(group) != group_sizes[i]:
            return False
    return True

def unfold_conditions(line:str) -> str:
    return ((line+"?") * 5)

def unfold_group_sizes(group_sizes:str) -> tuple[int]:
    return tuple(int(size) for size in group_sizes.split(",")*5)

@cache
def count_valid_permutations(string, group_sizes, current_group_count=0):
    if not string:
        return not group_sizes and current_group_count == 0

    total_count = 0
    possible_chars = determine_possible_chars(string[0])

    for char in possible_chars:
        if char == "#":
            total_count += count_valid_permutations(string[1:], group_sizes, current_group_count + 1)
        else:
            total_count += handle_non_group_char(string, group_sizes, current_group_count)

    return total_count

def determine_possible_chars(char):
    return [".", "#"] if char == "?" else [char]

def handle_non_group_char(string, group_sizes, current_group_count):
    if current_group_count:
        if group_sizes and group_sizes[0] == current_group_count:
            return count_valid_permutations(string[1:], group_sizes[1:])
        return 0
    return count_valid_permutations(string[1:], group_sizes)

if __name__ == "__main__":
    main()
