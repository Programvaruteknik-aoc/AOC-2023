from utils.util import get_input
import numpy as np

def main() -> None:
    file_input = get_input("day13/input.txt")
    print(f"Part one: {part_one(file_input)}")
    print(f"Part two: {part_two(file_input)}")

def part_one(input: list[str]) -> int:
    patterns = extract_patterns(input)
    return sum(find_real_vertical_mirror(pattern, find_possible_vertical_mirrors) for pattern in patterns) \
           + sum(find_real_horizontal_mirror(pattern, find_possible_horizontal_mirrors) for pattern in patterns) * 100

def part_two(input: list[str]) -> int:
    patterns = extract_patterns(input)
    total = 0
    for pattern in patterns:
        pattern_grid = np.array([list(row) for row in pattern])
        horizontal_score = 100 * calculate_mirror_location(pattern_grid, is_smudged=True)
        vertical_score = calculate_mirror_location(pattern_grid.T, is_smudged=True)
        total += horizontal_score or vertical_score
    return total

def extract_patterns(input: list[str]) -> list[list[str]]:
    patterns, pattern = [], []
    for line in input:
        if line == "":
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(line)
    patterns.append(pattern)
    return patterns

def find_possible_vertical_mirrors(pattern: list[str]) -> list[int]:
    possible_mirrors = []
    num_rows, num_cols = len(pattern), len(pattern[0])

    for col in range(num_cols - 1):
        if all(pattern[row][col] == pattern[row][col + 1] for row in range(num_rows)):
            possible_mirrors.append(col + 1)

    return possible_mirrors

def find_real_vertical_mirror(pattern: list[str], possible_locations: callable, clean_smudge = False) -> int:
    num_rows, num_cols = len(pattern), len(pattern[0])
    for location in possible_locations(pattern):
        is_mirror = True
        left_index, right_index = location - 1, location
        while left_index >= 0 and right_index < num_cols:
            if any(pattern[row][left_index] != pattern[row][right_index] for row in range(num_rows)):
                is_mirror = False
                break
            left_index -= 1
            right_index += 1
        if is_mirror:
            return location
    return 0

def find_possible_horizontal_mirrors(pattern: list[str]) -> list[int]:
    return [i + 1 for i, (line, next_line) in enumerate(zip(pattern, pattern[1:])) if line == next_line]

def find_real_horizontal_mirror(pattern: list[str], possible_locations: callable, clean_smudge = False) -> int:
    for location in possible_locations(pattern):
        upper_rows = pattern[:location:][::-1]
        lower_rows = pattern[location:]
        if all(upper_rows[row] == lower_rows[row] for row in range(min(len(upper_rows), len(lower_rows)))):
            return location
    return 0

def calculate_mirror_location(patterns: np.array[str], is_smudged: bool = False) -> int:
    original_mirror_location = calculate_mirror_location(patterns, is_smudged=False) if is_smudged else 0

    for potential_mirror in range(1, patterns.shape[0]):
        if potential_mirror == original_mirror_location:
            continue
        mismatch_count = 0
        for upper_part, lower_part in zip(reversed(patterns[:potential_mirror]), patterns[potential_mirror:]):
            mismatch_count += sum(upper != lower for upper, lower in zip(upper_part, lower_part))
            if mismatch_count > is_smudged:
                break
        else:
            return potential_mirror

    return 0

if __name__ == "__main__":
    main()
