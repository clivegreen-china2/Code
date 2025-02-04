from typing import Callable
from lambdas import do, item_lambdas, list_lambdas

squared: Callable = item_lambdas.get_item('squared')
cubed: Callable = item_lambdas.get_item('cubed')


if __name__ == '__main__':

    sum_of_1_to_9 = do(
        description='Sum of the first 9 integers',
        value_list=list(range(1, 10))  # 1 to 9
    )

    sum_of_cubes_of_1_to_3 = do(
        description='Sum of the cubes of the first 3 integers',
        item_lambda=cubed,
        seed=0.0,
        value_list=[1, 2, 3]
    )

    product_of_squares_of_1_to_5 = do(
        description='Multiplication product of the squares of the first 5 integers',
        item_lambda=squared,
        list_lambda=list_lambdas.get_item('multiply'),
        seed=1.0,
        value_list=[1, 2, 3, 4, 5]
    )

    product_of_square_of_10 = do(
        description='Multiplication product of the square of 10 only',
        item_lambda=squared,
        list_lambda=list_lambdas.get_item('multiply'),
        seed=1.0,
        value_list=[10]
    )

    average_of_sum_of_cubes_of_1_to_3 = do(
        description='Average of the sum of cubes of 1, 2 and 3',
        value_list=[sum_of_cubes_of_1_to_3, 3],
        list_lambda=list_lambdas.get_item('divide')
    )

    six_factorial = do(
        description='Six factorial',
        value_list=list(range(1, 7)),
        list_lambda=list_lambdas.get_item('multiply')
    )
