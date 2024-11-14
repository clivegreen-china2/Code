from regex_functions import (
    extract_amounts,
    extract_dates,
    extract_names
)


def test(**args) -> [str]:
    test_function = args.get('function', None)
    label: str = args.get('label', 'data')
    the_input: str = input(f'Type in your {label}: ')

    if callable(test_function):
        results = test_function(the_input)
        display(results)
        return results
    else:
        print(f'{test_function} is not callable.')
        return []


def display(items: [str]) -> None:
    items = sorted(items)
    count = len(items)
    label = f"match{'' if count == 1 else 'es'}"
    items_string = "\n\t".join([item for item in items])
    print(f"\n{count} {label}:\n\n\t{items_string}")


if __name__ == "__main__":
    test(function=extract_names, label="name(s)")
    test(function=extract_amounts, label="amount(s)")
    test(function=extract_dates, label="date(s)")
