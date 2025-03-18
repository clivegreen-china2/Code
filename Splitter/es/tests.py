def test_es(es):
    def wrapper(*args, **kwargs):
        explanation: dict = es(*args, **kwargs)
        examine(explanation)
        return explanation
    return wrapper


def examine(ex: dict) -> None:

    amount = ex.get('amount')
    count = ex.get('count')
    precision = ex.get('precision', 2)
    normal: float = ex.get('normal')
    normal_count: int = ex.get('normal_count')
    delta: float = ex.get('delta')
    delta_count: int = ex.get('delta_count')

    print('EXPLANATION:')
    for key, value in ex.items():
        print(f'\t{key} = {value}')

    splits: [float] = []
    splits += [normal] * normal_count
    splits += [normal + delta] * delta_count
    splits_sum: float = round(sum(splits), precision)

    print('\nRESULTS: ')
    print(
        f'\t{"" if splits_sum == amount else 'un'}successful'
    )
    print(f'\t{count} splits: ')
    print(f'\t{normal_count} * {normal}')
    if delta_count > 0:
        delta_amount: float = round(normal+delta, precision)
        print(f'\t{delta_count} * {delta_amount}')
    print(f'\ttotal: {splits_sum}')
