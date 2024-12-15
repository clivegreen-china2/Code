from copy import deepcopy
import re

exit_char: str = 'x'
exit_msg: str = f'\n(type an \'{exit_char}\' to exit)'

group_total_range: range = range(28, 36)  # 28 to 35
min_group_total: int = group_total_range[0]
max_group_total: int = group_total_range[-1]

candidate_total_range: range = range(1, 5)  # 1 to 4
min_candidate_total: int = candidate_total_range[0]
max_candidate_total: int = candidate_total_range[-1]

years: range = range(7, 12)  # 7 to 11
letters: [str] = list('ABCDEF')

candidates_template: dict[str: int] = {}  # to store names with votes
group_template: dict = dict(
    group_total=min_group_total,
    candidate_total=0,
    candidates=candidates_template,
    abstentions=0
)

groups: dict[str: dict] = dict()
for year in years:
    for letter in letters:
        key: str = str(f'{year}{letter}')
        value: dict[str: int] = deepcopy(group_template)
        groups.update({key: value})


def group_size_ok(n: int) -> bool:
    return n in group_total_range


def candidate_total_ok(n: int) -> bool:
    return n in candidate_total_range


def specify_group() -> None:

    the_input: str = input(
        f'Input a valid tutor group name (e.g.: \'9E\'){exit_msg}'
    )
    if the_input == exit_char:
        return

    if the_input not in groups.keys():
        print(f'Sorry, the group \'{the_input}\' isn\'t recognized.\n')
        specify_group()

    group_name = the_input
    specify_candidates(group_name)


def specify_candidates(group_name: str) -> None:

    the_input = input(
        f'Please enter 1-4 unique candidate names separated by spaces{exit_msg}'
    )
    names: [str] = re.split(the_input, r'\s+')
    total: int = len(names)
    if not candidate_total_ok(total):
        specify_candidates(group_name)

    group: dict = groups[group_name]
    group['candidate_total'] = total
    candidates: dict = group['candidates']
    [candidates.update({name, 0}) for name in names]


if __name__ == '__main__':
    ...
    # for key, value in tutor_groups.items():
    #     print(key, value)
