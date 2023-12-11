from utils.util import get_input

START_SYMBOL = "S"
PIPE_TYPE = {
    "|": ("N", "S"),
    "-": ("E", "W"),
    "L": ("N", "E"),
    "J": ("N", "W"),
    "7": ("S", "W"),
    "F": ("S", "E"),
}

def main() -> None:
    file_input = get_input("day10/input.txt")
    print(f"Part one: {part_one(file_input)}")
    print(f"Part two: {part_two(file_input)}")

def part_one(input:list[str]) -> int:
    start_x, start_y = find_starting_coordinates(input)
    max_distance, _ = traverse_maze(input, start_x, start_y)
    return round(max_distance / 2)


def part_two(input: list[str]) -> int:
    start_x, start_y = find_starting_coordinates(input)
    _, loop_boundary = traverse_maze(input, start_x, start_y)

    inside_count = 0
    for y, line in enumerate(input):
        for x, _ in enumerate(line):
            if (x,y) in loop_boundary:
                continue
            crosses = 0
            x2,y2 = x,y

            while x2 < len(input[0]) and y2 < len(input):
                pipe = input[y2][x2]
                if (x2,y2) in loop_boundary and pipe not in ["L", "7"]:
                    crosses += 1
                x2 += 1
                y2 += 1

            if crosses % 2 == 1:
                inside_count += 1
    return inside_count

def traverse_maze(pipe_layout: list[str], start_col: int, start_row: int) -> tuple[int, set[tuple[int, int]]]:
    max_distance = 0
    exploration_stack = [(start_col, start_row, 0)]
    visited_positions = set()

    while exploration_stack:
        current_col, current_row, steps_from_start = exploration_stack.pop()
        if (current_col, current_row) in visited_positions:
            continue
        visited_positions.add((current_col, current_row))

        max_distance = max(max_distance, steps_from_start)

        for direction in get_directions(pipe_layout[current_row][current_col]):
            next_col, next_row = move(current_col, current_row, direction)
            if is_valid(next_col, next_row, pipe_layout):
                exploration_stack.append((next_col, next_row, steps_from_start + 1))

    return max_distance, visited_positions

def find_starting_coordinates(input:list[str]) -> tuple[int, int]:
    for y, line in enumerate(input):
        if START_SYMBOL in line:
            return (line.index(START_SYMBOL), y)
    return (-1, -1)

def get_directions(pipe:str) -> list[str]:
    if pipe == START_SYMBOL:
        return ["N", "E", "S", "W"]
    return PIPE_TYPE.get(pipe, [])

def move(x:int, y:int, direction:str) -> tuple[int, int]:
    if direction == "N":
        return x, y - 1
    if direction == "E":
        return x + 1, y
    if direction == "S":
        return x, y + 1
    if direction == "W":
        return x - 1, y
    return x, y

def is_valid(x:int, y:int, maze:list[str]) -> bool:
    return 0 <= y < len(maze) and 0 <= x < len(maze[0]) and maze[y][x] != '.'

if __name__ == "__main__":
    main()
