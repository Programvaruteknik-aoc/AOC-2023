def get_input(path:str) -> list[str]:
    with open(path, 'r') as f:
        return [line.strip() for line in f.readlines()]
