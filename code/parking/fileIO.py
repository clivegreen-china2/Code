def read(filename: str) -> str:
    with open(filename, mode='r') as file:
        return file.read()


def write(filename: str, text: str) -> None:
    with open(filename, mode='w') as file:
        file.write(text)
