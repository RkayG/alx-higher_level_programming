#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        sentence[0] = None
    tuple_sen = (len(sentence), sentence[0])
    return (tuple_sen)
