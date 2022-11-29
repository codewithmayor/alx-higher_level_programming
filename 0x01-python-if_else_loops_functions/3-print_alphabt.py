#!/usr/bin/python3
for alpha in range(ord('a'), ord('z') + 1):
    alphabet = chr(alpha)
    if alphabet not in "eq":
        print("{}".format(chr(alpha)), end="")
