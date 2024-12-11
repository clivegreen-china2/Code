import re
# from functools import cache


class Mymath(int):

    @classmethod
    def is_prime(cls, n: int) -> bool:

        # if n < 2:
        #     return False
        # i = 2
        # while i * i <= n:
        #     if n % i == 0:
        #         return False
        #     i += 1
        # return True
        return not re.match(r'^.?$|^(..+?)\1+$', '_' * n)

    @classmethod
    def get_prime(cls):

        yield 2
        yield 3

        index: int = 1
        while True:
            index_x6 = index * 6
            for n in (index_x6 - 1, index_x6 + 1):
                if Mymath.is_prime(n):
                    yield n
            index += 1

    @classmethod
    def print_primes(cls, count: int) -> None:

        prime = Mymath.get_prime()
        for i in range(count):
            print(next(prime), end=' ')


if __name__ == '__main__':

    Mymath.print_primes(127)
    # print(Mymath.is_prime(48_593))
