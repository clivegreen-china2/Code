from random import shuffle
from explain_splits import explain_splits


if __name__ == '__main__':

    explanation: dict = explain_splits(
        amount=1743.19,
        count=17
    )

    # fairly split the amount between different people:
    names: [str] = [
        'Bashful',
        'Doc',
        'Dopey',
        'Grumpy',
        'Happy',
        'Sleepy',
        'Sneezy'
    ]
    shuffle(names)

    # use the explanation to assign amounts to people:
    ...
