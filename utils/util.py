def get_input(path: str) -> list[str]:
    with open(path, 'r') as f:
        return f.read().splitlines()
