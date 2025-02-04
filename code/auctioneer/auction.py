from uuid import uuid1


class Auction:

    # shared settings for all auctions:
    minimum_auction_item_count: int = 10
    sale_fee_percentage: int = 10

    # known participants (sellers and bidders) with (nick)names:
    registered_participants: dict[int: str] = dict()

    # all auction items are kept here:
    registered_items: dict[int: dict] = dict()

    # used to create new seller items for auction:
    item_box_template = dict(

        # set when the item is created:
        item_id=None,
        seller_id=None,
        reserve_price=None,
        description=None,

        # updated during auction:
        number_of_bids=0,
        current_highest_bid=0,
        highest_bidder_id=None,

        # updated when an item is successfully auctioned:
        sold=False,
        sale_price=None,
        buyer_id=None,

        # updated when payment is complete:
        buyer_has_paid=False,
        seller_has_been_paid=False,
        commission_earned=0.00
    )

    @classmethod
    def get_new_id(cls) -> int:

        return uuid1().int

    @classmethod
    def short_id(cls, long_id: int) -> str:
        last_six_digits: str = str(long_id)[-6:]
        return last_six_digits

    @classmethod
    def is_valid_id(cls, id_num: int) -> bool:

        # check for a positive 39-digit integer:
        return (
                isinstance(id_num, int) and
                id_num > 0 and
                len(str(id_num)) == 39)

    @classmethod
    def register_participant(cls, role: str, moniker: str | None) -> int:

        participant: dict[int: dict] = dict()

        if role not in ['bidder', 'seller']:
            role = 'bidder'

        new_id: int = Auction.get_new_id()
        if moniker is None or moniker == '':
            moniker = f'{role}_{Auction.short_id(new_id)}'

        participant.update(dict(
            id=new_id,
            role=role,
            moniker=moniker
        ))

        Auction.registered_participants.update({new_id: participant})
        return new_id

    @classmethod
    def register_item(cls, item_box: dict) -> int | None:

        """
        Checks the submitted item box's contents, and
        stores the successfully validated item
        :param item_box: a dictionary of settings
        :return: the integer id of the stored item,
        or None if validation was unsuccessful
        """

        # validate item details here:
        if (
                item_box.get('seller_id') is None or
                item_box.get('reserve_price') is None or
                item_box.get('description') is None
        ):
            print(
                'Item could not be registered.\n'
                'Check your seller, reserve price and description details.\n'
            )
            return None

        else:
            # get a fresh id:
            item_id: int = Auction.get_new_id()

            # this id is stored as both a key and a value:
            item_box['item_id'] = item_id
            Auction.registered_items.update({item_id: item_box})
            return item_id

    @classmethod
    def get_input(cls, msg: str) -> str:

        input_text: str = input(f'{msg}\n(or type x to cancel): ').strip()
        if input_text == 'x':
            exit()
        return input_text

    @classmethod
    def input_bidder_id(cls) -> int:

        input_text: str = Auction.get_input('Enter your bidder id')
        candidate_id: int = int(input_text)
        if candidate_id in Auction.registered_participants.keys:
            return candidate_id
        else:
            print(
                'You need to enter the 39-digit\n'
                'bidder id number you were given.\n'
                'Please try again.'
            )
            return Auction.input_bidder_id()

    @classmethod
    def input_item_number(cls, count: int) -> int:

        input_text: str = Auction.get_input(
            f'Type a number from 1 to {count}\n'
            f'representing the item you wish to bid for'
        )

        num: int = int(input_text)
        if 1 <= num <= count:
            return num

        else:
            print(
                f'{num} is outside the range of valid numbers.\n'
                f'Please try again.'
            )
            return Auction.input_item_number(count)

    @classmethod
    def input_price(cls, current_price: float) -> float:

        input_text: str = Auction.get_input(
            f'Type a bid price (greater than {current_price:.2f})'
        )

        num: float = float(input_text)
        if num > current_price:
            return num

        else:
            print(
                f'{num:.2f} must be greater than the current price.\n'
                f'Please try again.'
            )
            return Auction.input_price(current_price)

    @classmethod
    def confirm_bid(cls, message: str, signal: str = 'y') -> bool:

        return Auction.get_input(message) == signal

    @classmethod
    def get_item_box(cls) -> dict:

        # returns an uninitialized container for an item:
        return Auction.item_box_template.copy()

    @classmethod
    def get_item(cls, item_id: int) -> dict | None:

        # retrieve (a reference to) the container for an item -
        # note that modifying the contents of this container
        # will update the original item's details:
        return Auction.registered_items.get(item_id, None)

    def __init__(self):

        # create a new auction:
        self.auction_items: dict[int: dict] = {}
        self.auction_item_count: int = 0
        self.auction_can_proceed: bool = False
        self.initialize()

    def initialize(self) -> None:

        # set up a new or existing auction:
        self.auction_items.clear()
        items = Auction.registered_items.values()

        # collect all currently unsold items:
        position: int = 1
        for item in items:
            if item.get('sold') is False:
                self.auction_items.update({position: item})
                position += 1

        # are there enough items to open the auction with?
        self.auction_item_count = len(self.auction_items.items())
        self.auction_can_proceed = (
                self.auction_item_count >=
                Auction.minimum_auction_item_count
        )

    def show_auction_board(self) -> None:

        if not self.auction_can_proceed:
            min_count = Auction.minimum_auction_item_count
            print(
                'The auction cannot proceed.\n'
                f'Are at least {min_count} unsold items available?'
            )
            return

        print('AUCTION BOARD')
        print(f'{self.auction_item_count} items at auction:\n')

        for number, item in self.auction_items.items():

            num_str: str = f'{number:02d}'
            desc: str = item.get('description')
            reserve_price: float = item.get('reserve_price')
            number_of_bids: int = item.get('number_of_bids')

            print(
                f'\t{num_str}:\n'
                f'\t{desc}\n'
                f'\treserve price: ${reserve_price:,.2f}\n',
                f'\tnumber of bids: {number_of_bids}\n'
            )

    def input_bid(self) -> bool:

        if not self.auction_can_proceed:
            "Auction closed. Bids no longer accepted."
            return False

        # who is bidding?
        bidder_id: int = Auction.input_bidder_id()

        nickname: str = Auction.registered_participants.get(bidder_id)
        print(f'Thank you, {nickname}.')

        # which item is being bid for?
        count = self.auction_item_count
        item_number: int = Auction.input_item_number(count)
        item: dict = self.auction_items.get(item_number)
        item_id: int = item.get('item_id')
        description: str = item.get('description')

        # what is the price being bid?
        current_price: float = item.get('current_highest_bid')
        new_price: float = Auction.input_price(current_price)

        # ask for confirmation before submitting the bid:
        msg: str = (
            f'A bid of ${new_price:.2f} by {nickname}\n'
            f'will be offered for the following item:\n'
            f'item_id: {item_id}\n'
            f'description: {description}'
        )
        signal: str = 'y'
        confirmed: bool = Auction.confirm_bid(msg, signal)

        if confirmed:
            item.update(dict(
                highest_bidder_id=bidder_id,
                current_highest_bid=new_price,
                number_of_bids=item.get('number_of_bids') + 1
            ))
        return confirmed


if __name__ == '__main__':
    ...
