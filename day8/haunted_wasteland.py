from utils.util import get_input
import re
import math
import itertools

def main() -> None:
    file_input = get_input("day8/input.txt")
    print(f"Part one: {part_one(file_input)}")
    print(f"Part two: {part_two(file_input)}")

def part_one(input: list[str]) -> int:
    char_pattern = re.compile(r"[A-Z]+")
    directions = input[0]
    current_location = "AAA"
    target_location = "ZZZ"

    coord_map = parse_map(input, char_pattern)

    return calculate_steps(directions, current_location, target_location, coord_map)

def part_two(input: list[str]) -> int:
    char_pattern = re.compile(r"[A-Z0-9]+")
    coord_map:dict[str, tuple[str,str]] = parse_map(input, char_pattern)
    steps = 1
    for coord in coord_map:
        directions = itertools.cycle(input[0])
        if coord.endswith("A"):
            steps = math.lcm(steps, solvesteps(coord, directions, coord_map))
    return steps

def solvesteps(start, directions, coord_map):
    pos = start
    i = 0
    while not pos.endswith('Z'):
        d = next(directions)
        pos = coord_map[pos][0 if d=='L' else 1]
        i += 1
    return i

def calculate_steps(directions, current_location, target_location, coord_map):
    steps = 0
    while current_location != target_location:
        for direction in directions:
            if direction == "L":
                steps += 1
                current_location = coord_map[current_location][0]
            elif direction == "R":
                steps += 1
                current_location = coord_map[current_location][1]
            else:
                raise Exception("Invalid direction")
            if current_location == target_location:
                break
    return steps

def parse_map(input, char_pattern):
    coord_map = {}

    for line in input[2:]:
        matches = re.findall(char_pattern, line)
        coord_map[matches[0]] = (matches[1], matches[2])
    return coord_map


if __name__ == "__main__":
    main()
