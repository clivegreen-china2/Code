color_names: [str] = [
    'red', 'green', 'yellow', 'blue'
]


def get_color(index: int) -> str:

    index %= len(color_names)
    return color_names[index]
