# import re


class my_math(int):

    @classmethod
    def is_prime(cls, n: int) -> bool:
        # return not re.match(r'^.?$|^(..+?)\1+$', '_' * n)
        if n < 2:
            return False
        i = 2
        while i*i <= n:
            if n%i == 0:
                return False
            i += 1
        return True

    @classmethod
    def get_prime(cls):
        yield 2
        yield 3
        index: int = 1
        while True:
            six_times_index = 6 * index
            for n in (six_times_index - 1, six_times_index + 1):
                if my_math.is_prime(n):
                    yield n
            index += 1

    @classmethod
    def print_primes(cls, count: int) -> None:
        prime = my_math.get_prime()
        for i in range(count):
            print(next(prime), end=' ')


if __name__ == '__main__':
    my_math.print_primes(20000)
