import re
from datetime import datetime


def extract_names(the_input: str) -> [str]:

    # Assemble a proper noun regex:
    first_letter = r'\b[A-Z]'
    rest_of_name = r'[a-z]+\b'
    name_regex = f'{first_letter}{rest_of_name}'
    # i.e.: an uppercase initial letter followed by at least one lowercase letter.

    return re.findall(name_regex, the_input.strip())


def extract_amounts(the_input: str) -> [str]:

    # Assemble a number regex:
    sign = r'[+-]?'
    integer_part = r'\d+'
    decimal_part = r'\.\d+'
    number_regex = f'{sign}{integer_part}(?:{decimal_part})?'
    # The ?: above means the enclosing parentheses are non-capturing

    results = re.findall(number_regex, the_input.strip())
    return [f'{float(r):.2f}' for r in results]


def extract_dates(the_input: str) -> [str]:

    # Assemble a date regex:
    two_or_four_digits = r'\d{2,4}'
    one_or_two_digits = r'\d{1,2}'
    year = f'({two_or_four_digits})'
    month = f'({one_or_two_digits})'
    day = f'({one_or_two_digits})'
    separator = r'[/-]'
    date_regex = f'({year}{separator}{month}{separator}{day})'

    # Compile a list of all valid dates in the input supplied:
    results = re.findall(date_regex, the_input.strip())
    dates = []
    for r in results:
        date, y, m, d = r[0], r[1], r[2], r[3]
        if len(y) == 2:
            # for two-digit years, assume current century:
            current_year = datetime.now().year
            century = str(current_year)[0:2]
            date = f'{century}{date}'
            y = f'{century}{y}'

        # to validate the date information, attempt to create
        # a temporary date object from it:
        try:
            date_object = datetime(int(y), int(m), int(d))
            # if the above date object is valid, the following will happen:
            date_string = date_object.strftime("%Y/%m/%d")
            dates.append(date_string)
        except ValueError:
            # raise an exception for impostors:
            print(f"Ignoring invalid date: {date}")
    return dates


