import re

bag = {
        12: 'red', 13: 'green', 14: 'blue'
    }


def main():
    print(part_one())


def part_one() -> int:
    with open('input.txt', 'r') as f:
        x = 0
        for line in f:
            games = line.split(':', 1)[1]
            game_number = int(re.findall(r'\d+', line.split(':', 1)[0])[0])
            legit = True
            for game in games.split(';'):
                game_map = {}
                game = game.strip()
                pairs = game.split(',')
                for pair in pairs:
                    number, color = pair.strip().split(' ')
                    game_map[int(number)] = color
                if not process_map(game_map):
                    legit = False
            if legit:
                x += game_number
    return x


def process_map(game_map) -> bool:
    for key, value in game_map.items():
        if value in bag.values():
            corresponding_bag_key = [bag_key for bag_key, bag_value in bag.items() if bag_value == value][0]
            if key > corresponding_bag_key:
                return False
    return True


if __name__ == "__main__":
    main()
