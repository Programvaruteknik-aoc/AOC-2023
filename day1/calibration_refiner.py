from utils.util import get_input
import re

def main() -> None:
    print(f'Part one: {first_last_digit_calibration(get_input("day1/input.txt"))}')
    print(f'Part two: {first_last_digit_word_calibration(get_input("day1/input.txt"))}')

def first_last_digit_calibration(calibration: list[str]) -> int:
    return sum([extract_first_last_digit(line) for line in calibration])

def first_last_digit_word_calibration(calibration: list[str]) -> int:
    return sum([extract_real_first_last_digit(line) for line in calibration])

def get_input(path:str) -> list[str]:
    with open(path, 'r') as f:
        return [line.strip() for line in f.readlines()]


def extract_first_last_digit(line:str) -> int:
    numbers = re.findall(r'\d', line)
    return int(numbers[0] + numbers[-1])

def extract_real_first_last_digit(line:str) -> int:
    digit_map = {
        "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }

    for key, value in digit_map.items():
        line = line.replace(key, key[0]+value+key[-1])

    return extract_first_last_digit(line)


if __name__ == '__main__':
    main()
