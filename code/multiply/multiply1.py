def multiply(nums):
    product = 1.0
    for n in nums:
        product *= n
    return product

input_text = input("Please enter numbers separated by spaces: ")
num_strings = input_text.split(" ")
numbers = [float(s) for s in num_strings]

print(
    f"The product of all the numbers in {numbers} "
    f"is: {multiply(numbers)}"
)
