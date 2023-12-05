import re
from collections import defaultdict
from utils.util import get_input

def is_symbol(char):
    return (not char.isdigit()) and char != '.'

def get_neighbors(row, start_col, end_col):
    neighbor_set = set()
    for col in range(start_col, end_col):
        for delta_row in [-1, 0, 1]:
            for delta_col in [-1, 0, 1]:
                neighbor_row = row + delta_row
                neighbor_col = col + delta_col
                if 0 <= neighbor_row < grid_height and 0 <= neighbor_col < grid_width:
                    neighbor_set.add((neighbor_row, neighbor_col))
    return neighbor_set

grid = [line for line in get_input('input.txt')]
grid_height = len(grid)
grid_width = len(grid[0])
total = 0

for row in range(grid_height):
    col = 0
    while col < grid_width:
        if not grid[row][col].isdigit():
            col += 1
            continue
        end_num_idx = col + 1
        while end_num_idx < grid_width and grid[row][end_num_idx].isdigit():
            end_num_idx += 1
        if any(is_symbol(grid[neighbor_row][neighbor_col]) for neighbor_row, neighbor_col in get_neighbors(row, col, end_num_idx)):
            number = int(grid[row][col:end_num_idx])
            total += number
        col = end_num_idx


def main():
    print("Day 3")
    print(total)

if __name__ == "__main__":
    main()
