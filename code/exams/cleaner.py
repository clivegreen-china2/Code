import string


class Cleaner:

    letters = string.ascii_lowercase
    numbers = list(range(10))
    allowed = *letters, *numbers,

    @classmethod
    def cleanup(cls, text):
        wanted = [
            ch for ch in text.lower()
            if ch in Cleaner.allowed
        ]
        return ''.join(wanted)


if __name__ == "__main__":

    print(Cleaner.cleanup("Hello -@Ther3e!"), end='')
    print(Cleaner.allowed[25])
