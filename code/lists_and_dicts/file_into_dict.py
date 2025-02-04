from uuid import uuid1


# get a random identification number:
def get_new_id() -> int:

    # provide a 39 digit integer:
    return uuid1().int


# where is our list of item names?
filename: str = 'data/item_names.txt'

# open the file and read its contents:
with open(filename, 'r') as text:
    names: [str] = text.read().split('\n')


# where is our list of descriptions with prices?
filename: str = 'data/item_descriptions_with_prices.txt'

# open the file and read its contents:
with open(filename, 'r') as text:

    # add each line to a list:
    lines: [str] = text.read().split('\n')

# we are going to build a dictionary of dictionaries:
descriptions_with_prices: dict[int: dict] = {}

# extract the information from each line:
for index, line in enumerate(lines):

    # we need two items of information:
    description, price = line.split(' ** ')

    # we need a label and id for every item:
    number_label: str = f'{(index + 1):02d}'
    item_id: int = get_new_id()

    # create a dictionary to hold the information for one item:
    item_info = dict(
        item_id=item_id,
        description=description,
        price=float(price)
    )

    # create and add a key-value pair:
    item: dict = {number_label: item_info}
    descriptions_with_prices.update(item)


if __name__ == '__main__':

    # print each name:
    for index, name in enumerate(names):

        # what is the position number?
        number: int = index + 1
        number_label: str = f'{number:02d} '
        print(number_label + name)

    print()

    # print out the contents of the items dictionary:
    for label, item_info in descriptions_with_prices.items():

        print(label)
        key_value_pairs = item_info.items()
        [
            print(f'{k}: {v}')
            for k, v in key_value_pairs
        ]
        print()
