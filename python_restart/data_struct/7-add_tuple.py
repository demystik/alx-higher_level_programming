#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    ta = tuple_a + (0, 0)
    tb = tuple_b + (0, 0)
    tc = (ta[0] + tb[0], ta[1] + tb[1])
    return (tc)
