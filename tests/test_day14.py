import unittest
from day14 import parabolic_reflector_dish

test_input_1 = """\
"""

class TestDay14(unittest.TestCase):
    def test_part_one(self):
        expected_result = -1
        result:int = parabolic_reflector_dish.part_one(test_input_1.split("\n"))
        self.assertEqual(result, expected_result)

    def test_part_two(self):
        expected_result = -1
        result:int = parabolic_reflector_dish.part_two(test_input_1.split("\n"))
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
