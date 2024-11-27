from math import prod
from get_numbers import input_numbers

# sub_count cannot be larger than count:
count: int = 3
sub_count: int = 2
sorted_numbers: [int] = input_numbers(count)

start_from: int = count - sub_count
factors: [int] = sorted_numbers[start_from::]
product: int = prod(factors)
factors_as_text: str = ", ".join([str(n) for n in factors])
product_as_text: str = f'{product:,}'
print(
    f'\nThe product of the {sub_count} largest numbers '
    f'({factors_as_text}) is {product_as_text}.'
)
