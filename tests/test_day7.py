import unittest
from day7 import camel_cards

test_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

class TestDay7(unittest.TestCase):
    def test_part_one(self):
        expected_result = 6440
        result:int = camel_cards.part_one(test_input.split("\n"))
        self.assertEqual(result, expected_result)

    def test_part_two(self):
        expected_result = 0
        result:int = camel_cards.part_two(test_input.split("\n"))
        self.assertEqual(result, expected_result)

    def test_hand_type(self):
        expected_result = 7
        result:int = camel_cards.Hand("AAAAA 1").type
        self.assertEqual(result, expected_result)

    def test_sorting_hands_by_type(self):
        input = ["AAAA2 684", "AAAAA 765"]
        expected_result = "AAAA2"
        hands = [camel_cards.Hand(hand) for hand in input]
        hands.sort()
        result:str = hands[0].cards
        self.assertEqual(result, expected_result)

    def test_sorting_hands_by_type_and_card(self):
        input = ["KKAA2 1", "AAJJ3 4"]
        expected_result = "KKAA2"
        hands = [camel_cards.Hand(hand) for hand in input]
        hands.sort()
        result:str = hands[0].cards
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
