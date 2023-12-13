from utils.util import get_input

def main() -> None:
    file_input = get_input("day13/input.txt")
    print(f"Part one: {part_one(file_input)}")
    print(f"Part two: {part_two(file_input)}")

def part_one(input: list[str]) -> int:
    patterns = extract_patterns(input)
    return sum(find_real_vertical_mirror(pattern, find_possible_vertical_mirrors) for pattern in patterns) \
           + sum(find_real_horizontal_mirror(pattern, find_possible_horizontal_mirrors) for pattern in patterns) * 100

def part_two(input:list[str]) -> int:
    patterns = extract_patterns(input)
    return sum(find_real_vertical_mirror(pattern, find_possible_vertical_mirrors, True) for pattern in patterns) \
           + sum(find_real_horizontal_mirror(pattern, find_possible_horizontal_mirrors, True) for pattern in patterns) * 100

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

def fix_vertical_smudge(pattern: list[str], left_index: int, right_index: int) -> bool:
    num_rows = len(pattern)
    for row in range(num_rows):
        if pattern[row][left_index] != pattern[row][right_index]:
            new_char_left = '#' if pattern[row][right_index] == '.' else '.'
            pattern[row] = replace_char_at_index(pattern[row], left_index, new_char_left)
            return True
    return False

def fix_horizontal_smudge(pattern: list[str], upper_index: int, lower_index: int) -> bool:
    num_cols = len(pattern[0])
    smudge_fixed = False

    for col in range(num_cols):
        if pattern[upper_index][col] != pattern[lower_index][col]:
            new_char = '#' if pattern[upper_index][col] == '.' else '.'
            pattern[upper_index] = replace_char_at_index(pattern[upper_index], col, new_char)
            smudge_fixed = True

    return smudge_fixed

def replace_char_at_index(s: str, index: int, new_char: str) -> str:
    return s[:index] + new_char + s[index + 1:]

if __name__ == "__main__":
    main()
