from utils.util import get_input
import re

def main() -> None:
    print(f'Part one: {first_last_digit_calibration(get_input("day1/input.txt"))}')
    print(f'Part two: {first_last_digit_word_calibration(get_input("day1/input.txt"))}')

def first_last_digit_calibration(calibration: list[str]) -> int:
    """
    Part one:
    Extracts the first and last digit of each line in calibration and sums them up
    """
    return sum([extract_first_last_digit(line) for line in calibration])

def first_last_digit_word_calibration(calibration: list[str]) -> int:
    """
    Part two:
    Extracts the first and last digit, or spelled out number, of each line in calibration and sums them up
    """
    return sum([extract_real_first_last_digit(line) for line in calibration])

def extract_first_last_digit(line:str) -> int:
    """Extracts the first and last digit of a string"""
    numbers = re.findall(r'\d', line)
    return int(numbers[0] + numbers[-1])

def extract_real_first_last_digit(line:str) -> int:
    """Extracts the first and last digit, or spelled out number, of a string"""
    digit_map = {
        "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }

    for key, value in digit_map.items():
        # replace the word with the first letter, digit, and the last letter
        # e.g. "oneight" -> "o1eight" -> "o1e8t"
        line = line.replace(key, key[0]+value+key[-1])

    return extract_first_last_digit(line)


if __name__ == '__main__':
    main()
