from typing import Callable
from user_input import get_numbers_from_user
from display import (
    show_error, show_description, show_values, show_result
)

pwr: Callable = lambda a, b: a ** b

item_lambdas = dict(
    squared=lambda x: pwr(x, 2),
    cubed=lambda x: pwr(x, 3)
)

list_lambdas = dict(
    sum_up=lambda x, y: x + y,
    substract=lambda x, y: x - y,
    multiply=lambda x, y: x * y,
    divide=lambda x, y: x / y,
    next=lambda x, y: y,
    max=lambda x, y: x if x >= y else y
)


def build_reduction_function(settings: dict) -> Callable:

    """
    This returns a function that can be used to
    iterate over a list of values.
    :param settings: a dictionary of items needed to build the function.
    :return: a list of floating point values.
    """

    # unpack settings, using sensible default values as needed:
    value_list: [float] = settings.get('value_list', [])
    list_lambda: Callable = settings.get('list_lambda', list_lambdas.get('sum_up'))
    item_lambda: Callable = settings.get('item_lambda', lambda x: x)

    seed: float | None = settings.get('seed', None)
    if seed is not None:
        value_list = [seed] + value_list

    # Define a nested function:
    def __() -> float:

        # build a range of valid indices:
        indices = range(0, len(value_list) - 1)

        # The 'indices' range above will be empty for a single-item value list.
        # In which case, the loop below will NOT be run:
        for i in indices:
            # get an adjacent pair of listed values:
            a, b = value_list[i], value_list[i + 1]

            # call the processing operations; store the result:
            value_list[i + 1] = list_lambda(a, item_lambda(b))

        # this function returns the final value in the list:
        return value_list[-1]

    # return a reference to the nested function:
    return __


def do(**settings) -> float | None:

    """
    Processes a list of values to obtain a single result.
    :param settings: a set of items needed to build the processor function.
    :return: a floating point number
    """

    # what are we doing?
    show_description(
        settings.get('description', '(not given)')
    )

    # use a list of supplied values, or else ask the user to provide them:
    value_list: [float] = settings.get('value_list', [])
    settings['values_list'] = \
        get_numbers_from_user() if value_list == [] else value_list.copy()

    # what values were used?
    show_values(value_list)

    # build and execute the function:
    f: Callable = build_reduction_function(settings)
    result: float = f()
    if result is None:
        show_error('No result was obtained')
    else:
        show_result(result)

    return result
