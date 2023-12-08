import unittest
from day8 import haunted_wasteland

test_input_1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

test_input_2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

test_input_3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

class TestDay8(unittest.TestCase):
    def test_part_one(self):
        expected_result_1 = 2
        expected_result_2 = 6
        result_1:int = haunted_wasteland.part_one(test_input_1.split("\n"))
        self.assertEqual(result_1, expected_result_1)
        result_2:int = haunted_wasteland.part_one(test_input_2.split("\n"))
        self.assertEqual(result_2, expected_result_2)

    def test_part_two(self):
        expected_result = 6
        result:int = haunted_wasteland.part_two(test_input_3.split("\n"))
        self.assertEqual(result, expected_result)



if __name__ == "__main__":
    unittest.main()
