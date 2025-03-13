import re
from math import floor
from random import shuffle

from currency import (
    format_as_currency as fac,
    convert_to_pennies as ctp
)
from text import sorted_name_list as snl


def get_bill_in_pennies() -> int | None:

    amount_str: str = input('Enter total bill: ')
    if amount_str == 'x':
        print('Exiting the program ...')
        exit()

    try:
        amount: float = float(amount_str)
        pennies: int = abs(ctp(amount))

    except ValueError:
        print(
            'Please input a number amount '
            '(or an \'x\' to quit)'
        )
        return get_bill_in_pennies()

    return pennies


def get_names() -> [str]:

    names_str = input(f'Enter people\'s names: ')
    if names_str == 'x':
        print('Exiting the program ...')
        exit()

    try:
        return snl(names_str)

    except ValueError:
        print(
            'Please type in some names '
            '(or an \'x\' to quit)'
        )
        return get_names()


def get_names_with_amounts(pennies: int, names: [str]) -> [dict]:

    # how many pennies should each person pay as a minimum?
    payer_count: int = len(names)
    base_pennies: int = floor(pennies / payer_count)
    remaining_pennies: int = pennies - base_pennies * payer_count

    if remaining_pennies == 0:

        return [
            dict(
                names=names,
                pennies=base_pennies
            )
        ]

    else:

        # randomly mix up the list of names, in order
        # to fairly assign pennies:
        shuffle(names)

        # divide the names into two groups,
        # each with a payment amount:
        rp: int = remaining_pennies
        return [
            dict(
                names=sorted(names[rp:]),
                pennies=base_pennies
            ),
            dict(
                names=sorted(names[:rp]),
                pennies=base_pennies + 1
            )
        ]


def run(**settings) -> None:

    # get pennies as needed:
    the_pennies: int = (
            settings.get('pennies') or
            get_bill_in_pennies()
    )

    # get names as needed:
    the_names: [str] = (
            settings.get('names') or
            get_names()
    )

    # split the bill and store the results:
    names_with_amounts: [dict] = (
        get_names_with_amounts(the_pennies, the_names)
    )

    # recalculate and display the total bill:
    total: int = 0
    for d in names_with_amounts:
        count: int = len(d['names'])
        total += d['pennies'] * count

    print(
        f'\n\tCalculated Total:\n\t'
        f'{fac(pennies=total)}\n'
    )

    # explain who needs to pay what:
    for d in names_with_amounts:
        how_much: str = fac(
            pennies=d['pennies']
        )
        who_pays: str = ", ".join(sorted(d['names']))

        # replace the final comma+space with 'and':
        pattern = r',\s(?=\w+$)'
        who_pays = re.sub(pattern, ' and ', who_pays)

        print(f'\t{how_much}: {who_pays}')


if __name__ == '__main__':

    # test the app without manually inputting data:
    bill_input: float = 9000.0402
    names_input: str = \
        '   clive,.. ___JOHn, KArl_  & + . abbey MARK @@'

    run(
        pennies=abs(ctp(bill_input)),
        names=snl(names_input)
    )
