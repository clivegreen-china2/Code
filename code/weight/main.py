from inputter import Inputter as In

def run():
    weight = In(
        input_type='weight',
        # units='kg',
        min=0.5, max=5
    ).ask_for_input()

if __name__ == "__main__":
    run()
