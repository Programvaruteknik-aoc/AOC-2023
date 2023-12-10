import unittest
from day9 import mirage_maintenance

test_input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


class TestDay9(unittest.TestCase):
    def test_part_one(self):
        expected_result = 114
        result:int = mirage_maintenance.part_one(test_input.split("\n"))
        self.assertEqual(result, expected_result)

    def test_part_two(self):
        expected_result = 2
        result:int = mirage_maintenance.part_two(test_input.split("\n"))
        self.assertEqual(result, expected_result)



if __name__ == "__main__":
    unittest.main()
