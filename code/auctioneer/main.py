import re
from auction import Auction


# get some imaginary bidders and sellers:
def import_participants() -> None:

    # we are going to store our participant names in a dictionary
    # containing two separate lists:
    participant_names: dict[str: [str]] = dict(bidder=[], seller=[])

    # populate each list:
    for kind, names in participant_names.items():

        # which file contains the kind of participants we want?
        file_name = f'data/{kind}_names.txt'

        # open the file and read its contents:
        with open(file_name, 'r') as name_strings:
            names += name_strings.read().split('\n')


def import_items() -> None:

    # where is our auction item information stored?
    file_name = f'data/items.txt'

    # open the file
    with (open(file_name, 'r') as item_strings):
        for item_string in item_strings:
            matches = re.match(parse_pattern, item_string)
            seller_name: str = matches[1]
            reserve_price: float = abs(float(matches[2]))
            description: str = matches[3]

            seller_id: int = \
                Auction.register_participant('seller', seller_name)

            new_item: [dict] = Auction.get_item_box()
            new_item.update(dict(
                seller_id=seller_id,
                reserve_price=reserve_price,
                description=description
            ))
            Auction.register_item(new_item)


if __name__ == '__main__':

    import_participants()
    participants: dict = Auction.registered_participants
    for pid, settings in participants.items():
        print(f'{pid=}, {settings}')
    print('\n\n')

    import_items()
    auction: Auction = Auction()
    auction.show_auction_board()
