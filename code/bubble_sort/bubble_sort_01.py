numbers = [25,11,19,4,8,3,17,13,6,2]

# nums_string = input("Please enter 3 integers separated with spaces:")
# numbers = nums_string.split(" ")


last = len(numbers)
while last > 1:
    for index in range(last - 1):
        i1, i2 = numbers[index], numbers[index + 1]
        if i1 > i2:
            numbers[index], numbers[index + 1] = i2, i1
    last -= 1

[print(n, end=' ') for n in numbers]
