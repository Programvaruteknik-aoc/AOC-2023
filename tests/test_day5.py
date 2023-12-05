import unittest
from day5 import food_production

test_input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

class TestDay5(unittest.TestCase):
    def test_part_one(self):
        expected_result = 35
        result:int = food_production.part_one(test_input.split("\n"))
        self.assertEqual(result, expected_result)

    def test_part_two(self):
        expected_result = 46
        result:int = food_production.part_two(test_input.split("\n"))
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
