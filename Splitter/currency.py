def convert_to_pennies(amount: float) -> int:
    """
    provides the nearest number of whole pennies
    equal to the amount supplied
    """
    return round(100 * float(amount))


def format_as_currency(**settings) -> str:
    """
    Converts a monetary amount provided in pennies (hundredths)
    into a currency-formatted string.
    """
    pennies: int = settings.get('pennies', 0)
    before: str = settings.get('before', '¥')
    after: str = settings.get('after', '')

    amount_in_units: float = pennies / 100
    format_str: str = "{:,.2f}"  # i.e.: two decimal places
    amount_str: str = format_str.format(amount_in_units)
    currency_str: str = f"{before}{amount_str}{after}"
    return currency_str
