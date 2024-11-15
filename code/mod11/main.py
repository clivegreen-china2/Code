from mod11 import (is_valid, calc_digit)

if __name__ == "__main__":
    base_num: int = 1234567
    with_check_digit: str = calc_digit(base_num)
    prefix: str = '' if is_valid(with_check_digit) \
        else 'in'
    print(
        f"the number entered was {base_num}.\n"
        f"The result was {with_check_digit}.\n"
        f"This is {prefix}valid"
    )
