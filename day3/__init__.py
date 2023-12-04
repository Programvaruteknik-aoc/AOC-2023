import re
from utils.util import get_input

def main():
    print("Day 3")

    print(part_one(get_input('test.txt')))


class Node:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val

def part_one(input) -> int:

    x = 0
    y = 0
    nodes = list(Node)
    for line in input:
        for col in line:
            if col.isdigit():
                

            x+=1
        y +=1
        print(y)

    return 1









if __name__ == "__main__":
    main()
