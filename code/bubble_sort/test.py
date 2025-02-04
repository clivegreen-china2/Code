def sort_list(values: list, forwards: bool = True) -> list:

    def twiddle(vals: list, index: int) -> None:

        a, b = vals[index], vals[index+1]
        if a > b:
            vals[index], vals[index+1] = b, a  # swap positions

    new_values = values.copy()
    end = len(new_values)-1
    while end > 0:
        [twiddle(new_values, i) for i in range(0, end)]
        end -= 1

    if not forwards:
        new_values.reverse()
    return new_values


if __name__ == '__main__':

    my_values: [int] = [5, 2, 3, 1, 4]

    sorted_values = sort_list(my_values, False)
    value_strings: [str] = [str(v) for v in sorted_values]
    values_string: str = ', '.join(value_strings)
    print(values_string)

    # BTW: Python already has functions for sorting!
