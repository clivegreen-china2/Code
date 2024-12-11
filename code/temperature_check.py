from random import randrange


class Checker:

    min_temp: int = -25
    max_temp: int = -18


    @classmethod
    def get_random_temp(cls) -> int:
        return randrange(Checker.min_temp-10, Checker.max_temp+10)


    current_temp: int = -22

    @classmethod
    def get_random_temperature(cls) -> int:
        start: int = Checker.min_temp - 5
        return


    min_exceeded_count, min_exceeded_limit = 0, 10
    min_exceeded: bool = False
    max_exceeded_count, max_exceeded_limit = 0, 5
    temp_ok_count = 0

    @classmethod
    def problem_found(cls)-> bool:
        ...


    @classmethod
    def temp_in_range(cls) -> bool:
        return Checker.min_temp <= Checker.current_temp <= Checker.max_temp

    @classmethod
    def check(cls) -> bool:

        if Checker.temp_in_range():
            Checker.temp_ok_count += 1
        elif Checker.current_temp < Checker.min_temp:
            Checker.min_exceeded_count += 1
        else:
            Checker.max_exceeded_count += 1

        if Checker.min_exceeded_count > Checker.min_exceeded_limit:
            print('Too Cold: Call an Engineer!')
        elif Checker.max_exceeded_count > Checker.max_exceeded_limit:
            print('Too hot - sound the alarm!')


while
    ...

print()
