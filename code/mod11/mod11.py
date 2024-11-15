def calc_digit(num: int) -> str:
    digits: [int] = [int(ds) for ds in str(num)]
    count: int = len(digits)
    total: int = 0
    for index, digit in enumerate(digits):
        weight = count + 1 - index
        total += weight * digit
    print(f'total: {total}')
    check_digit = 11 - (total % 11)
    if check_digit > 9:
        check_digit = 'X'
    return f"{num}{check_digit}"


def is_valid(num_str: str) -> bool:
    candidate: int = int(num_str[:-1])
    recalculated: str = calc_digit(candidate)
    return recalculated == num_str
