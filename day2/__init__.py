import re


def main():
    print(part_one())
    print(part_two())


def part_two() -> int:

    with open('input.txt', 'r') as f:
        x = 0
        for line in f:
            games = line.split(':', 1)[1]
            game_map = {}
            for game in games.split(';'):
                game = game.strip()
                for game_pair in game.split(','):
                    color = game_pair.split(" ")[-1]
                    number = re.findall(r'\d+', game_pair)[0]
                    if color not in game_map or game_map[color] < int(number):
                        game_map[color] = int(number)
            y = 1
            for value in game_map.values():
                y *= int(value)
            x += y
    return x


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
                for game_pair in game.split(','):
                    number, color = game_pair.strip().split(' ')
                    game_map[int(number)] = color
                if not process_map(game_map):
                    legit = False
            if legit:
                x += game_number
    return x


def process_map(game_map) -> bool:

    bag = {
        12: 'red', 13: 'green', 14: 'blue'
    }

    for key, value in game_map.items():
        if value in bag.values():
            corresponding_bag_key = [bag_key for bag_key, bag_value in bag.items() if bag_value == value][0]
            if key > corresponding_bag_key:
                return False
    return True


if __name__ == "__main__":
    main()
