from utils.util import get_input
import re
import math

def main() -> None:
    file_input = get_input("day3/input.txt")
    print(f"Part one: {part_one(file_input)}")
    print(f"Part two: {part_two(file_input)}")

def part_one(input: list[str]) -> int:
    parts = identify_parts(input)
    return sum(sum(part) for part in parts.values())

def part_two(input: list[str]) -> int:
    parts = identify_parts(input)
    return sum(math.prod(part) for part in parts.values() if len(part) == 2)

def identify_parts(lines: list[str]) -> dict[tuple[int, int], list[int]]:
    """Identifies the parts in the input."""
    non_symbol_positions = identify_non_symbol_positions(lines)
    part_numbers = {}
    number_pattern = re.compile(r'\d+')

    for row_index, row_content in enumerate(lines):
        for number_match in number_pattern.finditer(row_content):
            edge_cells = find_edge_cells(row_index, number_match, len(row_content))
            number = int(number_match.group())
            add_numbers_to_parts(part_numbers, edge_cells, number, non_symbol_positions)

    return part_numbers

def identify_non_symbol_positions(lines: list[str]) -> dict[tuple[int, int], list]:
    """Identifies the positions of all non-symbol characters in the input."""
    number_dot_pattern = re.compile(r'[\d\.]+')
    non_symbol_positions = {}

    for row_index, row_content in enumerate(lines):
        for col_index, char in enumerate(row_content):
            if not number_dot_pattern.match(char):
                non_symbol_positions[(row_index, col_index)] = []
    return non_symbol_positions

def find_edge_cells(row_index: int, number_match, line_length: int) -> set:
    """Finds the edge cells of a number in a row."""
    edge_cells = set()

    for row in (row_index-1, row_index, row_index+1):
        for col in range(max(0, number_match.start() - 1),
                         min(number_match.end() + 1, line_length)):
            edge_cells.add((row, col))
    return edge_cells

def add_numbers_to_parts(part_numbers: dict, edge_cells: set, number: int, non_symbol_positions: dict):
    """Adds the number to parts."""
    for position in edge_cells:
        if position in non_symbol_positions:
            if position not in part_numbers:
                part_numbers[position] = []
            part_numbers[position].append(number)

if __name__ == "__main__":
    main()
