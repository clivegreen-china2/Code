# where is our list of item names?
filename: str = 'data/item_names.txt'

# open the file and read its contents:
with open(filename, 'r') as text:
    names: [str] = text.read().split('\n')

# print each name in the list:
for index, name in enumerate(names):

    # what is the position number?
    number: int = index + 1
    number_label: str = f'{number:02d} '
    print(number_label + name)
