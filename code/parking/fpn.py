from stdnum.iso7064.mod_11_10 import (calc_check_digit, is_valid)
from random import randint


def base(length: int = 4) -> str:
    random_number: int = randint(1, pow(10, length))
    format_spec: str = "{:0" + str(length) + "d}"
    return format_spec.format(random_number)


def generate_fpn(the_base: str) -> str:
    check_digit: str = calc_check_digit(the_base)
    return the_base + check_digit


def fpn_is_valid(candidate_id: str) -> bool:
    return is_valid(candidate_id)
