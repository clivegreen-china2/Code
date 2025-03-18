import re


def sorted_name_list(text: str) -> [str]:
    """
    proper-cases, extracts & sorts words from a string
    """
    # make all words begin with a capital letter:
    text = text.title()

    # remove any underscores:
    text = re.sub('_', '', text)
    # underscores aren't recognised by findall() ...

    matches: [str] = re.findall(r'\w+', text)
    return sorted(matches)


def list_to_string(**settings) -> str:

    values: list = settings.get('values', [])
    delimiter: str = settings.get('delimiter', ', ')
    _and_: str = settings.get('and', ' and ')
    _sort_: bool = settings.get('sort', False)

    # convert supplied list into a comma-delimited string:
    if _sort_:
        values.sort()
    text: str = delimiter.join(values)

    # replace the final delimiter with an _and_:
    pattern = rf'{delimiter}(?=\w+$)'
    text = re.sub(pattern, _and_, text)

    return text


def format_as_currency(**settings) -> str:
    """
    Converts a monetary float amount into a
    currency-formatted string.
    """
    amount: float = settings.get('amount', 0)
    before: str = settings.get('before', '¥')
    after: str = settings.get('after', '')

    format_str: str = "{:,.2f}"  # i.e.: two decimal places
    amount_str: str = format_str.format(amount)
    currency_str: str = f"{before}{amount_str}{after}"
    return currency_str
