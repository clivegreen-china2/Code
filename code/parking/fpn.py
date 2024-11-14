from stdnum.iso7064.mod_11_10 import (
    calc_check_digit, is_valid
)
from random import randint


def generate_fpn() -> str:
    base: str = str(randint(1, 9999))
    check_digit: str = calc_check_digit(base)
    return base + check_digit


def fpn_is_valid(candidate_id: str) -> bool:
    return is_valid(candidate_id)
