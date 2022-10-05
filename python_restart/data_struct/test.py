#!/usr/bin/python3

ta = (1, 2, 3, 4)
tb = (1,)
ta + (0, 0)
tb + (0, 0)
tc = (tb[0] + ta[0], tb[1] + ta[1])
print(tc)
