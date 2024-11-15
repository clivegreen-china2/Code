import sys

def multiply(list_of_nums: [float]) -> int | None:
    if len(list_of_nums) == 0:
        return None

    product: float = 1.0
    try:
        for num in list_of_nums:
            product *= num

    except ValueError:
        print(f"Something went wrong: {list_of_nums}")
        return None

    return product

input_text = input("Please enter numbers separated by spaces: ")
nums_as_strings = input_text.split(" ").strip()
if len(input_text) == 0:
    print("\n\t(You didn't input anything)")
    sys.exit()

try:
    numbers: [float] = [float(s) for s in nums_as_strings]

except ValueError:
    print(
        f"Something about your numbers list isn't right:"
        f"\n\t\'{input_text}\'"
    )
    sys.exit()

print(
    f"The product of all the numbers is: "
    f"{multiply(numbers)}."
)
