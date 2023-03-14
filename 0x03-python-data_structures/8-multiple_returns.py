#!/usr/bin/python3
def multiple_returns(sentence):
    len_str = 0
    frst_chr = None
    if not sentence:
        tuple_a = (len_str, frst_chr)
        return tuple_a
    len_str = len(sentence)
    frst_chr = sentence[0]
    tuple_b = (len_str, frst_chr)
    return tuple_b
