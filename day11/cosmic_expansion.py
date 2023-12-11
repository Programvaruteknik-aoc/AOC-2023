from utils.util import get_input
import itertools

def main() -> None:
    file_input = get_input("day11/input.txt")
    print(f"Part one: {part_one(file_input)}")
    print(f"Part two: {part_two(file_input)}")

def part_one(input:list[str]) -> int:
    expanded_universe = expand_universe(input)
    galaxy_coordinates = find_galaxy_coordinates(expanded_universe)
    return sum(find_shortest_path_between_galaxies(galaxy_coordinates))

def part_two(input: list[str], rate_of_expansion = 1000000) -> int:
    # expanded_universe = expand_universe(input, rate_of_expansion)
    expanded_rows = find_empty_rows(input)
    expanded_columns = find_empty_columns(input)
    galaxy_coordinates = find_galaxy_coordinates(input)
    return sum(find_shortest_path_between_galaxies(galaxy_coordinates, rate_of_expansion, expanded_rows, expanded_columns))

def expand_universe(universe: list[str], expansion_rate = 1) -> list[str]:
    expand_universe = expand_rows(universe, find_empty_rows(universe), expansion_rate)
    expand_universe = expand_columns(expand_universe, find_empty_columns(expand_universe), expansion_rate)
    return expand_universe

def display_universe(universe: list[str]) -> None:
    print()
    for line in universe:
        print(line)

def find_empty_rows(universe: list[str]) -> list[int]:
    empty_rows = []
    for i, line in enumerate(universe):
        if all(symbol == "." for symbol in line):
            empty_rows.append(i)
    return empty_rows

def find_empty_columns(universe: list[str]) -> list[int]:
    empty_columns = []
    for i in range(len(universe[0])):
        if all(line[i] == "." for line in universe):
            empty_columns.append(i)
    return empty_columns

def expand_rows(universe: list[str], rows_to_expand:list[int], expansion_rate) -> list[str]:
    expanded_universe = universe.copy()
    shift = 0
    for row in rows_to_expand:
        for i in range(expansion_rate):
            expanded_universe.insert(row + shift, "." * len(universe[0]))
            shift += 1
    return expanded_universe

def expand_columns(universe: list[str], columns_to_expand: list[int], expansion_rate) -> list[str]:
    expanded_universe = []
    for line in universe:
        new_line = list(line)
        for column in sorted(columns_to_expand, reverse=True):
            for i in range(expansion_rate):
                new_line.insert(column, '.')
        expanded_universe.append(''.join(new_line))
    return expanded_universe

def find_galaxy_coordinates(universe: list[str]) -> list[tuple[int, int]]:
    galaxy_coordinates = []
    for y, line in enumerate(universe):
        if "#" in line:
            for x, symbol in enumerate(line):
                if symbol == "#":
                    galaxy_coordinates.append((x,y))
    return galaxy_coordinates

def find_shortest_path_between_galaxies(galaxy_coordinates: list[tuple[int, int]], rate_of_expansion = 1, expand_rows = [], expand_cols = []) -> list[int]:
    shortest_paths = []
    for galaxy1, galaxy2 in itertools.combinations(galaxy_coordinates, 2):
        shortest_paths.append(find_shortest_path(galaxy1, galaxy2, rate_of_expansion, expand_rows, expand_cols))
    return shortest_paths


def find_shortest_path(start: tuple[int, int], end: tuple[int, int], rate_of_expansion = 1, expand_rows = [], expand_cols = []) -> int:
    x_distance = abs(start[0] - end[0])
    y_distance = abs(start[1] - end[1])
    for row in expand_rows:
        if start[1] < row <= end[1] or end[1] < row <= start[1]:
            y_distance += rate_of_expansion - 1
    for col in expand_cols:
        if start[0] < col <= end[0] or end[0] < col <= start[0]:
            x_distance += rate_of_expansion - 1
    return x_distance + y_distance

if __name__ == "__main__":
    main()
