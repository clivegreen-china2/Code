def tes(es):

    def wrapper(**kwargs):
        results: dict[str: int | float] = es(**kwargs)
        test_explain_splits(results.update(**kwargs))
        return results
    return wrapper


def test_explain_splits(info: dict) -> None:

    # unpack original inputs:
    test_amount = info.get('amount')
    test_count = info.get('count')
    test_precision = info.get('precision', 2)

    # unpack results:
    normal: float = info.get('normal')
    normal_count: int = info.get('normal_count')
    delta: float = info.get('delta')
    delta_count: int = test_count - normal_count

    # print results:
    print('RESULTS:')
    for key, value in info.items():
        print(f'{key} = {value}')
    print(f'delta_count = {delta_count}\n')

    # generate a list of split amounts
    # and add them together:
    splits: [float] = []
    splits += [normal] * normal_count
    splits += [normal + delta] * delta_count

    # successful?
    test_amount: float = (
        round(test_amount, test_precision)
    )
    splits_sum: float = (
        round(sum(splits), test_precision)
    )
    if splits_sum == test_amount:
        print('SUCCESS!')
    else:
        print('FAILURE:')
        print(
            f'test_amount = {test_amount};\n'
            f'splits_sum = {splits_sum}'
        )
