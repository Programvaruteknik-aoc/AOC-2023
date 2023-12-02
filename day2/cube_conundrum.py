from utils.util import get_input
from functools import reduce
import re

def main() -> None:
    file_input = get_input("day2/input.txt")
    print(f"Part one: {part_one(file_input)}")
    print(f"Part two: {part_two(file_input)}")


def part_one(input:list[str]) -> int:
    """
    Calculates the sum of game IDs that match the given constraints.

    Args:
        input (list[str]): List of strings representing game data.

    Returns:
        int: Sum of game IDs that match the constraints.
    """
    red_constraint = 12
    green_constraint = 13
    blue_constraint = 14
    sum = 0
    for line in input:
        gameID, data = line.split(":")
        gameID = re.findall(r'\d+', gameID).pop()
        sets = data.split(";")
        sum += int(gameID) if match_constraints(red_constraint, green_constraint, blue_constraint, sets) else 0
    return sum

def part_two(input:list[str]) -> int:
    """ Calculates the power sum of the fewest number of cubes that match the given constraints.

    Args:
        input (list[str]): _description_

    Returns:
        int: _description_
    """
    power_sum = 0
    for line in input:
        _, data = line.split(":")
        sets = data.split(";")
        fewest_number_of_cubes = get_fewest_number_of_cubes(sets)
        power_sum += calculate_power(fewest_number_of_cubes.values())
    return power_sum


def match_constraints(amount_red:int, amount_green:int, amount_blue:int, cube_data:list[str]) -> bool:
    """
    Checks if the given cube data satisfies the color constraints.

    Args:
        amount_red (int): Maximum allowed amount of red cubes.
        amount_green (int): Maximum allowed amount of green cubes.
        amount_blue (int): Maximum allowed amount of blue cubes.
        cube_data (list[str]): List of cube colors.

    Returns:
        bool: True if the color constraints are satisfied, False otherwise.
    """
    for revealed in cube_data:
        color_counts = extract_color_count(revealed)
        if (color_counts['red'] > amount_red or
            color_counts['green'] > amount_green or
            color_counts['blue'] > amount_blue):
            return False
    return True

def get_fewest_number_of_cubes(sets:list[str]) -> dict[str, int]:
    """
    Calculates the maximum count of each color in a list of sets.

    Args:
        sets (list[str]): A list of sets, where each set represents the colors of cubes revealed.

    Returns:
        dict[str, int]: A dictionary containing the maximum count of each color, with color names as keys.
    """
    max_color_counts = {'red': 0, 'green': 0, 'blue': 0}
    for revealed in sets:
        for color, count in extract_color_count(revealed).items():
            max_color_counts[color] = max(count, max_color_counts[color])
    return max_color_counts

def calculate_power(values:list[int]) -> int:
    """ Calculates the power of a list of values.

    Args:
        values (list[int]): A list of values.

    Returns:
        int: The power of the values.
    """
    return reduce(lambda a, b: a * b, values, 1)

def extract_color_count(revealed:str) -> dict[str, int]:
    """
    Extracts the count of red, green, and blue colors from the given string.

    Args:
        revealed (str): The string containing color counts in the format 'x red, y green, z blue'.
    Returns:
        dict[str, int]: A dictionary containing the count of red, green, and blue colors.
    """
    pattern = r'(\d+) red|(\d+) green|(\d+) blue'
    color_counts = {'red': 0, 'green': 0, 'blue': 0}

    for match in re.finditer(pattern, revealed):
        red, green, blue = match.groups()
        if red:
            color_counts['red'] += int(red)
        elif green:
            color_counts['green'] += int(green)
        elif blue:
            color_counts['blue'] += int(blue)
    return color_counts

if __name__ == '__main__':
    main()
