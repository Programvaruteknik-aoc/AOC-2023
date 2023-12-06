from utils.util import get_input

def main() -> None:
    file_input = get_input("day6/input.txt")
    print(f"Part one: {part_one(file_input)}")
    print(f"Part two: {part_two(file_input)}")

def part_one(input: list[str]) -> int:
    product = 1
    times = extract_numbers_from_line(input[0])
    distances = extract_numbers_from_line(input[1])
    for time, distance in zip(times, distances):
        amount = count_winning_strategies(time, distance)
        product *= amount if amount > 0 else 1
    return product

def part_two(input: list[str]) -> int:
    product = 1
    time = extract_number_from_line(input[0])
    distance = extract_number_from_line(input[1])
    product = count_winning_strategies(time, distance)
    return product

def extract_numbers_from_line(line:str) -> list[int]:
    return [int(num) for num in line.split(":")[1].split()]

def extract_number_from_line(line:str) -> int:
    return int(line.split(":")[1].replace(" ", ""))

def count_winning_strategies(time:int, distance:int) -> int:
    winning_distances = []
    for press_time in range(time + 1):
        traveled = press_time * (time - press_time)
        if traveled > distance:
            winning_distances.append(distance)
    return len(winning_distances)

def calculate_travel_distance(speed:int, remaining_time: int) -> int:
    return speed * remaining_time

if __name__ == "__main__":
    main()
