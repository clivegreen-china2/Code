from random import shuffle
from es.explain_splits import explain_splits as es
from utility_functions import (
    sorted_name_list as snl,
    list_to_string as lts,
    format_as_currency as fac
)


def get_amount() -> float | None:

    amount_str: str = input('Enter bill amount: ')
    if amount_str == 'x':
        print('Exiting the program ...')
        exit()

    try:
        amount: float = float(amount_str)

    except ValueError:
        print(
            'Please input a numerical value '
            '(or an \'x\' to quit)'
        )
        return get_amount()

    return amount


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


def run(**settings) -> None:

    the_amount: float = (
            settings.get('amount') or get_amount()
    )
    the_names: [str] = (
            settings.get('names') or get_names()
    )
    explanation = es(
        amount=the_amount,
        count=len(the_names)
    )

    normal: float = explanation.get('normal')
    delta: float = explanation.get('delta')
    delta_count: int = explanation.get('delta_count')

    print('\nRUN:')
    if delta_count == 0:
        print(f'\tEveryone pays {fac(amount=normal)}.')

    else:

        shuffle(the_names)
        i: int = delta_count

        names_with_amounts: [dict] = [
            dict(
                who_pays=lts(values=the_names[:i], sort=True),
                how_much=fac(amount=normal+delta)
            ),
            dict(
                who_pays=lts(values=the_names[i:], sort=True),
                how_much=fac(amount=normal)
            )
        ]

        # explain who needs to pay what:
        for d in names_with_amounts:
            print(
                f'\t{d['how_much']}: {d['who_pays']}'
            )


if __name__ == '__main__':

    # test the app without manually inputting data:
    bill_input: float = 91000.7192
    names_input: str = \
        'clive,._JOHn, KArl_  & Will +. abbey MARK @@'

    run(amount=abs(bill_input), names=snl(names_input))
