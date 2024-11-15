

class Inputter:

    def as_number(input: str) -> float | None:
        try:
            return float(input)
        except ValueError:
            print(f"\'{input}\' is not a valid number.")
            return None

    cancel_chars: [str] = ['q', 'Q']

    def check_for_cancellation(string: str) -> None:
        if string in Inputter.cancel_chars:
            print( "\nINPUT CANCELLED" )
            import sys
            sys.exit()

    def __init__(self, **args):
        self.quantity: int | float = None
        self.input_type = args.get('input_type', 'mass')
        self.units: str = args.get('units', 'kg')
        self.min: float = float(args.get('min', 0))
        self.max: float = float(args.get('max', 1))

        prompt_text = f"{self.input_type}({self.units})".upper()
        prompt_label = f"\033[1;30;47m {prompt_text} \033[1;0;0m : "
        self.message = (
            f"Enter {self.input_type} "
            f"({self.min}{self.units} - {self.max}{self.units})"
            f"; type {' or '.join(Inputter.cancel_chars)} to cancel\n\n"
            f"{prompt_label}"
        )

    def within_range(self) -> bool:
        return self.min <= self.quantity <= self.max

    def ask_for_input(self) -> int | float:
        while self.quantity == None:
            input_string = input(self.message)
            Inputter.check_for_cancellation(input_string)

            input_number = Inputter.as_number(input_string)
            if (input_number) is not None:
                self.quantity = abs(input_number)

        print(f"{self.input_type.title()} entered: "
              f"{self.quantity}{self.units}.")

        if self.within_range():
            print("Accepted.")
            return self.quantity
        else:
            print(
                f"This value is too "
                f"{'large' if self.quantity > self.max else 'small'}."
            )
            self.quantity = None
            self.ask_for_input()
