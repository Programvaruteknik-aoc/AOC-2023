import unittest
from day10 import pipe_maze

test_input_1 = """\
    .....
    .S-7.
    .|.|.
    .L-J.
    ....."""

test_input_2 = """\
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""

class TestDay10(unittest.TestCase):
    def test_part_one(self):
        expected_result = 4
        result:int = pipe_maze.part_one(test_input_1.split("\n"))
        self.assertEqual(result, expected_result)

    def test_part_two(self):
        expected_result = 10
        result:int = pipe_maze.part_two(test_input_2.split("\n"))
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
