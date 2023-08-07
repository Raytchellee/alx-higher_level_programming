#!/usr/bin/python3
"""Function that adds new lines after specific symbols"""


def text_indentation(text):
    """Prints the input text after adding new lines

    Args:
        text: Input text to check
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.strip()
    new_text = []

    for idx in range(len(text)):
        new_text.append(text[idx])
        if text[idx] in "?.:":
            new_text.append("\n\n")
    new_text = "".join(new_text)
    print("\n".join([line.strip() for line in new_text.split("\n")]), end="")
