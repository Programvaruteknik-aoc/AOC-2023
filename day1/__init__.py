import re


def part_one() -> int:
    x = 0
    with open('input.txt', 'r') as f:
        for line in f:
            digits = re.findall(r'\d+', line)
            if digits:
                if len(digits) == 1 and len(digits[0]) > 9:
                    x += int(digits[0])
                else:
                    first_int = digits[0][0]
                    last_int = digits[-1][-1]
                    x += int(first_int + last_int)
    return x

def part_two() -> int:
    x = 0
    digits = {
        "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    with open('test.txt', 'r') as f:
        for line in f:
            line = line.lower()
            for key, value in digits.items():
                line = line.replace(key, key[0] + value + key[-1])

            found_digits = re.findall(r'\d+', line)
            if len(found_digits) == 1 and len(found_digits[0]) > 0:
                x += int(found_digits[0])
            else:
                first_int = found_digits[0][0]
                last_int = found_digits[-1][-1]
                x += int(first_int + last_int)
    return x

if __name__ == "__main__":
    print(part_one())
    print(part_two())


