def format_as_currency(the_amount: float) -> str:
    return "{:.2f}".format(the_amount)


total = float(input('Total bill: '))
count = int(input('How many people: '))
payee, payees = 'person needs', 'people need'
split = (total / count)
pennies = (total - split * count)

amount: str = ""
if pennies == 0:
    amount = format_as_currency(split)
    print(f"The split is {amount} each.")
else:
    most = count - 1
    amount = format_as_currency(split + pennies)
    print(
        f"{most} {payee if most == 1 else payees} to pay {split}\n"
        f"1 {payee} to pay {amount}."
    )
