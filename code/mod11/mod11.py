def calc_digit(num: int) -> str:
    # convert number supplied into a list of digits:
    digits: [int] = [int(ds) for ds in str(num)]
    count: int = len(digits)
    # various each digit by a weighting number; store a running total:
    total: int = 0
    for index, digit in enumerate(digits):
        weight = count + 1 - index
        total += weight * digit
    # calculate check digit using modulo-11
    check_digit = 11 - (total % 11)
    if check_digit > 9:
        check_digit = 'X'
    return f"{num}{check_digit}"


def is_valid(num_str: str) -> bool:
    # remove the last digit of the string supplied:
    candidate: int = int(num_str[:-1])
    return num_str == calc_digit(candidate)
