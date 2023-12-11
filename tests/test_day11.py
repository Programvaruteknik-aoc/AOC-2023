import unittest
from day11 import cosmic_expansion

test_input_1 = """\
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

class TestDay11(unittest.TestCase):
    def test_part_one(self):
        expected_result = 374
        result:int = cosmic_expansion.part_one(test_input_1.split("\n"))
        self.assertEqual(result, expected_result)

    def test_part_two(self):
        expected_result = 8410
        result:int = cosmic_expansion.part_two(test_input_1.split("\n"), 100)
        self.assertEqual(result, expected_result)

    def test_expand_universe(self):
        expected_width = 16
        expected_height = 14
        result = cosmic_expansion.expand_universe(test_input_1.split("\n"), 2)
        self.assertEqual(len(result[0]), expected_width, "Width of universe is not correct")
        self.assertEqual(len(result), expected_height, "Height of universe is not correct")


if __name__ == "__main__":
    unittest.main()
