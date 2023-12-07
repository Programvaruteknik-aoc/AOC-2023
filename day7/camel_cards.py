from utils.util import get_input

class Hand:
    def __init__(self, hand:str):
        self.HAND_RANKS = {
            "Five of a Kind": 7,
            "Four of a Kind": 6,
            "Full House": 5,
            "Three of a Kind": 4,
            "Two Pair": 3,
            "One Pair": 2,
            "High Card": 1
        }
        self.CARD_RANKS = {
            "A": 14,
            "K": 13,
            "Q": 12,
            "J": 11,
            "T": 10,
            "9": 9,
            "8": 8,
            "7": 7,
            "6": 6,
            "5": 5,
            "4": 4,
            "3": 3,
            "2": 2
        }
        self.cards:str = self.parse_cards(hand)
        self.bid:int = self.parse_bid(hand)
        self.type:int = self.evaluate_type()

    def parse_cards(self, hand:str) -> str:
        return hand.split(" ")[0].strip()

    def parse_bid(self, hand:str) -> int:
        return int(hand.split(" ")[1].strip())

    def evaluate_type(self) -> int:
        card_counts = {}
        for card in self.cards:
            card_counts[card] = card_counts.get(card, 0) + 1

        count_values = set(card_counts.values())

        if 5 in count_values:
            return self.HAND_RANKS["Five of a Kind"]
        elif 4 in count_values:
            return self.HAND_RANKS["Four of a Kind"]
        elif 3 in count_values and 2 in count_values:
            return self.HAND_RANKS["Full House"]
        elif 3 in count_values:
            return self.HAND_RANKS["Three of a Kind"]
        elif list(count_values).count(2) == 2:
            return self.HAND_RANKS["Two Pair"]
        elif 2 in count_values:
            return self.HAND_RANKS["One Pair"]
        else:
            return self.HAND_RANKS["High Card"]

    def __eq__(self, other) -> bool:
        return self.type == other.type

    def __gt__(self, other) -> bool:
        if not self.__eq__(other):
            return self.type > other.type
        else:
            for i in range(len(self.cards)):
                if self.cards[i] != other.cards[i]:
                    return self.CARD_RANKS[self.cards[i]] > self.CARD_RANKS[other.cards[i]]

    def __lt__(self, other) -> bool:
        return not self.__gt__(other)

    def __repr__(self) -> str:
        return f"{self.cards} {self.bid} {self.type}"


def main() -> None:
    file_input = get_input("day7/input.txt")
    print(f"Part one: {part_one(file_input)}")
    print(f"Part two: {part_two(file_input)}")

def part_one(input: list[str]) -> int:
    hands = [Hand(hand) for hand in input]
    hands.sort()
    return calculate_total_winnings(hands)

def part_two(input: list[str]) -> int:
    pass

def calculate_total_winnings(hands:list[str]) -> int:
    total_winnings = 0
    for i in range(len(hands)):
        total_winnings += hands[i].bid * (i + 1)
    return total_winnings

if __name__ == "__main__":
    main()
