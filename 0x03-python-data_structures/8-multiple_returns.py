#!/usr/bin/python3
def multiple_returns(sentence):
    """ returns a tuple with the length of a string and its
        first character.
    """
    length = len(sentence)
    char = sentence[0] if length > 0 else None

    return (length, char)
