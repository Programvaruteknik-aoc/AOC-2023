from utils.util import get_input
import itertools
import re

def main() -> None:
    file_input = get_input("day12/input.txt")
    print(f"Part one: {part_one(file_input)}")
    print(f"Part two: {part_two(file_input)}")

def part_one(input: list[str]) -> int:
    total_count = 0
    for line in input:
        conditions, group_sizes_str = line.split()
        group_sizes = [int(size) for size in group_sizes_str.split(",")]

        valid_permutations = filter(lambda s: validate_permutation(s, group_sizes), generate_permutations(conditions))
        total_count += sum(1 for _ in valid_permutations)

    return total_count

def part_two(input:list[str]) -> int:
    return -1

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

def validate_permutation(full_string: str, group_sizes: list[int]) -> bool:
    groups = re.findall(r'[#]+', full_string)
    if len(groups) != len(group_sizes):
        return False
    for i, group in enumerate(groups):
        if len(group) != group_sizes[i]:
            return False
    return True

def unfold_row(line:str) -> str:
    print((line+"?") * 5)
    return (line+"?") * 5

if __name__ == "__main__":
    main()
