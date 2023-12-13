import unittest
from day13 import point_of_incidence

test_input_1 = """\
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

class TestDay13(unittest.TestCase):
    def test_part_one(self):
        expected_result = 405
        result:int = point_of_incidence.part_one(test_input_1.split("\n"))
        self.assertEqual(result, expected_result)

    def test_part_two(self):
        expected_result = -1
        result:int = point_of_incidence.part_two(test_input_1.split("\n"))
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
