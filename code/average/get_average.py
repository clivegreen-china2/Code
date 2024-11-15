import sys
message = "Input a comma-separated list of numbers. "
"Type the ENTER key to see the average:\n"

while 1:
    list_str = input(message)
    try:
        numbers = [float(n) for n in list_str.split(',')]
        print(sum(numbers)/len(numbers))
        sys.exit()
    except ValueError:
        print(
            f"Not a valid list of numbers:"
              f"\n{list_str}"
              f"\nPlease try again.\n\n"
              )
