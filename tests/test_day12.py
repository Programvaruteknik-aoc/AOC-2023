import unittest
from day12 import hot_springs

test_input_1 = """\
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

class TestDay12(unittest.TestCase):
    def test_part_one(self):
        expected_result = 21
        result:int = hot_springs.part_one(test_input_1.split("\n"))
        self.assertEqual(result, expected_result)

    def test_part_two(self):
        expected_result = 525152
        result:int = hot_springs.part_two(test_input_1.split("\n"))
        self.assertEqual(result, expected_result)

    @unittest.skip("Not implemented")
    def test_get_permutations(self):
        input_1 = "???.###"
        group_sizes_1 = [1, 1, 3]
        expected_result_1 = 1
        input_2 = "?###????????"
        group_sizes_2 = [3, 2, 1]
        expected_result_2 = 10
        result_1 = hot_springs.generate_arrangements(input_1, 0, '', group_sizes_1)
        result_2 = hot_springs.generate_arrangements(input_2, 0, '', group_sizes_2)
        self.assertEqual(result_1, expected_result_1)
        self.assertEqual(result_2, expected_result_2)


if __name__ == "__main__":
    unittest.main()
