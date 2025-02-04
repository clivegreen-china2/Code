from math import floor


def format_number(value: float) -> str:

    """
    Converts float values to an appropriate display format:
    :param value: a floating point number
    :return: formatted number as a string
    """

    # does the float value supplied have a non-zero decimal component?
    has_decimal: bool = value > floor(value)

    # for decimal numbers, apply some formatting:
    if has_decimal:
        return f'{value:.2f}'  # str
    else:
        # convert into a 'whole-number' string:
        return str(int(value))


def show_error(message: str) -> None:

    print(f'Error found: \'{message}\'')


def show_description(description_text: str) -> None:

    print(f'\nDESCRIPTION: {description_text}')


def show_values(values: [], prefix: str | None = 'values') -> None:

    if prefix is None:
        prefix = 'values'

    print(f'{prefix.upper()}: ', end='')
    value_strings: [str] = [format_number(v) for v in values]
    print(f"{', '.join(value_strings)}")


def show_result(result: float) -> None:

    show_values([result], 'result')
