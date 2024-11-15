from random import randint

def guess_int(prompt: str, answer: int) -> None:
    the_input = input(f'{prompt}')
    guess = 0
    try:
        guess = int(the_input)
    except ValueError:
        print('Not a number: \'{input}\'.')
        guess_int(prompt, answer)

    if guess == answer:
        print(f'Correct, well done! The answer is {answer}')
    elif guess < answer:
        guess_int('Too low, try again: ', answer)
    else:  # guess > answer:
        guess_int('Too high, try again: ', answer)


a, b = 1, 100
prompt = f'Guess a random integer from {a} to {b}'
answer = randint(a, b)
guess_int(prompt, answer)
