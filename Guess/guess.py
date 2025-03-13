from random import randint
from sys import exit


def guess_int(prompt: str, answer: int) -> None:

    the_input = input(f'{prompt}')
    if the_input == 'x':
        exit()
    else:

        guess = 0
        try:
            guess = int(the_input)
        except ValueError:
            print('Not a number: \'{input}\'.')
            guess_int(prompt, answer)

        if guess == answer:
            print(f'Correct, well done! The answer is {answer}')
        elif guess < answer:
            guess_int(f'{guess} is too low, try again: ', answer)
        else:  # guess > answer:
            guess_int(f'{guess} is too high, try again: ', answer)


if __name__ == '__main__':

    limit: str = input('Enter a positive integer:')
    a: int = 1
    b: int = int(limit)
    my_prompt = f'Guess a random integer from {a} to {b}: '
    my_answer = randint(a, b)
    guess_int(my_prompt, my_answer)
