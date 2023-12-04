from utils.util import get_input
import re

class Card:
    """ Represents a scratch card. """
    def __init__(self, card: str):
        self.card = card
        self.card_number:int = self.parse_card_number()
        self.winning_numbers:list[int] = self.parse_winning_numbers()
        self.scratch_numbers:list[int] = self.parse_scratch_numbers()
        self.points:int = None

    def parse_card_number(self) -> int:
        number_pattern = re.compile(r'\d+')
        return int(number_pattern.findall(self.card.split(":")[0])[0])

    def parse_winning_numbers(self) -> list[int]:
        return {int(number) for number in self.card.split(":")[1].split("|")[0].split(" ")[1:] if number.isdigit()}

    def parse_scratch_numbers(self) -> list[int]:
        return {int(number) for number in self.card.split("|")[1].split(" ") if number.isdigit()}

    def set_points(self, points:int) -> None:
        self.points = points

    def __str__(self) -> str:
        return f"Card {self.card_number}: winning numbers -> {self.winning_numbers} scratch numbers -> {self.scratch_numbers}"

    def __repr__(self) -> str:
        return self.__str__()

def main() -> None:
    file_input = get_input("day4/input.txt")
    print(f"Part one: {part_one(file_input)}")
    print(f"Part two: {part_two(file_input)}")

def part_one(input: list[str]) -> int:
    cards = [Card(card) for card in input]
    return sum([calculate_card_points(card) for card in cards])

def part_two(input: list[str]) -> int:
    cards = [Card(card) for card in input]
    cards_count = {card: 1 for card in cards}

    return sum(propagate_cards(cards, cards_count))

def propagate_cards(cards: list[Card], cards_count:[Card,int]) -> list[int]:
    """ Propagates the cards and increments the count for each card. Returns a list of the counts. """
    for index, card in enumerate(cards):
        card.set_points(calculate_matches(card))
        for i in range(1, card.points + 1):
            if index + i < len(cards):
                cards_count[cards[index + i]] += cards_count[card]

    return cards_count.values()


def calculate_card_points(card: Card) -> int:
    """ Calculates the points for a card. """
    points = 0
    # Add 1 point for first match, multiply by 2 for each subsequent match
    for _ in card.winning_numbers.intersection(card.scratch_numbers):
        points = points * 2 if points > 0 else 1
    return points

def calculate_matches(card: Card) -> int:
    """ Calculates the number of matches (intersections) for a card. """
    return len(card.winning_numbers.intersection(card.scratch_numbers))


if __name__ == "__main__":
    main()
