from sys import exit
from bubble_sort import bubble_sort as sort


exit_key: str = 'x'


def get_sorted_numbers(count: int) -> [int]:

    the_input: str = input(
        f"Enter {count} unique integers separated "
        f"by spaces (or type {exit_key} to cancel): "
    )
    if the_input == exit_key:
        exit()

    numbers: [int] = []
    try:
        numbers = [
            int(n) for n in the_input.split(' ')
        ]
    except ValueError:
        print("\nPlease enter numbers only!\n")
        get_sorted_numbers(count)

    if len(numbers) != count:
        print(f"\nPlease enter exactly {count} numbers!\n")
        get_sorted_numbers(count)

    return sort(numbers)
