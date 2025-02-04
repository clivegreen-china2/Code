import re
from typing import Callable
from sys import exit
from display import show_error


def extract_numbers(text: str) -> [float]:

    """
    Returns a list of all valid numbers found in the text supplied.
    :param text: the text string to search
    :return: a list of floating point numbers
    """

    # match any number:
    number_pattern: str = r'[-]?\d+(?:[.]\d+)?'

    # extract any matching strings:
    matches: [str] = re.findall(number_pattern, text)

    # convert these into actual numbers:
    return [float(s) for s in matches]


def get_input(guidance: str, extractor: Callable, exit_str: str = 'x'):

    """
    Asks for user input, and processes the string data supplied.
    :param guidance: guidance instructions for the user
    :param extractor: the operation to be used on the input data
    :param exit_str: a string which terminates the program!
    :return: varies according to the extractor used.
    """

    guidance += f"\n(or type \'{exit_str}\' to cancel): "

    text: str = input(guidance)
    if text == exit_str:
        exit()

    return extractor(text)


def get_numbers_from_user() -> [float]:

    """
    Asks the user to input one or more numbers.
    :return: a list of floating point values.
    """

    numbers: [float] = get_input("Enter value(s)", extract_numbers)

    try:
        if len(numbers) == 0:
            print("At least one value is required.\n")
            return get_numbers_from_user()

    except ValueError:
        # something went wrong: tell the user to try again:
        show_error(numbers)
        return get_numbers_from_user()

    finally:
        # always return the list of numbers:
        return numbers
