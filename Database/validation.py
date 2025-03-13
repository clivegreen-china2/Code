from string import ascii_letters as letters
legal_characters = letters + "\'-"


def validated_name(name: str) -> str | None:

    try:
        name = name.strip().title()
        if len(name) == 0:
            return None

        for char in name:
            if char not in legal_characters:
                return None
        return name

    except ValueError:
        return None
