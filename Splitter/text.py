import re


def sorted_name_list(text: str) -> [str]:
    """
    proper-cases, extracts & sorts words from a string
    """
    # make all words begin with a capital letter:
    text = text.title()

    # remove any underscores:
    text = re.sub('_', '', text)
    # underscores aren't recognised by findall() ...

    matches: [str] = re.findall(r'\w+', text)
    return sorted(matches)
